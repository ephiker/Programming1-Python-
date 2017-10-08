##21000348 Andre Seo
##Listing Dicision Nodes(BMAX_VAL)


def display(sequence, weight, flag = False):
    ##bmax_val 함수가 시행될 때마다 반복되어 현재 가방 상태를 알 수 있
    nlist = []
    for item in sequence:
        nlist.append(item[0]) ##범위 안의 아이템의 이름만 가져와서 리스트로 만들기

    if flag: ##flag True는 fast mode에서 필요
        print ((" "*6)*indent, nlist, weight, "Already solved")
    else:
        print ((" "*6)*indent, nlist, weight ) #인덴트*빈칸으로 레벨 구분 #웨이트는 현재 남은 무게
        


def comp_result(sub_seq, avail): #BMAX가 선언 될 때마다 선언..
    nextitem = sub_seq[0] ##남아있는 리스트의 첫 튜플을 넥스트 아이템으로 봄
##    print (nextitem) #(이름, 가치, 무게)
    
    if nextitem[2] <= avail: ##물건의 의 무게가 현재 avail보다 작으면(담을 수 있으면)
##        재귀적으로 모든 경우의 수가 실행된다

        #분기1 : 
        tsub_seq1, val1 = bmax_val(sub_seq[1:], avail-nextitem[2]) ##첫 번째 경우로 a를 가방에 넣었다고 생각하고 b,c,d에 대한 튜플로 다시 함수를 시작한다ㅔ
        val1 += nextitem[1] ## a를 담았으니까 총 가치를 계산하는 var1에 a의 가치를 추가해준다 [1]인 이유는nexttime이 계속 바뀌지만 value를 갖는 인덱스틑 동일
                            ##a,b,c,d를 다 넣었다면 더해지는 순서는 d + c + b + a.. 재귀되면서 역순으로 더해진다
        
        #분기2
        tsub_seq2, val2 = bmax_val(sub_seq[1:], avail) ##두 번째 경우로 a를 걍 버렸다고 생각하고 b,c,d에 대한 튜플로 다시 함수를 시작한다
##        val2에는 nextitem을 담지 않았으므로 nextitem[1]을 더해 줄 필요 없음
        

        ##위의 두 경우에 대해서 어떤 경우의 value가 더 큰지 비교해서 큰 것을 result로 return...
        if val1>val2: ##val1은 처음에 a를 가지고 다음 b를 가진 녀석, val2는 처음에 a를 안가지고 다음 b를 가진 녀석
            #tsub_seq1는 a의 무게를 제외한 무게에서 만든 최대 가치 리스트 + a가 있는 경우이므로 a를 더해줌
            result = tsub_seq1 + (nextitem,), val1 ##리스트 더하기 리스트 하면 리스트의 요소가 추가된다. 리턴값은 리스트와 value
##            print(result)
        else:
            #tsub_seq2는 a의 무게를 제외하지 않은 무게에서 만든 최대 가치 리스트 + a가 없는 경우이므로 a를 더하지 않고 그 리스트 리턴
            result = tsub_seq2, val2 #리턴값은 리스트와 value
##            print(result)
    else:
        print (" "*6*(indent+1), "No left node") ##next 아이템보다 avail이 부족하여 못 담았을 때 프린트, a의 무게가 5보다 높았으면 바로 출력
        result = bmax_val(sub_seq[1:], avail)

    return result ##result 값은 담은 물건의 리스트와, 총 밸류에 대한 튜플이다


def bmax_val(sub_seq, avail):
    global count, indent ##카운트와 인덴트를 글로벌로 불러옴
    indent+=1 ##한 번의 시행이기 때문에 함수 시작하자 마자 인덴트 넣어주어 구분
                ##bmax_val 함수가 시행될 때마다 반복되어 더 들여쓰기가 깊게 됨을 알 수 있음
    
    display(sub_seq, avail) #현재 돗자리 상황을 그대로 디스플레이

    if sub_seq == [] or avail == 0: ##더 가져올 남은 물건이 없거나, 현재 가방에 자리가 없는 경우
        result = (), 0 ##이번 실행의 result는 (), 0임
        indent -= 1 #후퇴하여 한 단계 위로 올라감
        return result

    count +=1 #재귀적으로 몇 번이나 불러와야 하는지(몇 번 넣었다 뺐다 해봐야하는지) count
    result = comp_result(sub_seq, avail) #sub_seq라는 리스트와 avail을 제시했을 때, 최고의 MAX_VALUE 조합은? 리스트와 가치를 리턴

    indent -= 1 ##함수가 끝나기 전에 제자리로 돌아옴
    return result
    

##Main Program

names = ["a", "b", "c", "d"]
vals = [6,7,8,9] #물건의 값어치->최대로 해야할 것
weights = [3,3,2,5]#물건의 무게


items = [] ##튜플을 요소로 가지는 아이템 리스트 만들기
for i in range(len(names)):
    items.append((names[i], vals[i], weights[i]))
##print(items)


#목표는 이 아이템 중 특정 무게 제한에서 가장 많은 가치를 넣는 법은?
    
count = 0
indent = -1

taken, val = bmax_val(items, 5)##이 아이템중에서 5의 제한을 걸었을 때 최적의 MAX_VALUE를 찾아와


print ("\n")
print ("result")
for item in taken:
    print (item)
print ("Total values of items taken(MAXIMUM VALUE) =", val, "count =", count)






