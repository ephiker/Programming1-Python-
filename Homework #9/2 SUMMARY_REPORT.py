#21000348 Andre Seo
#Summary Report

years = range(1994,2010) #making list of 1994 ~ 2009


#Defining Functions
def read_year(yr, data):
    fname = "data/%d.txt" %yr #making names of files to open
    f = open(fname, "r")
    for line in f: #reformatting the data
        date1, value1 = line.split()#unpacking line by line
        value = float(value1)
        value = int(1.0/value) #exchage to KRW
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) #reformatting
        data.append((date, value)) #appending as tuple type
    f.close()
    return data

def create_list_with_files():
    data = []
    for yr in years:
        data = read_year(yr, data)
    return data

def find_min(data):
    vm = 99999 #for first comparison 
    dm = None #date pair
        for d, v in data: #unpacking (date, value)
        if v < vm:
            vm = v #최소값이 계속 갱신
            dm = d #날짜 갱신
    return dm, vm

def find_max(data):
    vm = 0
    dm = None
    for d, v in data:
        if v > vm:
            vm = v
            dm = d
    return dm, vm

def average(data, yr):
    sum = 0
    count = 0
    start = yr * 10000 #only yyyy
    end = (yr+1) * 10000 # yyyy+1
    for d, v in data:
        if start <= d < end: #in a year 
            sum += v #1년간 수치 모두 합
            count += 1 # 1년 날짜 세기
    return sum / count


   



def main():
    data = create_list_with_files()
    print ("Minimum:", find_min(data))
    print ("Maximum:", find_max(data))
    print ("\n")
    for yr in years:
        avg = average(data, yr)
        print (yr, int(avg))


main()
