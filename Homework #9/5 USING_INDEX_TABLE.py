years = range(1994, 2010)

def read_year(yr, data):
    fname = "data/%d.txt" % yr
    f = open(fname, "r")
    for line in f :
        date1, value1 = line.split()
        value = float(value1)
        value = int(1.0/value)
        ys, ms, ds = date1.split("/")
        date = 10000 * int(ys) +100 * int(ms) + int(ds)
        data.append((date,value))
    f.close()
    return data

def find_location(data,year):
    table = create_ind_tb(data)
    location = table[year - 1994]
    return location
    

def create_list_with_files():
    data = []
    for yr in years :
        data = read_year(yr, data)
    return data

def create_ind_tb(data):
    yr = 1994
    inx_tb = [0] * 16
    for i in range(len(data)):
        date, rate = data[i]
        year = date // 10000
        if year!= yr:
            inx_tb[year - 1994] = i
            yr = year
        return inx_tb

def average(data, yr): # the average exchange rates for the years
    sum = 0 # start point
    count = 0 # start point
    start = yr * 10000 
    end = (yr +1) * 10000
    for d,v in data:
        if start < d < end:
            sum += v
            count+= 1
    return sum / count

def find_min(data,Input_yr):
    vm = 99999
    dm = None
    start = find_location[Input_yr]
    end = find_location[Input_yr +1]
    for d,v in data[start:end]:
        if v < vm:
            vm = v
            dm = d
    return dm, vm

def find_max(data,Input_yr):
    vm = 0
    dm = None
    start = find_location[Input_yr]
    end = find_location[Input_yr +1]
    for d,v in data[start:end]:
        if v > vm:
            vm = v
            dm = d
    return dm, vm


def main():
    while True:
        
        data = create_list_with_files()

        Input_yr = int(input( "Input Year(1994~2010) :"))
        print("\n")
        if Input_yr == "Q":
            break
        
        print("Year:", Input_yr)
        print("Average Rate : ", average(data,Input_yr))
        print("Maximum Rate : ", find_max(data,Input_yr))
        print("Minimun Rate : ", find_min(data,Input_yr))
        
   
main()





###21000348 Andre Seo
###Using Index Table
##
##
##years = range(1994,2010) #making list of 1994 ~ 2009
##
##
###Defining Functions
##def read_year(yr, data):
##    fname = "data/%d.txt" %yr #making names of files to open
##    f = open(fname, "r")
##    for line in f: #reformatting the data
##        date1, value1 = line.split()#unpacking line by line
##        value = float(value1)
##        value = int(1.0/value) #exchage to KRW
##        ys, ms, ds = date1.split("/")
##        date = 10000*int(ys) + 100*int(ms) + int(ds) #reformatting
##        data.append((date, value)) #appending as tuple type
##    f.close()
##    return data
##        
##def create_list_with_files():
##    data = []
##    for yr in years:
##        data = read_year(yr, data)
##    return data
##
##def create_ind_tb(data):
##    inx_tb = [0]*17 #리스트를 모두 0으로 초기화
##    inx_tb[16] = 5844 #2009년까지 처리하기위해 리스트 길이를 17로 만들고 5844대입
##
##    yr = 1994 #기준년도를 1994년으로 두고 출발
##    for i in range(len(data)): ##5844번 반복
##        date, rate = data[i] ##5844개의 튜플 모두 검색
##        year = int(date/10000) #연도 4자리만 가져옴
##        if year != yr: #돌다가 처음으로 1994년이 아닌 1995년 1월 1일이 나오면 
##            inx_tb[year-1994] = i #그 인덱스(순서)를 리스트에 저장 [0]에는 0, [1]에는 365
##            yr = year #if문에서 1년씩 짜르기 위해 기준년도를 업데이트 해줌
##    return inx_tb
##
##
####아규먼트로 전달받은 연도의 정보가 시작하는 로케이션을 리턴하는 함수
##def find_location(data, yr): ##몇년도의 데이터는 몇 번째인덱스부터 시작하는가?
##    table = create_ind_tb(data)
##    location = table[yr-1994]
##    return location
##
##
##def average(data, yr):
##    sum = 0
##    count = 0
##    start = yr * 10000
##    end = (yr+1) * 10000
##    for d, v in data:
##        if start <= d < end:
##            sum += v
##            count += 1
##    return sum / count
##   
##def find_max(data, yr):
##    vm = 0
##    dm = None
##    start = find_location(data, yr)##해당연도가 시작하는 로케이션
##    end = find_location(data, yr+1)##해당연도 다음해가 시작하는 로케이션
####    if yr == 2009:
####        end = 5843
##    ##FOR문을 DATA LIST 전체 범위로 수행하는 것이 아니라
##    ##FIND_LOCATION함수를 이용하여 해당하는 연도의 범위에 한정하여 수행한다
##    for d, v in (data[start:end]): 
##        if v > vm:
##            vm = v
##            dm = d
##    print (vm, end =" ")
##    return dm, vm
##
##def find_min(data, yr):
##    vm = 99999
##    dm = None
##    start = find_location(data, yr) 
##    end = find_location(data, yr+1)
####    if yr == 2009:
####        end = 5843
##    for d, v in (data[start:end]):
##        if v < vm:
##            vm = v
##            dm = d
##    print (vm, end=" ")
##    return dm, vm
##
##def main():
##
##    while True:        
##        data = create_list_with_files()
##        givenyear = input("Input Year(1994~2009) : ")##정보를 얻으려는 연도를 입력받는다
##
##        if givenyear == 'Q':
##            break
##        
##        givenyear = int(givenyear)##RAW_INPUT으로 받은 숫자는 STR이므로 INT로 형변환
##        
##
##        print ("\n\n")
##        print ("Year : ", givenyear)
##        print ("Start Location : ", find_location(data, givenyear), "of", (len(data)-1))
##        print ("Average Rate : ", average(data, givenyear))
##        print ("Maximum Rate : ", find_max(data, givenyear))
##        print ("Minimum Rate : ", find_min(data, givenyear))
##        print ("\n\n")
##        print ("(Input 'Q' : Quit)")
##        
##main()
##print ("Goodbye")
##
##
