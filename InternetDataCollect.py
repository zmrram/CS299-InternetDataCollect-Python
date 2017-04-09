import urllib.request
import sys


def findHighest(priceList,dateList):
    i = 0
    highestPrice = 0
    date = ""
    for each in priceList:
        if each > highestPrice:
            highestPrice = each
            date = dateList[i]
        i+=1
    return highestPrice,date

def findLowest(priceList,dateList):
    i = 0
    lowestPrice = priceList[0]
    date = dateList[0]
    for each in priceList:
        if each  < lowestPrice:
            lowestPrice = each
            date = dateList[i]
        i+=1
    return lowestPrice,date

def largestVolume(volumeList,dateList):
    highestVolume = 0
    i = 0
    date = ""
    for each in volumeList:
        if each > highestVolume:
            highestVolume = each
            date = dateList[i]
        i+=1
    return highestVolume,date

def readPage(company,urlAddress):   
    page =urllib.request.urlopen(urlAddress)
    pageText = page.readline()
    pageText = page.readline()
    pageText = page.readline()
    pageText = page.readline()
    highestPrice = []
    lowestPrice = []
    volume = []
    date = []
    avgPrice = 0

    for i in range (0,5):
        pageText = page.readline();
        decodedPageText = pageText.decode("utf-8")
        values = decodedPageText.split(",")
        highestPrice.append(float(values[2]))
        lowestPrice.append(float(values[3]))
        date.append(values[0])
        volume.append(int(values[5]))
        avgPrice += float(values[4])

    pricehighest,dateHighest = findHighest(highestPrice,date)
    pricelowest,dateLowest = findLowest(lowestPrice,date)
    highestVolume, dateH = largestVolume(volume,date)
    avgPrice = avgPrice / 5
    print("Organization:", company)
    print("Highest Price:", pricehighest,"on date", dateHighest)
    print("Lowest Price:", pricelowest,"on date", dateLowest)
    print("Highest trading volume is", highestVolume,"share on", dateH)
    print("Avg Closing Price is", avgPrice)
    
def main():
    readPage("TARGET", "http://chart.yahoo.com/table.csv?s=TGT")
    print()
    readPage("MICROSOFT", "http://chart.yahoo.com/table.csv?s=MSFT")
    sys.stdout = open('TestOutput.txt', 'w')
    readPage("TARGET", "http://chart.yahoo.com/table.csv?s=TGT")
    print()
    readPage("MICROSOFT", "http://chart.yahoo.com/table.csv?s=MSFT")
    
if  __name__ =='__main__':
    main()
