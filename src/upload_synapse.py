import os
import sys

def create_project(projectID=None):
    project = Project('My uniquely named project')
    project = syn.store(project)

def upload_derivatives(localdir='data/cpac/derivatives'):
    walked_path = os.walk(localdir)
    for dirpath,dirnames,filenames in walked_path:
        if filenames: 
            print(dirpath)
            for filename in filenames:
                print(filename)
        else:
            print(dirpath)
            print(dirnames)

def main():
 # print command line arguments
    #datadir = sys.argv[1]
    upload_derivatives()

if __name__ == "__main__":
    main()