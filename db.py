
import csv

def MakeCSV(csvfile:str) -> None:
    with open(csvfile,mode="w",newline='') as file:
        file.write("who,value\n")

def FindPayments(csvfile:str, who:str = "", value:float = 0.0) -> list | None:

    with open(csvfile, mode ="r", newline='') as file:
        data = csv.reader(file)
        out = []
        for row in data:
            print(row)
            if who == "" and value == 0.0:
                return data
            if (who != "" and row[0] == who) or (value != "" and row[1] == value):
                out.append(row)
        
    return out if len(out)>0 else None

def RemovePayment(csvfile:str, who:str = "", value:float = 0.0) -> bool:

    if who == "" and value == 0.0:
        return False
    
    with open(csvfile, mode="r", newline='') as file:
        data = csv.reader(file)
        out = []
        for row in data:
            if row[0] != who and row[1] != value:
                out.append(row)
    with open(csvfile,mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return True

def AddPayment(csvfile:str, who:str, value:float) -> None:
    
    with open(csvfile, mode="a", newline='') as file:
        file.write(f"{who},{value}\n")

    return   


