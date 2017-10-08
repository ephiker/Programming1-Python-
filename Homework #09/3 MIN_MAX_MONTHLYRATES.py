#21000348 Andre Seo
#Year : Minimum/Maximum Monthly

years = range(1994,2010) #making list of 1994 ~ 2009


#Defining Functions
def read_year(yr):
    fname = "data/%d.txt" %yr #making names of files to open
    f = open(fname, "r")
    data = []
    for line in f: #reformatting the data
        date1, value1 = line.split()#unpacking line by line
        value = float(value1)
        value = int(1.0/value) #exchage to KRW
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) #reformatting
        data.append((date, value)) #appending as tuple type
    f.close()
    return data


def find_minmax(yr):
    minmax = [(9999,0)]*12 #making max/min 12 tuple list
##    print (minmax) #이 함수가 실행될 때마다 12개월짜리 (최소,최대)*12 튜플 리스트 만들어짐
    data = read_year(yr)
    for d, v in data: #d는 날짜19950505
        month = (int(d/100)) % 100 - 1 #8자리날짜를 100으로 나눈 수를 다시 100으로 나눴을 때 나머지 = 월
        minr, maxr = minmax[month] #변수 생성
        if v < minr:
            minr = v
        if v > maxr:
            maxr = v
        minmax[month] = minr, maxr #최대최소 저장
    return minmax
        
def main():
    for yr in years:
        print ("%4d:" %yr, end =" ")
        minmax = find_minmax(yr)
        for mon in range(12):
            print ("%4d/%-4d" % minmax[mon], end =" ")
        print ("\n")


main()


    

