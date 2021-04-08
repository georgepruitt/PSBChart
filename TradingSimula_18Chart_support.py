#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 19, 2021 09:21:57 PM EST  platform: Windows NT
import turtle
from turtle import TurtleScreen, RawTurtle, TK
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os.path
import datetime
import csv
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def parseDate(dateString):
    whereIsAslash = dateString.find('/')
    if whereIsAslash != -1:
        firstSlashLoc = whereIsAslash
        x = dateString[0:whereIsAslash]
        tempStr = dateString[whereIsAslash+1:len(dateString)]
        whereIsAslash = tempStr.find('/')
        y = tempStr[0:whereIsAslash]
        z = tempStr[whereIsAslash+1:len(tempStr)]
        if firstSlashLoc < 4:
            tempDate = int(z)*10000 + int(x)*100 + int(y)
        else:
            tempStr = dateString.replace('/','')
            tempDate = int(tempStr)
        return(tempDate)
    whereIsAdash = dateString.find('-')
    if whereIsAdash != -1:
        firstDashLoc = whereIsAdash
        x = dateString[0:whereIsAslash]
        tempStr = dateString[whereIsAslash+1:len(dateString)]
        whereIsAslash = tempStr.find('/')
        y = tempStr[0:whereIsAslash]
        z = tempStr[whereIsAslash+1:len(tempStr)]
        if firstSlashLoc < 4:
            tempDate = int(z)*10000 + int(x)*100 + int(y)
        else:
            tempStr = dateString.replace('-','')
            tempDate = int(tempStr)
        return(tempDate)
    return(int(dateString))

class ManageTrades(object):
    def __init__(self):
        self.load = True
        self.draw = False
    def setLoadDraw(self,load,draw):
        self.load = load
        self.draw = draw

tradeInfo = ManageTrades()
globalIndicList = list()
numBarsPlot = 0
d = list()
dt = list()
o = list()
h = list()
l = list()
c = list()
v = list()
oi = list()
bolBandList = list()
movAvgList = list()
donchChanList = list()
tradeDate = list()
tradeSymbol = list()
tradeVal1 = list()
tradeType = list()
tradeSize = list()
tradeNtryOrXit = list()
tradePrice = list()
highestHigh = 0
lowestLow = 99999999

commName = list()
colorList = list()
indicList = list([])
#root.withdraw()
##s = tk.ScrollBar(root)
'''root = tk.Tk()
#root.call('wm', 'attributes', '.', '-topmost', '1')
T = tk.Text(root,height=10,width=70)
T.pack(side=tk.RIGHT, fill = tk.Y)
##s.pack(side=tk.RIGHT, fill = tk.Y)'''
#T.attributes('-topmost', 'true')

def setIndicList(myIndicList):
    global globalIndicList
    globalIndicList = myIndicList

def setColors(colorList,colorStr):
    for j in range(0,len(colorStr)):
        if colorStr[j] in "rR": colorList[j] = "Red"
        if colorStr[j] in "gG": colorList[j] ="Green"
        if colorStr[j] in "bB": colorList[j] = "Blue"
        if colorStr[j] in "yY": colorList[j] = "Yellow"
        if colorStr[j] in "pP": colorList[j] = "Purple"
        if colorStr[j] in "oO": colorList[j] = "Orange"
        if colorStr[j] in "cC": colorList[j] = "Cyan"

    return colorList

