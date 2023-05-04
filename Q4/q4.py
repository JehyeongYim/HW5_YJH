def main():
    import csv
    f=open('q4.csv', encoding='cp949')
    data=csv.reader(f)
    header=next(data)

    max_1 = 0
    min_1 = 9999999
    max_2 = 0
    min_2 = 9999999
    max_3 = 0
    min_3 = 9999999
    max_4 = 0
    min_4 = 9999999
    
    max_s1 = ''
    min_s1 = ''
    max_s2 = ''
    min_s2 = ''
    max_s3 = ''
    min_s3 = ''
    max_s4 = ''
    min_s4 = ''

    for row in data:
        if row[1]=="1호선":
            total=int(row[4])+int(row[5])
            if total>max_1:
                max_1 = total
                max_s1 = row[3]
            if total<min_1:
                min_1 = total
                min_s1 = row[3]

        elif row[1]=="2호선":
            total=int(row[4])+int(row[5])
            if total>max_1:
                max_2 = total
                max_s2 = row[3]
            if total<min_1:
                min_2 = total
                min_s2 = row[3]

        elif row[1]=="3호선":
            total=int(row[4])+int(row[5])
            if total>max_3:
                max_3 = total
                max_s3 = row[3]
            if total<min_1:
                min_3 = total
                min_s3 = row[3]

        elif row[1]=="4호선":
            total=int(row[4])+int(row[5])
            if total>max_4:
                max_4 = total
                max_s4 = row[3]
            if total<min_1:
                min_4 = total
                min_s4 = row[3]

        else:
            continue
        
    print("*** Subway Report for Seoul on March 2023 ***")
    print("Line 1:")
    print("Busiest Station:",max_s1,"(",max_1,")")
    print("Least Used Station:",min_s1,"(",min_1,")")
    print("Line 2:")
    print("Busiest Station:",max_s2,"(",max_2,")")
    print("Least Used Station:",min_s2,"(",min_2,")")
    print("Line 3:")
    print("Busiest Station:",max_s3,"(",max_3,")")
    print("Least Used Station:",min_s3,"(",min_3,")")
    print("Line 4:")
    print("Busiest Station:",max_s4,"(",max_4,")")
    print("Least Used Station:",min_s4,"(",min_4,")")
    f.close()

if __name__ == '__main__':
    main()


