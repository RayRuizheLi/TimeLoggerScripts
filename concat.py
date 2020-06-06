import csv

def main():

    print('output file name:')
    output_file = input()
    
    print('input file names (type end to end):') 
    files = []
    inFlag = True 
    while inFlag:
        tmp = input()
        if tmp == 'end':
            break;
        else:
            files.append(tmp)

    lines = []

    for file in files: 
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader: 
                lines.append(row)
        
        lines.append([])
    
    with open(output_file, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in lines:
            writer.writerow(line)



if __name__ == '__main__':
    try: 
        main()
    except: 
        print("files don't exist")