def plotIndicVals(myLilTrtl,whichIndic,sameScale,indicValues,colors):
    numPlots = 0
    myPlotColors = list()
    n = -15
    if whichIndic == "movAvg":
        numPlots = 3
        for j in range(0,numPlots):
            myPlotColors.append("Green")
        myPlotColors = setColors(myPlotColors,colors)

    if whichIndic == "bollingerBand":
        numPlots = 3
        for j in range(0,numPlots):
            myPlotColors.append("Green")
        myPlotColors = setColors(myPlotColors,colors)

    if whichIndic == "donchianChan":
        numPlots = 4
        for j in range(0,numPlots):
            myPlotColors.append("Green")
        myPlotColors = setColors(myPlotColors,colors)


    for j in range(0,numPlots):
        n = -15
        distBetweenPlots = 14
        for i in range(0,len(indicValues)):
            n = n + 1
            myLilTrtl.penup()
            myLilTrtl.color(myPlotColors[j])
            if j==0:
                if i == 0 : myLilTrtl.goto(n*distBetweenPlots,indicValues[i][0])
                myLilTrtl.pendown()
                myLilTrtl.goto(n*distBetweenPlots,indicValues[i][0])
            if j ==1:
                if i == 0 : myLilTrtl.goto(n*distBetweenPlots,indicValues[i][1])
                myLilTrtl.pendown()
                myLilTrtl.goto(n*distBetweenPlots,indicValues[i][1])
            if j ==2:
                if i == 0 : myLilTrtl.goto(n*distBetweenPlots,indicValues[i][2])
                myLilTrtl.pendown()
                myLilTrtl.goto(n*distBetweenPlots,indicValues[i][2])
            if j ==3:
                if i == 0 : myLilTrtl.goto(n*distBetweenPlots,indicValues[i][3])
                myLilTrtl.pendown()
                myLilTrtl.goto(n*distBetweenPlots,indicValues[i][3])

##
    myLilTrtl.penup()

def manageTrades(trades,indicatorList):
    global tradesFileName
    if trades.load:
        cnt = tradeCnt = 0
        file = askopenfilename(filetypes=(('TXT files','*.txt'),),
        title='Select Graph File to Plot!')
        head,tail = os.path.split(file)
        tradesFileName = tail
        if 'Graph' in file:
            with open(file) as f:
                f_csv = csv.reader(f)
                numDecs = 0
                for row in f_csv:
#                    if row[1] == trades.symbol:
                    numCols = len(row)
                    cnt += 1
                    tradeDate.append(int(row[0]))
    #                dt.append(datetime.datetime.strptime(row[0],'%Y%m%d'))
                    tSymbol =row[1]
                    tradeSymbol.append(row[1])
                    tradeVal1.append(int(row[2]))
                    tradeType.append(row[3])
                    tSize = int(row[4])
                    tradeSize.append(int(row[4]))
                    tPrice = float(row[5])
                    tradePrice.append(float(row[5]))
#                        print("Trades ",tradeDate[-1]," ",tradePrice[-1])
                    tradeCnt = cnt
    if tradeCnt > 0:
        tradeDate.append(d[-1])
        tradeSymbol.append(tSymbol)
        tradeVal1.append(1)
        tradePrice.append(c[-1])
        trades.setLoadDraw(False,True)
        w.Button5.configure(state = "disable")
    loadAndDraw(False,True,0,indicatorList,trades)

def loadAndDraw(load,draw,move,indicatorList,trades):
    global numBarsPlot,T
    def get_mouse_click_coor(x, y):
        print(x, y)
        barNumber = round((x+206)/14)
        barNumber = max(1,barNumber)
        print(barNumber, (x+ 206)/14)
##        print("Bar Number: ",barNumber," ",d[startPt+barNumber-1]," ",o[startPt+barNumber-1]," ",highestHigh)
        # tkMessageBox("Information",str(barNumber)
       # # trtl.write('Vivax Solutions', font=("Arial", 20, "bold")) # chosing the font
