#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('taxi_tripdata.csv')
df = df.drop(['ehail_fee', 'VendorID', 'trip_type', 'congestion_surcharge','store_and_fwd_flag','RatecodeID','payment_type'], axis= 1)
df = df[df['total_amount'] > 0]
df = df[df['fare_amount'] > 0]
df = df[df['trip_distance'] > 0]

for i in df.columns[[0, 1]]:
    df[i] = pd.to_datetime(df[i])

time_diff = df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']
duration = []
for x in time_diff :
    duration.append(x.total_seconds() / 60)

df['duration'] = duration
df['duration'] = df['duration'].round(2)

df.loc[df['passenger_count'].isna(), 'passenger_count'] = 1.0

df['tip_pct'] = pd.to_numeric(df['tip_amount']/df['fare_amount'])
df['week'] = df['lpep_pickup_datetime'].dt.day_name()

df['hour'] = df['lpep_pickup_datetime'].dt.hour


days= ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
plt.figure(figsize= (20, 10))
Day = df.groupby('week')['PULocationID'].count().reindex(days).reset_index()
sns.set_style("darkgrid")

plt.figure(figsize=(20,10))
ax = sns.barplot(x="week", y="PULocationID",data=Day)

ax.set_ylabel("Number of Rides",fontsize=18)
ax.set_xlabel("Day of Week",fontsize=18)
plt.title('Number of Rides by Day', fontsize=20)

plt.savefig("Rides_Day.png",dpi=300)
plt.show()

plt.figure(figsize= (20, 10))
ax1 = sns.countplot(x= 'hour', data= df,color='royalblue')

ax1.set_ylabel("Number of Rides",fontsize=18)
ax1.set_xlabel("Hour of Day",fontsize=18)
plt.title('Number of Rides by the Hour', fontsize=20)

plt.savefig("Rides_Hour.png",dpi=300)

plt.show()


tip_pct_week = df.groupby('week')['tip_pct'].mean().reindex(days).reset_index()

plt.figure(figsize= (20, 10))
ax2 = sns.barplot(x='week',y='tip_pct',data=tip_pct_week)

ax2.set_ylabel("Percent of Tip",fontsize=18)
ax2.set_xlabel("Day of Week",fontsize=18)
plt.title('Average Tip Percent by Day', fontsize=20)

plt.savefig("Tip_Day.png",dpi=300)

plt.show()


plt.figure(figsize= (20, 10))
tip_pct_hour = df.groupby('hour')['tip_pct'].mean().reset_index()
ax3 = sns.barplot(x='hour',y='tip_pct',data=tip_pct_hour,color='royalblue')

ax3.set_ylabel("Percent of Tip",fontsize=18)
ax3.set_xlabel("Hour of Day",fontsize=18)
plt.title('Average Tip Percent by Hour', fontsize=20)

plt.savefig("Tip_Hour.png",dpi=300)

plt.show()

