#import difflib

#file1 = open('text_1.txt', 'r',)
#file2 = open('text_2.txt', 'r')

#diff = difflib.ndiff(file1.readlines(), file2.readlines())
#delta = ''.join(x[2:] for x in diff if x.startswith('- '))
#print (delta)

# Open File in Read Mode
#file_1 = open('text_1.txt',  'r',encoding="utf-8")
#file_2 = open('text_2.txt',  'r',encoding="utf-8")

#print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')

#file_1_line = file_1.readline()
#file_2_line = file_2.readline()

# Use as a COunter
#line_no = 1

#print()
#same=[]
#with open('file1.txt', encoding="utf-8") as file1:
    #with open('file2.txt', encoding="utf-8") as file2:
        #same = set(file1).intersection(file2)

#print("Common Lines in Both Files")

#for line in same:
    #print(line, end='')

#print('\n')
#print("Difference Lines in Both Files")
#while file_1_line != '' or file_2_line != '':

    # Removing whitespaces
    #file_1_line = file_1_line.rstrip()
    #file_2_line = file_2_line.rstrip()

    # Compare the lines from both file
    #if file_1_line != file_2_line:

        # otherwise output the line on file1 and use @ sign
        #if file_1_line == '':
            #print("@", "Line-%d" % line_no, file_1_line)
        #else:
            #print("@-", "Line-%d" % line_no, file_1_line)

        # otherwise output the line on file2 and use # sign
        #if file_2_line == '':
            #print("#", "Line-%d" % line_no, file_2_line)
        #else:
            #print("#+", "Line-%d" % line_no, file_2_line)

        # Print a empty line
        #print()

    # Read the next line from the file
    #file_1_line = file_1.readline()
    #file_2_line = file_2.readline()

    #line_no += 1

#file_1.close()
#file_2.close()

import argparse
import difflib
import sys

from pathlib import Path


def create_diff(old_file: Path, new_file: Path, output_file: Path = None):
    file_1 = open(old_file,'r', encoding="utf-8").readlines()
    file_2 = open(new_file,'r', encoding="utf-8").readlines()
    #print('file_1=',file_1)

    if output_file:
        delta = difflib.HtmlDiff().make_file(
            file_1, file_2, old_file, new_file
        )
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(delta)
    else:
        delta = difflib.unified_diff(file_1, file_2, old_file.name, new_file.name)
        sys.stdout.writelines(delta)


def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("old_file_version")
    #parser.add_argument("new_file_version")
    #parser.add_argument("--html", help="specify html to write to")
    #args = parser.parse_args()

    #old_file = Path(args.old_file_version)
    #new_file = Path(args.new_file_version)

    #if args.html:
        #output_file = Path(args.html)
    #else:
        #output_file = None

    create_diff('file1.txt', 'file2.txt', 'ou.html')


if __name__ == "__main__":
    main()
