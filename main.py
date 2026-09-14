

import os
import pandas as pd

dbPath = "data.csv"
#db.MakeCSV(dbPath)

def main():

    breakOuter = False

    while True:

        if breakOuter:
            break
        breakOuter = True

        arg = input("What csv? ")
        filePath = f"Settlements/{arg}.csv"


        if not os.path.isfile(filePath):
            while True:
                newQ = input("Couldn't find file, want new? (y/n) ")
                if newQ not in ("y","n"):
                    continue
                break
            if newQ == "n":
                breakOuter = False
                continue
            
            while True:
                who = input("Who is the settlement for? (separate names by comma) ")
                whoList = who.split(",")
                while True:
                    newQ = input(f"Is {whoList} correct? (y/n) ")
                    if newQ not in ("y","n"):
                        continue
                    break
                if newQ == "n":
                    continue
                
                whoList.extend(["value","who","when"])
                df = pd.DataFrame(columns=whoList)
                df.to_csv(filePath, index=False,header=True)
                break
        
        
    while True:
        arg = input("What action? (a - add, s - status)")

        match arg:
            case "a":
                pass
            case "s":
                pass
            case _:
                continue

        



main()