##        trtl.goto(10,highestHigh-.05*(highestHigh - lowestLow))
##        trtl.pendown()
        indexVal =startPt+barNumber-1
        if indexVal < len(d):
            outPutStr = str(d[indexVal]) + " " +str(o[indexVal])+ " " +str(h[indexVal])+ " " +str(l[indexVal])+ " " + str(c[indexVal]) # chosing the font
            outPutStr1 = ""
            outPutStr2 = ""
            if indicatorList is not None:
                if "bollingerBand" in indicatorList:
                    indicIndex = indicatorList.index("bollingerBand")
                    if barNumber <= len(bolBandList):
                        outPutStr1 = "Boll.Bands "+ "Bar# "+str(barNumber) +" UpBand: " + str(round(bolBandList[barNumber-1][1],4)) +" MidBand: "+ str(round(bolBandList[barNumber-1][0],2)) +" DnBand: "+ str(round(bolBandList[barNumber-1][2],2))
                if "movAvg" in indicatorList:
                    indicIndex = indicatorList.index("movAvg")
                    if barNumber <= len(movAvgList):
                        outPutStr2 = "MovAvg(2) "+ "Bar# "+str(barNumber) +" Avg1: " + str(round(movAvgList[barNumber-1][1],4)) +" Avg2: "+ str(round(movAvgList[barNumber-1][0],2)) +" Avg3: "+ str(round(movAvgList[barNumber-1][2],2))
                if "donchianChan" in indicatorList:
                    indicIndex = indicatorList.index("donchianChan")
                    if barNumber <= len(h):
                        outPutStr2 = "Donch.Chans "+ "Bar# "+str(barNumber) +" HH1 " + str(round(donchChanList[barNumber-1][0],4)) +" HH2: "+ str(round(donchChanList[barNumber-1][1],4)) +" LL1: "+ str(round(donchChanList[barNumber-1][2],4))  +" LL2: "+ str(round(donchChanList[barNumber-1][3],4))
#            root.focus_set()
            T.focus_set()
            T.insert(tk.END,outPutStr+"\n")
            if outPutStr1!="":T.insert(tk.END,outPutStr1+"\n")
            if outPutStr2!="":T.insert(tk.END,outPutStr2+"\n")
    ##        trtl.goto(20,highestHigh-60)
    ##        trtl.write(str(o[50-(50-barNumber)]), font=("Arial", 8, "bold")) # chosing the font
    ##        trtl.goto(20,highestHigh-80)
    ##        trtl.write(str(h[50-(50-barNumber)]), font=("Arial", 8, "bold")) # chosing the font
    ##        trtl.goto(20,highestHigh-100)
    ##        trtl.write(str(l[50-(50-barNumber)]), font=("Arial", 8, "bold")) # chosing the font
    ##        trtl.goto(20,highestHigh-120)
    ##        trtl.write(str(c[50-(50-barNumber)]), font=("Arial", 8, "bold")) # chosing the font

    ##
    ##    #root.withdraw()
    setIndicList(indicatorList)
    if load == True:
        cnt = 0
        file = askopenfilename(filetypes=(('CSV files', '*.csv'),
        ('TXT files', '*.txt')),
        title='Select Markets or Ports. To Test- CSV format only!')
        commName.clear()
        commName.append(file)
        if len(indicatorList) !=0: indicatorList.clear()
        with open(file) as f:
            f_csv = csv.reader(f)
            numDecs = 0
            for row in f_csv:
                numCols = len(row)
                cnt += 1
                d.append(parseDate(row[0]))
