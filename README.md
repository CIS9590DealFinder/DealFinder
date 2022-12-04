# DealFinder
# Introduction
The goal of this project is to run a python file, using Intel One API. We designed a python script to analyze past taxi data from a kaggle dataset: https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc. 

# Intel® oneAPI via Devcloud
To connect to the devcloud, documentation can be found here: https://devcloud.intel.com/oneapi/documentation/connect-with-ssh-linux-macos/. 

Using Intel OneAPI is a manual process but we have automated it as much as possible. The steps are:

> ssh devcloud

> wget https://raw.githubusercontent.com/CIS9590DealFinder/DealFinder/main/inteloneapi.sh

> qsub -l nodes=2:gen9:ppn=2 -d . inteloneapi.sh

> qsub -I -l nodes=2:gen9:ppn=2 -d .

> bash inteloneapi.sh 

This code has to be inputted into a SSH terminal such as Git Bash. The code will download the shell script and executes it by submit jobs to a queue for execution. By taking advantage of Intel OneAPI and hetergoenous computing, the code was able to run efficiently. Without splitting the jobs into compute nodes, the scripts would have been too resource intensive to run.


