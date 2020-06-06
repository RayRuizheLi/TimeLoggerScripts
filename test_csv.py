from datetime import timedelta
import datetime
import csv

def main():

    cost = []
    write = []

    input_file = input()
    output_file = input()

    with open('cost.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for field in row:
                cost.append(field)

    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        isFound = False
        costRows = []
        print("Income: ")
        write.append(['\nIncome'])
        costTotal = 0 
        incomeTotal = 0
        
        for row in csv_reader:
            isCost = False
            
            for field in row:
                if field == "%":
                    isFound = True
                    break
                if field in cost:
                    isCost = True; 

            if not isFound: 
                continue

            if isFound and ':' in row[1] and "Total" not in row[0]:
                time = int(row[1][0:1]) * 60 * 10 + int(row[1][1:2]) * 60 + int(row[1][3:4]) * 10 + int (row[1][4:5])
                if isCost:
                    costTotal += time                
                else:
                    incomeTotal += time            
            if isFound:
                if isCost:
                    costRows.append(row)
                elif "Total" not in row[0]:
                    print(" ".join(row) + "%")
                    write.append(row)
        print("\nCost: ")
        write.append(['\nCost'])
        for row in costRows:
             print(" ".join(row) + "%")
             write.append(row)   
        eff = (incomeTotal / (incomeTotal + costTotal)) * 100
        tenH =  60 * 60
        trueEff = incomeTotal / tenH * 100 
        rev = (incomeTotal - costTotal) / 60
        total = (incomeTotal + costTotal) / 60
        combine = "\nTotal: {:.2f} Income: {:.2f} Cost: {:.2f} Revenue: {:.2f} Efficiency: {:.2f}% True Efficiency: {:.2f}%".format(total, incomeTotal / 60, costTotal / 60, rev, eff, trueEff)
        print(combine)
        write.append([combine])

    with open(output_file, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in write:
            writer.writerow(line)

if __name__ == '__main__':
    try:
        main()
    except:
        print("Error, files don't exist.")