#                dt.append(datetime.datetime.strptime(row[0],'%Y%m%d'))
                o.append(float(row[1]))
                h.append(float(row[2]))
                l.append(float(row[3]))
                c.append(float(row[4]))
                if numCols == 6:
                    v.append(float(row[5]))
                if numCols == 7:
                    v.append(float(row[5]))
                    oi.append(float(row[6]))
                oString= str(o[-1])
                if '.' in oString:
                    decLoc = oString.index('.')
                    numDecs = max(numDecs,len(oString) - decLoc - 1)
        xDate = list()
        yVal = list()
        zVal = list()
        numBarsPlot = 98
        w.Button5.configure(state = "normal")
        w.Entry1.delete(0,"end")
        w.Entry1.insert(0,str(d[-numBarsPlot]))
 #       w.Entry2.delete(0,"end")
 #       w.Entry2.insert(0,"90")
        print("D[-90] = ",d[-numBarsPlot])

        w.Scale1.configure(from_= numBarsPlot)
        w.Scale1.configure(to=len(d)-1)
        w.Scale1.set(len(d)-1)

    if draw == True:
        highestHigh = 0
        lowestLow = 99999999
        scaleMult = 1
        if move != 0:
            startDrawDateStr = w.Entry1.get()
            if move == 1:
                startDrawDate = int(startDrawDateStr) - 5
                sDy = startDrawDate % 100
                sYr = int(startDrawDate/10000)
                sMn = int(startDrawDate/100 %100)
                if sMn < 1:
                    sMn = 12
                    sYr = sYr - 1
                if  sDy > 31:
                    if sMn in (1,3,5,7,8,10,12):
                        sDy = 31 + (sDy - 100)
                    else:
                        sDy = 30 + (sDy - 100)
            if move == 2:
                startDrawDate = int(startDrawDateStr) + 5
                sDy = startDrawDate % 100
                sYr = int(startDrawDate/10000)
                sMn = int(startDrawDate/100 %100)
                if  sDy > 31:
                    sMn = sMn + 1
                    if sMn > 12:
                        sYr = sYr + 1
                        sMn = 1
                    if sMn in (1,3,5,7,8,10,12):
                        sDy = sDy - 30
                    else:
                        sDy = sDy - 31
            startDrawDate = sYr * 10000 + sMn *100 + sDy
            startDrawDateStr = str(startDrawDate)
            w.Entry1.delete(0,END)
            w.Entry1.insert(0,startDrawDateStr)
            print("inside bars back: ",startDrawDate)


        startDrawDateStr = w.Entry1.get()
        startDrawDate = int(startDrawDateStr)

        cnt = -1
        for x in range(0,len(d)):
            cnt+=1
            if startDrawDate >= d[x]:
                startPt = x + 1

#        numBarsPlotStr = w.Entry2.get()
#        numBarsPlot = int(numBarsPlotStr)
#        if numBarsPlot > 180: numBarsPlot = 180
#        if numBarsPlot < 45: numBarsPlot = 45

        numBarsPlot = 98

        if startPt + numBarsPlot > len(d): startPt = len(d) - (numBarsPlot + 1)
        print(startPt," ",len(d)," ",numBarsPlot);
        for days in range(startPt,startPt+numBarsPlot):
            if h[days]*scaleMult > highestHigh: highestHigh = h[days]*scaleMult
            if l[days]*scaleMult < lowestLow: lowestLow = l[days]*scaleMult
        print("Date HHLL :", highestHigh," ",lowestLow)
        indicCnt = 0

        canvas1Width = w.Canvas1.winfo_width()
        canvas1Height = w.Canvas1.winfo_height()

        screen = TurtleScreen(w.Canvas1)
        trtl = RawTurtle(screen)
        screen.tracer(False)
        screen.bgcolor('black')
        screen.mode('world')

        clr=['red','green','blue','yellow','purple']
        trtl.pensize(1)
        trtl.penup()
        trtl.color("green")
        trtl.setheading(0)
        trtl.penup()

        hhllDiffScale= (highestHigh - lowestLow) /1.85
        hhllDiff = highestHigh - lowestLow
