import os

def walk():
    for root, dirs, files in os.walk('.'):
        print("root: {}".format(root))
        for dir in dirs:
            print("dir: {}".format(dir))
        for file in files:
            print("file: {}".format(file))

if __name__ == "__main__":
    walk()