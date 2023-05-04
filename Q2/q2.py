def main():
    import csv
    f=open('q2.csv', encoding='cp949')
    data=csv.reader(f)
    header=next(data)

    max_t = 0
    min_t = 999
    max_day = ''
    min_day = ''

    for row in data:
        if row[2]=='' or row[3]=='' or row[4]=='':
            continue
        else:
            temp_diff = float(row[4])-float(row[3])
            if temp_diff>max_t:
                max_t = temp_diff
                max_day = row[0]
            if temp_diff<min_t:
                min_t = temp_diff
                min_day = row[0]

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperatue Variation:",max_day)
    print("Maximum Temperature Difference:",round(max_t,1),"Celsius")
    print("Day with the Smallest Temperatue Variation:",min_day)
    print("Maximum Temperature Difference:",round(min_t,1),"Celsius")
    f.close()

if __name__ == '__main__':
    main()