#        screen.setworldcoordinates(-10,highestHigh-hhllDiffScale,canvas1Width,highestHigh)
        screen.setworldcoordinates(-10,highestHigh-(hhllDiffScale*1.1),canvas1Width/3.5,highestHigh)

        m=-15
        distTweenBars = 14
        if startPt + numBarsPlot >= len(h):
             startPt = len(d) - (numBarsPlot+1)
        for i in range(startPt,startPt+numBarsPlot+1):
            m=m+1
            trtl.penup()
            trtl.color("lime")
            trtl.goto(m*distTweenBars,h[i]*scaleMult)
            trtl.pendown()
            trtl.pensize(1)
            trtl.goto(m*distTweenBars,l[i]*scaleMult)
            trtl.penup()
            trtl.goto(m*distTweenBars,c[i]*scaleMult)
            trtl.pendown()
            trtl.goto(m*distTweenBars+5,c[i]*scaleMult)
            trtl.penup()
            trtl.goto(m*distTweenBars,o[i]*scaleMult)
            trtl.pendown()
            trtl.goto(m*distTweenBars-5,o[i]*scaleMult)
            trtl.penup()
            trtl.goto(distTweenBars,highestHigh)

        if indicatorList is not None and len(indicatorList)!=0:
            movAvgParams = list([])
            bollingerParams = list([])
            donchianParams = list([])
            if "movAvg" in indicatorList:
                movAvgVal = 0
                movAvgList.clear()
                movAvgParamIndexVal = indicatorList.index("movAvg")
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 1])
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 2])
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 3])
                if movAvgParams[0] + movAvgParams[1] + movAvgParams[2] != 0:
                    for i in range(startPt,startPt+numBarsPlot):
                        sum1 = sum2 = sum3 = avg1 = avg2 = avg3=0
                        if movAvgParams[0] != 0:
                            for k in range(i-movAvgParams[0],i):
                                sum1 = sum1 + c[k] * scaleMult
                            avg1 = sum1/movAvgParams[0]
                            highestHigh = max(avg1,highestHigh)
                            lowestLow = min(avg1,lowestLow)
                        if movAvgParams[1] != 0:
                            for k in range(i-movAvgParams[1],i):
                                sum2 = sum2 + c[k] * scaleMult
                            avg2 = sum2/movAvgParams[1]
                            highestHigh = max(avg2,highestHigh)
                            lowestLow = min(avg2,lowestLow)
                        if movAvgParams[2] != 0:
                            for k in range(i-movAvgParams[2],i):
                                sum3 = sum3 + c[k] * scaleMult
                            avg3 = sum3/movAvgParams[2]
                            highestHigh = max(avg3,highestHigh)
                            lowestLow = min(avg3,lowestLow)
                        movAvgList.append([avg1,avg2,avg3])
            if "bollingerBand" in indicatorList:
                bolBandList.clear()
                bollingerParamIndexVal = indicatorList.index("bollingerBand")
                bollingerParams.append(indicatorList[bollingerParamIndexVal + 1])
                bollingerParams.append(indicatorList[bollingerParamIndexVal + 2])
                bollingerParams.append(indicatorList[bollingerParamIndexVal + 3])
                for i in range(startPt,startPt+numBarsPlot):
                    movAvgVal = 0.0
                    dev1Sum = 0.0
                    dev2Sum = 0.0
                    for k in range(i-bollingerParams[0],i):
                        dev1Sum = dev1Sum + c[k]
                        dev2Sum = dev2Sum + c[k]**2
                    if bollingerParams[0] !=0: movAvgVal = dev1Sum/bollingerParams[0]
                    plotVal1 = movAvgVal
                    stdDev = 0.0
                    if bollingerParams[0] * dev2Sum > dev1Sum**2:
                        stdDev = ((bollingerParams[0]*dev2Sum -dev1Sum**2) / \
                        (bollingerParams[0] * (bollingerParams[0] - 1)))**0.5
                    midBand = movAvgVal * scaleMult
                    upBand = (movAvgVal + stdDev * bollingerParams[1])*scaleMult
                    dnBand = (movAvgVal - stdDev * bollingerParams[2])*scaleMult
                    bolBandList.append([movAvgVal,upBand,dnBand])
                    highestHigh = max(upBand,highestHigh)
                    lowestLow = min(dnBand,lowestLow)
            if "donchianChan" in indicatorList:
                donchChanList.clear()
                donchianParamIndexVal = indicatorList.index("donchianChan")
                donchianParams.append(indicatorList[donchianParamIndexVal + 1])
                donchianParams.append(indicatorList[donchianParamIndexVal + 2])
                for i in range(startPt,startPt+numBarsPlot):
                    hh1 = hh2 = 0.0
                    ll1 = ll2 = 999999999
                    for k in range(i-donchianParams[0],i):
                        hh1 = max(hh1,h[k])
                        ll1 = min(ll1,l[k])
                    if donchianParams[0] !=0:
                        plotVal1 = hh1
                        plotVal2 = ll1
                    for k in range(i-donchianParams[1],i):
                        hh2 = max(hh2,h[k])
                        ll2 = min(ll2,l[k])
                    if donchianParams[1] !=0:
                        plotVal3 = hh2
                        plotVal4 = ll2
                    hh1 = hh1 * scaleMult
                    hh2 = hh2 * scaleMult
                    ll1 = ll1 * scaleMult
                    ll2 = ll2 * scaleMult
                    donchChanList.append([hh1,hh2,ll1,ll2])
                    print("Donch Vals : ",hh1," ",hh2," ",ll1," ",ll2," ",)



            print("Inidcator 1 ",highestHigh," ",lowestLow)
            if "movAvg" in indicatorList:
                plotIndicVals(trtl,"movAvg",1,movAvgList,"rgb")
            if "bollingerBand" in indicatorList :
                plotIndicVals(trtl,"bollingerBand",1,bolBandList,"coo")
            if "donchianChan" in indicatorList:
                plotIndicVals(trtl,"donchianChan",1,donchChanList,"gyrb")

            if "RSI" in indicatorList:

                screen2 = TurtleScreen(w.Canvas2)
                trtl2 = RawTurtle(screen2)

                screen2.tracer(False)

                screen2.bgcolor('white')

                screen2.setworldcoordinates(-10,-20,973,200)
                n = 0
                for i in range(startPt,startPt+numBarsPlot):
                    n = n + 1
                    movAvgVal = (c[i] - l[i])/(h[i] - l[i])*100
                    print(movAvgVal)
                    if i == startPt : trtl2.goto(n*10,movAvgVal)
                    trtl2.pendown()
                    trtl2.goto(n*10,movAvgVal)
                trtl2.penup()
        botOfChart = lowestLow
        print("Indicator List: ",indicatorList)
