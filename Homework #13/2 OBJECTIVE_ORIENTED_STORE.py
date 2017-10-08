###



###21000348 Andre Seo
###Objective Oriented Store
##
####Creating the file stock.txt
##file = open("./stock.txt", 'w')
##
##stock1 = "apple,900,190\n"
##stock2 = "orange,1300,90\n"
##stock3 = "pineapple,550,13\n"
##stock4 = "carrot,600,60\n"
##stock5 = "cucumber,900,30\n"
##stock6 = "egg plant,1100,20\n"
##stock7 = "zuccini,1300,10\n"
##stock8 = "garlic,300,70"
##
##file.write(stock1)
##file.write(stock2)
##file.write(stock3)
##file.write(stock4)
##file.write(stock5)
##file.write(stock6)
##file.write(stock7)
##file.write(stock8)
##
##file.close()
##
##
##
###Defining Functions
##def load_stock(filename):
##    file = open(filename, 'r')
##    stock_list = []
##    for line in file:
##        line = line.strip()
##        item = line.split(",")
##        item[1] = int(item[1])
##        item[2] = int(item[2])
##        stock_list.append(item)
##    file.close()
##    stock_list.sort()
##    return stock_list
##
##
##def store_stock(stock_list):
##    file = open("./stock.txt", 'w')
##    for line in stock_list:
##        line[1] = str(line[1])
##        line[2] = str(line[2])
##        item = ",".join(line) + "\n"
##        file.write(item)
##    file.close()
##
##
##
##def take_name(stock_list):
##    while True:
##        res = " "
##        name = raw_input("What you want to buy?>>>")
##        for item in stock_list:
##            if item[0] == name:
##                break
##        if item[0] == name:
##            break
##        else:
##            print "Sorry, we do not have a stock for " + name + "."
##            res = raw_input("Do you what to buy other item? (y/n)>>>")
##            if (res == "n"):
##                break
##                
##        
##    if res == " ":
##        return item
##    else:
##        return []
##
##
##
##
##def take_quant(item):
##    while True:
##        res = " "
##        try:
##            qty = int(raw_input("How many? >>>"))
##            if qty > item[2]:
##                print "Sorry, we have only %5d items." % item[2]
##                res = raw_input("Would you buy? (y/n)>>>")
##                if res == "y":
##                    qty = item[2]
##            break
##        except:
##            print "Type in a number. >>>"
##
##    if res == "y" or res == " ":
##        return qty
##    else:
##        return 0        
##
##            
##
##def take_input(stock_list):
##    item = take_name(stock_list)
##    if item != []:
##        quant = take_quant(item)
##    else:
##        quant = 0
##    return item, quant
##
##
##def sell(stock_list, sales_history):
##    item, quant = take_input(stock_list)
##    if item == []:
##        return
##    item[2] -= quant #-1 from number of item
##    amount = item[1]*quant #amount = price*quant
##    print "item =", item[0], ": price =", item[1], ": quantity =", quant, ": amount =",amount
##    sales_history.append((item[0], item[1], quant, amount))
##
##
##def print_stock(stock_list):
##    print "\n", " "*20 + "STOCK REPORT"
##    print "Name\t\tPrice\tQuantity\tAmount"
##    for item in stock_list:
##        print "%-10s\t%5d\t%8d\t%6d" %(item[0], item[1], item[2], item[1]*item[2])
##
##
##def print_sales(sales_history):
##    print " "*20 + "SALES REPORT"
##    print "Name\t\tPrice\tQuantity\tAmount"
##    for item in sales_history:
##        print "%-10s\t%5d\t%8d\t%6d" %(item[0], item[1], item[2], item[3])
##
##
##def show_menu():
##    print "\n", "What would like to do?"
##    print "   S: Sell an item"
##    print "   P: Print stock"
##    print "   R: Report sales"
##    print "   E: Exit"
##    return raw_input("Enter your choice (S, P, R, or E)>>>")
##
##
##def input_error(s):
##    print s + "?" + "I beg your pardon."
##
##
###main
##stock_list = load_stock("./stock.txt")
##
##sales_history = []
##
##while True:
##    s = show_menu()
##    if s == "E":
##        break
##    elif s == "S":
##        sell(stock_list, sales_history)
##    elif s == "P":
##        print_stock(stock_list)
##    elif s == "R":
##        print_sales(sales_history)
##    else:
##        input_error(s)
##
##store_stock(stock_list) #saving history        
