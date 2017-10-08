#21000348 Andre Seo
#Global Coordinate Data

i, j = 0, 0
print (i)

#Function Defining
def binary_searching(data, code, low, high):
    #바이너리 서치에서 리턴된 값은 flag로 들어가는데 있다, 없다 두 가지고
    if low == high: ##data가 1개인 경우
##        return data[low][0] == code
        return data[low][1]

    mid = int((low+high)/2)

    if data[mid][0] == code: ##미드 인덱스에서 찾은 경우
        return data[mid][1]
    elif data[mid][0] < code: ##찾는 국가가 미드보다 큰 쪽에  경우
        return binary_searching(data, code, mid+1, high) ##범위를 오른쪽으로 하여 다시 검사
    else:
        if low != mid:
            return binary_searching(data, code, low, mid-1)
        else:
            return False
    
        


def merge(left, right):
    result = []
    i= 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:#left와 right 첫 번째 요소의 비교
            result.append(left[i]) #작은 왼쪽을 넣음
            i += 1 #왼쪽 인덱스 하나 업
        else:
            result.append(right[j])
            j += 1

    ##무조건 한쪽이 일찍 끝나게 된다

    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result
        

def merge_sorting(data):
    if len(data)<2:
        return data[:]

    mid = int(len(data)/2)
    left = merge_sorting(data[:mid])
    right = merge_sorting(data[mid:])
    return merge(left, right)



    
def creating_list():
    f = open("average-latitude-longitude-countries.csv", "r")
    tuple_list = []
    count = 0;
    
    for line in f:
        if (count == 0):
            count += 1
            
        ##sepatating data element
        else:
            line = line.strip("\n")
            elements = line.split(",") 
            code = elements[0].strip('"') 
            elements[1] = elements[1].strip('"')
            
##            if not len(elements) == 4:
##                print(elements)
            
            if len(elements) == 4: ##예외 걸러내기
                name = elements[1]
                lati = float(elements[2])
                longi = float(elements[3])
                elem_tuple = (code, name, lati, longi)
                tuple_list.append(elem_tuple)##appending

            else: ##이름이 추출되지 않는 9개의 항목 걸러내어 처리
                elements[2] = elements[2].strip('"')
                name = elements[2] + elements[1]
                lati = float(elements[3])
                longi = float(elements[4])
                elem_tuple = (code, name, lati, longi)
                tuple_list.append(elem_tuple)##appending

    return tuple_list



#main


##1-1 Creating and Sorting and Printing List
print ("\n\n\n1-1 Creating and Sorting and Printing List")

data = creating_list()
merge_sorting(data) ##바이너리 서치를 하려면 순서대로 소팅부터 해야함

##print country chart
for i in range(len(data)):
    print ("Code =", data[i][0], "/ Name =", data[i][1], "/ Latitude =", data[i][2], "/ Longitude =", data[i][3])



##1-2 Listing Countries in South of Equator
print ("\n\n\n1-2 Listing Countries in South of Equator")
for i in range(len(data)):
    if (data[i][2] < 0):##if latitude < 0
        print (data[i][1])##print country name
print ("\n\n")

    

##1-3 Input Code : Output Name  
print ("\n\n\n1-3 Input Code : Output Name")
while (1):
    input_code = input("Input Code : ")
    low = 0 ##시작 인덱스
    high = len(data)-1 ##끝 인덱스
    ##data list is already sorted


    name = binary_searching(data, input_code, low, high)
    print ("Country name is", name)





##딕셔너리로 바꿀 경우 data대신 country라는 딕셔너리를 사용하고,
##키 값으로 code or name을 사용한다
##county[name] = [lati, longi]
##county[code] = [name, lati, longi]

