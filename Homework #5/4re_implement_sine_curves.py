#21000348 AndreSeo
#Re-implement sin curves

#This program draws a bar_graph
import math
import time




def plot_graph(no_of_symbols):
    if no_of_symbols < 40:
        if no_of_symbols ==39:
            bar = " " * no_of_symbols + "!!"
        else:
            bar = " " * no_of_symbols + "!!" + " " * (37 - no_of_symbols) + "|"
    elif no_of_symbols == 40:
        bar = "-" * 39 + "!!" + "-" * 40
    else:
        bar = " " * 39 + "|" + " " * (no_of_symbols - 38) + "!!"
    print (bar)
            
def count_no_of_symbols(angle):
    val = math.sin(angle)
    if val < 0:
        no_of_symbols = int(val*40 - 0.5) + 40
    else:
        no_of_symbols = int(val*40 + 0.5) + 40
    return no_of_symbols

def compute_and_plot(angle):
    no_of_symbols = count_no_of_symbols(angle)
    plot_graph(no_of_symbols)


def main():
    for i in range(41):
        angle = (2*math.pi / 40) * i
        compute_and_plot(angle)



main()





