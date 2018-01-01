#!/usr/bin/env bash
#this script dumps some basic information to an output file when submitted via sbatch

#name the job nodeinfo and place it's output in a file named slurm-<jobid>.out
#set partition to 'all' this isn't strictly necessary but it's good practice
#set time to 5 minutes so jobs get killed if something weird happens

#SBATCH -J 'writestories'
#SBATCH -o outputs/slurm-%j-writestories.out
#SBATCH -p all
#SBATCH -t 1500

echo "In the directory: `pwd` "
echo "As the user: `whoami` "
echo "on host: `hostname` "

echo "With access to cpu id(s): "
cat /proc/$$/status | grep Cpus_allowed_list

echo "Array Allocation Number: $SLURM_ARRAY_JOB_ID"
echo "Array Index: $SLURM_ARRAY_TASK_ID"

echo "Generate data"
module load anaconda/4.4.0
source activate thesis
# date
# echo "***************************************** Generate poetry_toy stories *****************************************"
# python /home/cc27/Thesis/narrative/src/run_engine.py poetry_toy 100000 1 > outputs/$(date +"%Y%m%d%k%M%s")_writestories_CSWpoetrytoy.txt
# date
# echo "***************************************** Generate coffeeshop_simple stories *****************************************"
# python /home/cc27/Thesis/narrative/src/run_engine.py coffeeshop_simple 100000 1 > outputs/$(date +"%Y%m%d%k%M%s")_writestories_CSWcoffeeshopsimple.txt
date
echo "***************************************** Generate coffeeshop_differentlengths stories *****************************************"
python /home/cc27/Thesis/narrative/src/run_engine.py coffeeshop_differentlengths 100000 1 > outputs/$(date +"%Y%m%d%k%M%s")_writestories_CSWcoffeeshopdifferentlengths.txt
date
echo "Finished"