#       print("PlotTrades : ",plotTrades)
        if trades.draw:
            debugTradeDate = tradeDate[0]
            debugDate = d[startPt]
            n = 0
            trtl.penup()
            while debugTradeDate <= debugDate:
                n +=1
                debugTradeDate = tradeDate[n]
            m = -15
            for i in range(startPt,startPt+numBarsPlot):
                m = m + 1
                debugDate = d[i]
                if debugDate == debugTradeDate:
                    tradesTodayCnt = n
                    tradesToday = 0
                    while debugTradeDate == d[i]:
                        tradesToday+=1
                        tradesTodayCnt+=1
                        if tradesTodayCnt > len(tradeDate):
                            debugTradeDate = -1
                            tradesToday -=1
                        else:
                            if tradesTodayCnt == len(tradeDate):
                                debugTradeDate = tradeDate[-1] + 1
                            else:
                                debugTradeDate = tradeDate[tradesTodayCnt]
                    print("Found Trades ",tradesToday," ",debugTradeDate)
                    for k in range(tradesToday):
                        tradeValue = tradePrice[n]
                        nextTradeValue = c[startPt+numBarsPlot-1]
                        if n < len(tradePrice)-1:
                            nextTradeValue = tradePrice[n+1]
                        else:
                            nextTradeValue = c[-1]
                        if tradeType[n] == "buy":
                            trtl.goto(m*distTweenBars-5,tradeValue - hhllDiff *.03)
                            trtl.pensize(2)
                            trtl.pendown()
                            trtl.color("Green")
                            trtl.goto(m*distTweenBars,tradeValue)
                            trtl.goto(m*distTweenBars+5,tradeValue - hhllDiff *.03)
                            trtl.penup()
                            trtl.goto(m*distTweenBars,tradeValue)
                            trtl.pendown()
                            trtl.pencolor("Red")
                            if nextTradeValue > tradeValue: trtl.pencolor("Green")
    #                        trtl.penup()
                        if tradeType[n] == "sell":
                            trtl.goto(m*distTweenBars-5,tradeValue + hhllDiff *.03)
                            trtl.pensize(2)
                            trtl.pendown()
                            trtl.color("Red")
                            trtl.goto(m*distTweenBars,tradeValue)
                            trtl.goto(m*distTweenBars+5,tradeValue + hhllDiff *.03)
                            trtl.penup()
                            trtl.goto(m*distTweenBars,tradeValue)
                            trtl.pendown()
                            trtl.pencolor("Red")
                            if nextTradeValue < tradeValue: trtl.pencolor("Green")
    #                        trtl.penup()

                        if tradeType[n] == "liqLong" or tradeType[n] == "liqShort":
    #                        trtl.penup()
                            trtl.goto(m*distTweenBars-5, tradeValue)
                            trtl.color("Blue")
                            trtl.pensize(3)
                            trtl.pendown()
                            trtl.goto(m*distTweenBars+5, tradeValue)
                            trtl.penup()
                        trtl.pensize(1)
                        print("Found a trade: ",tradeValue," ",nextTradeValue)
                        n+=1
                        if n < len(tradeDate): debugTradeDate = tradeDate[n]
            if i == startPt + numBarsPlot -1 and trtl.isdown():
                trtl.goto(m*distTweenBars,nextTradeValue)
                trtl.penup()



        trtl.color("yellow")
        trtl.goto(-200,botOfChart+(.08*(hhllDiff)))
        trtl.pendown()
        trtl.write(commName[-1], font=("Arial", 9, "normal")) # chosing the font
        trtl.penup()

        trtl.goto(-200,botOfChart)
        trtl.pendown()
        trtl.goto(int(numBarsPlot+1*distTweenBars),botOfChart)


        trtl.penup()
        trtl.goto(-190,botOfChart+.03*(hhllDiff))
        trtl.color("yellow")
        trtl.pendown()
        trtl.write(str(d[startPt]), font=("Arial", 8, "normal")) # chosing the font
        trtl.penup()

        m = -15
        for i in range(startPt,startPt+numBarsPlot+1):
            if i % 10 == 0 :
                trtl.goto(m*distTweenBars,botOfChart+.03*(hhllDiff))
                trtl.pendown()
                trtl.color("yellow")
                trtl.write(str(d[i]), font=("Arial", 8, "normal")) # chosing the font
                trtl.penup()
                m = m + 10

        trtl.penup()
        trtl.goto(int(numBarsPlot*distTweenBars-180),highestHigh)
        trtl.pendown()
        trtl.goto(int(numBarsPlot*distTweenBars-180),botOfChart)
        trtl.penup()

        m = 0
        vertIncrement = hhllDiff/10
        for i in range(0,11):
            trtl.goto(int(numBarsPlot*distTweenBars-(170))+2,highestHigh - m*vertIncrement)
            trtl.pendown()
            trtl.write(str(highestHigh - m * vertIncrement),font=("Arial", 8, "normal"))
            trtl.penup()
            m +=1
        # turtle.done()
        screen.onscreenclick(get_mouse_click_coor)
    ##    turtle.mainloop()
def updateDateInWindow():
    global w,numBarsPlot,globalIndicList,tradeInfo
    scaleVal = w.Scale1.get()
    w.Entry1.delete(0,tk.END)
    w.Entry1.insert(0,str(d[scaleVal-numBarsPlot]))
    loadAndDraw(False,True,0,globalIndicList,tradeInfo)

def init(top, gui, textWindow,*args, **kwargs):
    global w, top_level, root, T
    w = gui
    top_level = top
    root = top
    T = textWindow

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def loadData():
    loadAndDraw(True,True,0,indicList,tradeInfo)

def getTrades():
    manageTrades(tradeInfo,indicList)


def upDateScale(EVENT=None):
    global w
    updateDateInWindow()

#def upDateScale(indicList,tradeInfo):
#    global w
#    updateDateInWindow()


if __name__ == '__main__':
    import TradingSimula_18Chart
    TradingSimula_18Chart.vp_start_gui()
