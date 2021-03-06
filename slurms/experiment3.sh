#!/usr/bin/env bash

#SBATCH -J 'experiment3'
#SBATCH -o outputs/slurm-%j-experiment3.out
#SBATCH -p all
#SBATCH -t 1500

echo "In the directory: `pwd` "
echo "As the user: `whoami` "
echo "on host: `hostname` "

echo "With access to cpu id(s): "
cat /proc/$$/status | grep Cpus_allowed_list

echo "Array Allocation Number: $SLURM_ARRAY_JOB_ID"
echo "Array Index: $SLURM_ARRAY_TASK_ID"

module load anaconda/4.4.0
source activate thesis

echo "Create data for experiments 1 and 2"
python /home/cc27/Thesis/narrative/src/run_engine.py variablefiller_train  80000 1
python /home/cc27/Thesis/narrative/src/run_engine.py variablefiller_test 20000 1
python /home/cc27/Thesis/narrative/combine_storyfolders.py variablefiller_train_gensymbolicstates_80000_1 variablefiller_test_gensymbolicstates_20000_1 variablefiller_gensymbolicstates_100000_1
