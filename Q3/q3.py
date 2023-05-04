def main():
    import csv
    f=open('q3.csv', encoding='cp949')
    data=csv.reader(f)
    header=next(data)

    totals = [0]*9
    
    max_1 = 0
    max_2 = 0
    min_1 = 999999999
    min_2 = 999999999

    max_h1 = ''
    max_h2 = ''
    min_h1 = ''
    min_h2 = ''

    for row in data:
        if row[1]=="1호선":
            total=int(row[4])+int(row[5])
            totals[0] = totals[0] + total
        elif row[1]=="2호선":
            total=int(row[4])+int(row[5])
            totals[1] = totals[1] + total
        elif row[1]=="3호선":
            total=int(row[4])+int(row[5])
            totals[2] = totals[2] + total
        elif row[1]=="4호선":
            total=int(row[4])+int(row[5])
            totals[3] = totals[3] + total
        elif row[1]=="5호선":
            total=int(row[4])+int(row[5])
            totals[4] = totals[4] + total
        elif row[1]=="6호선":
            total=int(row[4])+int(row[5])
            totals[5] = totals[5] + total
        elif row[1]=="7호선":
            total=int(row[4])+int(row[5])
            totals[6] = totals[6] + total
        elif row[1]=="8호선":
            total=int(row[4])+int(row[5])
            totals[7] = totals[7] + total
        elif row[1]=="9호선":
            total=int(row[4])+int(row[5])
            totals[8] = totals[8] + total
        else:
            continue

    count = 0;
    
    for i in totals:
        count += 1
        if max_1 < i:
            max_2 = max_1
            max_1 = i
            max_h2 = max_h1
            max_h1 = count
        elif max_1>i and i>max_2:
            max_2 = i
            max_h2 = count

        if min_1 >i:
            min_2 = min_1
            min_1 = i
            min_h2 = min_h1
            min_h1 = count
            
        elif min_1<i and i<min_2:
            min_2 = i
            min_h2 = count
        
            
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line",max_h1,"(",max_1,")")
    print("12nd Busiest Line: Line",max_h2,"(",max_2,")")
    print("1st Least used Line: Line",min_h1,"(",min_1,")")
    print("2nd Least used Line: Line",min_h2,"(",min_2,")")
    f.close()

if __name__ == '__main__':
    main()


