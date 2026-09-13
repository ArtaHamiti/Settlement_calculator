
import db

dbPath = "data.csv"

#db.MakeCSV(dbPath)

def main():
    while True:
        print("Velkommen. Velg handling: [1/2/3]")
        print("1. Se status for hvem som skylder hvem.")
        print("2. Legg inn et utlegg")
        print("3. Endre spesifikt utlegg")


        arg = input()
        match arg:
            case "1":
                break
            case "2":
                input("Angiv [person,verdi,dato]")
            case _:
                continue
    db.PrintList(db.FindPayments(dbPath))

    print(db.CurrentBalance(dbPath))
    print("ferdi snakka")
    return

main()