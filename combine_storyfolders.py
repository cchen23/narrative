"""Combines stories in two folders.

Used to combine train and test story folders.
Train and test stories are generated using separate files to enforce separate
train and test fillers. Experiment writers (experiment_writer_rolefillerbinding.py)
then separate these stories into a train and test set. Stories are combined into
a single file (as opposed to separately generating train and test sets) to ensure
that non-filler words share the same representations across datasets.

Assumes stories are generated using run_engine.py.
"""
import ast
import os
import sys

def make_helper_filename(foldername, helpername):
    """Generates the name of a file created by run_engine.py.

    Assumes stories are generated using run_engine.py.

    Args:
        foldername: Name of folder containing helper files.
        helpername: Specifier for helper file. Options: ["QA", "entities"]
    """
    split_name = foldername.split("_")
    split_helpername = split_name[:-2] + [helpername] + split_name[-2:]
    return "_".join(split_helpername)

def combine_storyfolders(inputname1, inputname2, outputname):
    """Combine stories from two folders.

    Assumes stories are generated using run_engine.py.

    Args:
        inputname1: Folder name containing first set of stories.
        inputname2: Folder name containing second set of stories.
        outputname: Folder name for combined stories.

    Saves:
        Files for combined stories.
    """
    STORY_BASEPATH = "/home/cc27/Thesis/narrative/story/"
    output_dir = os.path.join(STORY_BASEPATH, outputname)
    input1_dir = os.path.join(STORY_BASEPATH, inputname1)
    input2_dir = os.path.join(STORY_BASEPATH, inputname2)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, outputname + ".txt"), 'wb') as outfile:
        with open(os.path.join(input1_dir, inputname1 + ".txt"), 'rb') as infile:
            outfile.write(infile.read())
        with open(os.path.join(input2_dir, inputname2 + ".txt"), 'rb') as infile:
            outfile.write(infile.read())

    with open(os.path.join(output_dir, make_helper_filename(outputname, "QA") + ".txt"), 'wb') as outfile:
        with open(os.path.join(input1_dir, make_helper_filename(inputname1, "QA") + ".txt"), 'rb') as infile:
            outfile.write(infile.read())
        with open(os.path.join(input2_dir, make_helper_filename(inputname2, "QA") + ".txt"), 'rb') as infile:
            outfile.write(infile.read())

    with open(os.path.join(output_dir, make_helper_filename(outputname, "entities") + ".txt"), 'wb') as outfile:
            with open(os.path.join(input1_dir, make_helper_filename(inputname1, "entities") + ".txt"), 'rb') as infile1:
                with open(os.path.join(input2_dir, make_helper_filename(inputname2, "entities") + ".txt"), 'rb') as infile2:
                    entities1 = ast.literal_eval(infile1.readline())
                    entities2 = ast.literal_eval(infile2.readline())
                    assignments = ast.literal_eval(infile1.readline())
                    entities = {k:entities1[k]+entities2[k] for k in entities1.keys()}
                    outfile.write(str(entities))
                    outfile.write('\n')
                    outfile.write(str(assignments))

if __name__ == '__main__':
    inputname1 = sys.argv[1]
    inputname2 = sys.argv[2]
    outputname = sys.argv[3]
    combine_storyfolders(inputname1, inputname2, outputname)
