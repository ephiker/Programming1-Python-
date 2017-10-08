#21000348 Andre Seo
#Using a Dictionary Store


######Creating the file stock.txt
####file = open("./stock.txt", 'w')
####
####stock1 = "apple,900,190\n"
####stock2 = "orange,1300,90\n"
####stock3 = "pineapple,550,13\n"
####stock4 = "carrot,600,60\n"
####stock5 = "cucumber,900,30\n"
####stock6 = "egg plant,1100,20\n"
####stock7 = "zuccini,1300,10\n"
####stock8 = "garlic,300,70"
####
####file.write(stock1)
####file.write(stock2)
####file.write(stock3)
####file.write(stock4)
####file.write(stock5)
####file.write(stock6)
####file.write(stock7)
####file.write(stock8)
####
####file.close()


##Defining Functions
def load_stock(filename):
    file = open(filename, 'r')
    stock_dic = {}
    for line in file:
        line = line.strip()
        item = line.split(",")
        stock_dic[item[0]] = [item[0], int(item[1]), int(item[2])]
        print(stock_dic[item[0]])
        #dic[key] = value
        #dic[name] = [name, 가격, 수량]
    file.close()
    return stock_dic



def store_stock(stock_dic):
    file = open("./stock.txt", 'w')
    for line in stock_dic:
        line[1] = str(line[1])
        line[2] = str(line[2])
        item = ",".join(line) + "\n"
        file.write(item)
    file.close()




def take_name(stock_dic):
    while True:
        res = " "
        name = input("What you want to buy?>>>")
        for item in stock_dic:
            if stock_dic[item][0] == name:
                break
        if stock_dic[item][0] == name:
            break
        else:
            print ("Sorry, we do not have a stock for " + name + ".")
            res = input("Do you what to buy other item? (y/n)>>>")
            if (res == "n"):
                break
        
    if res == " ":
        return item
    else:
        return []

def take_quant(item):
    while True:
        res = " "
        try:
            qty = int(input("How many? >>>"))
            if qty > stock_dic[item][2]:
                print ("Sorry, we have only %5d items." % stock_dic[item][2])
                res = input("Would you buy? (y/n)>>>")
                if res == "y":
                    qty = stock_dic[item][2]
            break
        except:
            print ("Type in a number. >>>")

    if res == "y" or res == " ":
        return qty
    else:
        return 0        

def take_input(stock_dic):
    item = take_name(stock_dic)
    if item != []:
        quant = take_quant(item)
    else:
        quant = 0
    return item, quant


def sell(stock_dic, sales_history):
    item, quant = take_input(stock_dic)
    if item == []:
        return
    stock_dic[item][2] -= quant #-1 from number of item
    amount = stock_dic[item][1]*quant #amount = price*quant
    print ("item =", stock_dic[item][0], ": price =", stock_dic[item][1], ": quantity =", quant, ": amount =",amount)
    sales_history.append((stock_dic[item][0], stock_dic[item][1], quant, amount))
    print(sales_history)


def print_stock(stock_dic):
    print ("\n", " "*20 + "STOCK REPORT")
    print ("Name\t\tPrice\tQuantity\tAmount")
    for item in stock_dic:
        print ("%-10s\t%5d\t%8d\t%6d" %(stock_dic[item][0], stock_dic[item][1], stock_dic[item][2], stock_dic[item][1]*stock_dic[item][2]))


def print_sales(sales_history):
    print (" "*20 + "SALES REPORT")
    print ("Name\t\tPrice\tQuantity\tAmount")
    for item in sales_history:
        print ("%-10s\t%5d\t%8d\t%6d" %(stock_dic[item[0]][0], stock_dic[item[0]][1], stock_dic[item[0]][2], stock_dic[item[0]][1]*stock_dic[item[0]][2]))


def show_menu():
    print ("\n", "What would like to do?")
    print ("   S: Sell an item")
    print ("   P: Print stock")
    print ("   R: Report sales")
    print ("   E: Exit")
    return input("Enter your choice (S, P, R, or E)>>>")


def input_error(s):
    print (s + "?" + "I beg your pardon.")


#Main
stock_dic = load_stock("./stock.txt")
print (stock_dic)

sales_history = []

while True:
    s = show_menu()
    if s == "E":
        break
    elif s == "S":
        sell(stock_dic, sales_history)
    elif s == "P":
        print_stock(stock_dic)
    elif s == "R":
        print_sales(sales_history)
    else:
        input_error(s)

store_stock(stock_dic) #saving history        

