# Enter your code here. Read input from STDIN. Print output to STDOU
import re
month=["January","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
def convert(day,month,year):
    date=year+month+day
    print int(date)

def getMonDat(text,year):

text=""
while True:
    try:
        line=raw_input()
    except:
        break
    text=text+" "+line
lInd=[m.start() for m in re.finditer('[0-9]{4}',text)]
for ind in lInd:
    year=text[ind:ind+4]
    getMonDat(text[ind-15:ind],year)
    getMonDat(text[ind+4:ind+15],year)
