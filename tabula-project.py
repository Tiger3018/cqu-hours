#!/usr/bin/env python3
import os, sys, tabula, traceback, csv

def tabula_project():
    for file in os.listdir():
        replaceName = file.strip(".pdf") + ".tabula.csv"
        if file.endswith(".pdf") and not os.path.exists(replaceName):
            print("Start with {}.".format(file))
            try:
                tabula.convert_into(file, replaceName, pages="all")
            except Exception as e:
                traceback.print_exc()
            else:
                print("Done with {}.".format(file))

def csv_project(stuNumber):
    for file in os.listdir():
        if file.endswith(".tabula.csv"):
            with open(file, newline='') as f:
                try:
                    csvFile = csv.reader(f, delimiter=',')
                    for line in csvFile:
                        if line[0].find(str(stuNumber)) != -1:
                            print(line)
# [CONFIG] If you want to get the specific source file, you should uncomment next line.
                            # print("\nIN file:{}".format(file))
# [CONFIG] If you want to get the specific source file, you should uncomment next 3 lines.
                        # for i in line:
                        #     if i.find(str(stuNumber)) != -1:
                        #         print(line)
                except Exception:
                    print("WHEN READING {}, some error happened.".format(file))
                    traceback.print_exc()

if __name__ == "__main__":
    argDir = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "."
    try:
        stuNumber = int(sys.argv[2])
    except Exception:
        print("stuNumber can't be reached.")
        stuNumber = 0
    os.chdir(argDir)
    tabula_project()
    print("Get {} for your hours...".format(stuNumber))
    csv_project(stuNumber)
    print("Exiting...")
