

##21000348 Andre Seo
##Data From HTML

import urllib
import urllib.request

url = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT007023"


dates = []
min_tp = []
max_tp = []


##Function Defining
def extract_date(line):
    tdate = line[line.find('(')+1:line.find(')')]
    return tdate


def extract_temperature(line):
    if '<li class="nm">' in line:
        skip_len = len('temp">')
        start_idx = line.find('temp">') + skip_len
        end_idx = line.find('</span')
        temp = line[start_idx : end_idx]
        return temp
    return None



def print_weather():
    file = open("weather.html", "r")
    min_flag = True
    for line in file:
        if '<br><span>' in line:
            wdate = extract_date(line)
            dates.append(wdate)
        temp = extract_temperature(line)
        if min_flag == True:
            if temp != None:
                min_tp.append(temp)
                min_flag = False
        else:
            if temp != None:
                max_tp.append(temp)
                min_flag = True
    for i in range( len( dates ) ):
        print('%s :\t%5s ~ %5s' % ( dates[i], min_tp[i+2], max_tp[i+2] ))




##File wearther.html is already created in 2015/11/16
def process_webpage():
    webpage = urllib.request.urlopen(url)
    out = open("weather.html", "w")
    for line in webpage:
        out.write(line.strip().decode()+"\n")
    webpage.close()
    out.close()

        
def main():
    process_webpage()
    print_weather()



print ("loading...\n\n")
main()





