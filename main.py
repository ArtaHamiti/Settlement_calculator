
import db

def main():
    print("Velkommen. Velg handling: [1/2]")
    print("1. Se status for hvem som skylder hvem.")
    print("2. Legg inn et utlegg")

    dbPath = "data.csv"

    db.MakeCSV(dbPath)
    
    db.AddPayment(dbPath,"Gustav",10.0)

    db.FindPayments(dbPath)

    return

main()