# Enter your code here. Read input from STDIN. Print output to STDOU
import re
def convert(day,month,year):
    date=year+month+day
    print int(date)

def getMonDatl(text,year):
    month=["January","February","March","April","May","June","July","August","September","October","November","December",\
       "JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER",\
        "Jan.","Feb.","Mar.","Apr.","May","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec.",\
        "JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",\
           "01","02","03","04","05","06","07","08","09","10","11","12",\
      ]
    i=0
    mon=""
    for m in month:
        if m in text:
            flag=1
            print text,m
            mon=str((i%12)+1).zfill(2)
            break
        i+=1
    print mon

text=""
while True:
    try:
        line=raw_input()
    except:
        break
    text=text+" "+line
lInd=[m.start() for m in re.finditer('[0-9]{4}',text)]
for ind in lInd:
    print text[ind-15:ind+15]
    year=text[ind:ind+4]
    getMonDat(text[ind-15:ind],year)
    getMonDat(text[ind+4:ind+15],year)
