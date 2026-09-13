
import csv


def MakeCSV(csvfile:str) -> None:
    with open(csvfile,mode="w",newline='') as file:
        file.write("who,value,when\n")

def FindPayments(csvfile:str, who:str = "", value:float = 0.0,when:int = 0) -> list | None:

    with open(csvfile, mode ="r", newline='') as file:
        data = csv.reader(file)
        out = []
        for row in data:
            if (who == "" and value == 0.0 and when == 0) or (who != "" and row[0] == who) or (value != "" and row[1] == value) or (when != 0 and row[2]==when):
                out.append(row)
        
    return out if len(out)>0 else None

def RemovePayment(csvfile:str, who:str = "", value:float = 0.0, when:int = 0) -> bool:

    if who == "" and value == 0.0 and when == 0:
        return False
    
    with open(csvfile, mode="r", newline='') as file:
        data = csv.reader(file)
        out = []
        for row in data:
            if row[0] != who and row[1] != value and row[2]!= when:
                out.append(row)
    with open(csvfile,mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return True

def AddPayment(csvfile:str, who:str, value:float, when:int) -> None:
    
    with open(csvfile, mode="a", newline='') as file:
        file.write(f"{who},{value},{when}\n")


def PrintList(lst:list) -> None:
    for row in lst:
        print(f"{row[0]}, {row[1]},{row[2]}")

def CurrentBalance(csvfile:str) -> dict:
    with open(csvfile, mode="r", newline='') as file:
        data = csv.reader(file)
        paymentTotals = {}
        for row in data:
            if row[0] !="who":
                if row[0] not in paymentTotals:
                    paymentTotals[row[0]] = float(row[1])
                else:
                    paymentTotals[row[0]] += float(row[1])

        totalExpenses = 0.0
        out = {}
        for person in paymentTotals:
            totalExpenses+=paymentTotals[person]
            out[person] = 0.0

        for person in paymentTotals:
            out[person] = totalExpenses/len(paymentTotals) - paymentTotals[person]

        return out
        
