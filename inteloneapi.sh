#1/bin/bash
rm DealFinder
mkdir DealFinder
cd DealFinder
wget https://github.com/CIS9590DealFinder/DealFinder/raw/main/taxi_tripdata.csv
wget https://raw.githubusercontent.com/CIS9590DealFinder/DealFinder/main/TaxiProject.py
pip install seaborn
ipython TaxiProject.py
ls