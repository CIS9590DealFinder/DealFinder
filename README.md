# DealFinder
# Introduction
The goal of this project is to run a python file, using Intel One API. We designed a python script to analyze past taxi data from a kaggle dataset: https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc. 

# Intel® oneAPI
Using Intel OneAPI is a manual process. The steps are:

> wget https://raw.githubusercontent.com/CIS9590DealFinder/DealFinder/main/inteloneapi.sh

> qsub -l nodes=1:gpu:ppn=2 -d . inteloneapi.sh

> qsub -I -l nodes=1:gpu:ppn=2 -d .

> bash inteloneapi.sh 

This code can be input into a ssh terminal such as Git Bash. The code will download the shell script will submit jobs to a queue for execution on compute nodes. This way, we can run the code efficiently. Without splitting the jobs into compute nodes, the scripts will be too resource intensive to run.
