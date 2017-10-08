##21000348 Andre Seo
##Listing Dicision Nodes(BFAST_MAX)


def display(sequence, weight, flag):
    nlist = [] ##출력할 물건 리스트 저장
    for item in sequence:
        nlist.append(item[0])
    if flag: ##flag True는 fast mode에서 필요, 즉 이미 계산된 적이 있는 데이터
        print (" "*6*indent, nlist, weight, "Already solved")
    else:
        print (" "*6*indent, nlist, weight )


def fast_result(sub_seq, avail, memo): #똑같은데 메모가 따라다님
    nextitem = sub_seq[0] ##서브시퀀스의 첫번째 요소인 첫번째 아이템에 대한 튜플로 시작한다(a,a의밸류,a의무게) 리컬션되면 b,b의 밸류,b의 무게..
    if nextitem[2] <= avail: ##a의 무게가 avail보다 작으면
        tsub_seq1, val1 = bfast_max(sub_seq[1:], avail-nextitem[2], memo) ##첫 번째 경우로 a를 가방에 넣었다고 생각하고 b,c,d에 대한 튜플로 다시 함수를 시작한다
        val1 += nextitem[1] ## a,b,c,d를 다 넣었다면 더해지는 순서는 d + c + b + a.. 재귀되면서 역순으로 더해진다 
        tsub_seq2, val2 = bfast_max(sub_seq[1:], avail, memo) ##두 번째 경우로 a를 걍 버렸다고 생각하고 b,c,d에 대한 튜플로 다시 함수를 시작한다

        if val1>val2: ##val1은 처음에 a를 가지고 다음 b를 가진 녀석, val2는 처음에 a를 가지고 다음 b를 안가진 녀석
            result = tsub_seq1 + (nextitem,), val1 ##리스트 더하기 리스트 하면 리스트의 요소가 추가된다.
        else:
            result = tsub_seq2, val2
    else:
        print (" "*6*(indent+1), "No left node") ##avail이 부족하여 못 담았을 때 프린트
        result = bfast_max(sub_seq[1:], avail, memo)

    return result ##result 값은 담은 물건의 리스트와, 총 밸류에 대한 튜플이다
    

def bfast_max(sub_seq, avail, memo={}): #딕셔너리 추가
    global count, indent, flag
    indent +=1

    #튜플을 키로 사용한 memo 딕셔너리에서 해당 내용이 있는지 검사해서 바로 리턴 가능
    #memo딕셔너리의 키에 대한 밸류는 fast_result의 리턴값, 즉 최적의 리스트와 value 튜플임
##    print (len(sub_seq))
    
    if(len(sub_seq), avail) in memo:
        indent -= 1
        display(sub_seq, avail, flag = True)
        return memo[(len(sub_seq), avail)]
    
    flag = False
    display(sub_seq, avail, flag)

    if sub_seq == [] or avail ==0: ##가방에 자리가 없거나, 남은 물건이 없거나
        result = (),0
        indent -= 1
        return result
        
    count +=1
    result = fast_result(sub_seq, avail, memo) #최적의 조합을 찾아
    memo[(len(sub_seq), avail)] = result #일단 저장해!
    indent -= 1
    return result


##Main Program

names = ["a", "b", "c", "d"]
vals = [6,7,8,9] #물건의 값어치->최대로 해야할 것
weights = [3,3,2,5] #물건의 무게

items = [] ##튜플을 요소로 가지는 아이템 리스트
for i in range(len(names)):
    items.append((names[i], vals[i], weights[i]))

print (items)

count = 0
indent = -1

taken, val = bfast_max(items, 5) ##아이템가방을 넣고 무게 제한은 5임  

print ("\n")

for item in taken:
    print (item)
    
print ("Total values of items taken(MAXIMUM) =", val, "count =", count)



