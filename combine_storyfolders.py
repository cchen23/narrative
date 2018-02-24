import ast
import sys

def make_helper_filename(foldername, helpername):
    split_name = foldername.split("_")
    split_helpername = split_name[:-2] + [helpername] + split_name[-2:]
    return "_".join(split_helpername)

def combine_storyfolders(inputname1, inputname2, outputname):
    STORY_BASEPATH = "/home/cc27/Thesis/narrative/story/"
    with open("%s%s/%s.txt" % (STORY_BASEPATH, outputname, outputname), 'wb') as outfile:
        with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname1, inputname1), 'rb') as infile:
            outfile.write(infile.read())
        with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname2, inputname2), 'rb') as infile:
            outfile.write(infile.read())

    with open("%s%s/%s.txt" % (STORY_BASEPATH, outputname, make_helper_filename(outputname, "QA")), 'wb') as outfile:
        with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname1, make_helper_filename(inputname1, "QA")), 'rb') as infile:
            outfile.write(infile.read())
        with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname2, make_helper_filename(inputname2, "QA")), 'rb') as infile:
            outfile.write(infile.read())

    with open("%s%s/%s.txt" % (STORY_BASEPATH, outputname, make_helper_filename(outputname, "entities")), 'wb') as outfile:
            with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname1, make_helper_filename(inputname1, "entities")), 'rb') as infile1:
                with open("%s%s/%s.txt" % (STORY_BASEPATH, inputname2, make_helper_filename(inputname2, "entities")), 'rb') as infile2:
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
