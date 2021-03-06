#! /usr/bin/env python
#
# Support module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Jan 12, 2018 04:09:34 PM

import turtle
from turtle import TurtleScreen, RawTurtle, TK
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os.path
import datetime
import csv
import sys
from PSBChart import ManageTrades

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

d = list()
dt = list()
o = list()
h = list()
l = list()
c = list()
v = list()
oi = list()
tradeDate = list()
tradeVal1 = list()
tradeType = list()
tradeSize = list()
tradeNtryOrXit = list()
tradePrice = list()
highestHigh = 0
lowestLow = 99999999
root = tk.Tk()
#root.withdraw()
##s = tk.ScrollBar(root)
T = tk.Text(root,height=10,width=50)

##s.pack(side=tk.RIGHT, fill = tk.Y)
T.pack(side=tk.RIGHT, fill = tk.Y)
##s.config(command=T.yview)
##T.config(yscrollcommand.set)



def manageTrades(trades,indicatorList):
    if trades.load:
        cnt = 0
        file = askopenfilename(filetypes=(('CSV files', '*.csv'),
        ('TXT files', '*.txt'),('POR files', '*.por')),
        title='Select Markets or Ports. To Test- CSV format only!')
        with open(file) as f:
            f_csv = csv.reader(f)
            numDecs = 0
            for row in f_csv:
                numCols = len(row)
                cnt += 1
                tradeDate.append(int(row[0]))
#                dt.append(datetime.datetime.strptime(row[0],'%Y%m%d'))
                tradeVal1.append(int(row[1]))
                tradeType.append(row[2])
                tradeSize.append(int(row[3]))
                tradePrice.append(float(row[4]))
                print("Trades ",tradeDate[-1]," ",tradePrice[-1])
            tradeCnt = cnt
        trades.setLoadDraw(False,True)
    w.Button5.configure(state = "disable")    
    loadAndDraw(False,True,indicatorList,trades)


def loadAndDraw(load,draw,indicatorList,trades):


    def get_mouse_click_coor(x, y):
        print(x, y)
        barNumber = round(x/10)
        barNumber = max(1,barNumber)
        print("Bar Number: ",barNumber," ",d[startPt+barNumber-1]," ",o[startPt+barNumber-1]," ",highestHigh)
        # tkMessageBox("Information",str(barNumber)
       # # trtl.write('Vivax Solutions', font=("Arial", 20, "bold")) # chosing the font
##        trtl.goto(10,highestHigh-.05*(highestHigh - lowestLow))
##        trtl.pendown()
        indexVal =startPt+barNumber-1
        outPutStr = str(d[indexVal]) + " " +str(o[indexVal])+ " " +str(h[indexVal])+ " " +str(l[indexVal])+ " " + str(c[indexVal]) # chosing the font
        root.focus_set()
        T.focus_set(  )
        T.insert(tk.END,outPutStr+"\n")
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


    if load == True:
        cnt = 0
        file = askopenfilename(filetypes=(('CSV files', '*.csv'),
        ('TXT files', '*.txt'),('POR files', '*.por')),
        title='Select Markets or Ports. To Test- CSV format only!')
        with open(file) as f:
            f_csv = csv.reader(f)
            numDecs = 0
            for row in f_csv:
                numCols = len(row)
                cnt += 1
                d.append(int(row[0]))
                dt.append(datetime.datetime.strptime(row[0],'%Y%m%d'))
                o.append(float(row[1]))
                h.append(float(row[2]))
                l.append(float(row[3]))
                c.append(float(row[4]))
                v.append(float(row[5]))
                oi.append(float(row[6]))
                oString= str(o[-1])
                if '.' in oString:
                    decLoc = oString.index('.')
                    numDecs = max(numDecs,len(oString) - decLoc - 1)
        xDate = list()
        yVal = list()
        zVal = list()
        w.Button5.configure(state = "normal")
        w.Entry1.insert(0,str(d[-1]))

    if draw == True:
        startDrawDateStr = w.Entry1.get()
        startDrawDate = int(startDrawDateStr)
        cnt = -1
        for x in range(0,len(d)):
            cnt+=1
            if startDrawDate >= d[x]: startPt = x
        numBarsPlot = 60
        if startPt + numBarsPlot > len(d): startPt = len(d) - (numBarsPlot + 1)
        print(startPt," ",len(d)," ",numBarsPlot);

        indicCnt = 0
        screen = TurtleScreen(w.Canvas1)


        trtl = RawTurtle(screen)

        screen.tracer(False)

        screen.bgcolor('white')
        clr=['red','green','blue','yellow','purple']
        trtl.pensize(6)
        trtl.penup()
        trtl.color("black")
        highestHigh = 0
        lowestLow = 99999999
#        scaleMult = 10**numDecs
        scaleMult = 1
        for days in range(startPt,startPt+numBarsPlot):
            if h[days]*scaleMult > highestHigh: highestHigh = h[days]*scaleMult
            if l[days]*scaleMult < lowestLow: lowestLow = l[days]*scaleMult
        hhllDiffScale= (highestHigh - lowestLow) /1.65
        hhllDiff = highestHigh - lowestLow
        botOfChart = lowestLow
        screen.setworldcoordinates(-10,highestHigh-hhllDiffScale,673,highestHigh)
        print(highestHigh," ",lowestLow)
        m=0
        trtl.setheading(0)
        trtl.penup()


        for i in range(startPt,startPt+numBarsPlot+1):
            m=m+1
            trtl.goto(m*10,h[i]*scaleMult)
            trtl.pendown()
            trtl.goto(m*10,l[i]*scaleMult)
            trtl.penup()
            trtl.goto(m*10,c[i]*scaleMult)
            trtl.pendown()
            trtl.goto(m*10+5,c[i]*scaleMult)
            trtl.penup()
            trtl.goto(m*10,o[i]*scaleMult)
            trtl.pendown()
            trtl.goto(m*10-5,o[i]*scaleMult)
            trtl.penup()
            trtl.goto(10,highestHigh)
        print("Indicator List: ",indicatorList)
        if len(indicatorList)!=0:
            movAvgParams = list([])
            if "movAvg" in indicatorList:
                movAvgVal = 0
                movAvgParamIndexVal = indicatorList.index("movAvg")
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 1])
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 2])
                movAvgParams.append(indicatorList[movAvgParamIndexVal + 3])
                for j in range(0,3):
                    n = 0
                    trtl.penup()
                    if j == 0 : trtl.color("red")
                    if j == 1 : trtl.color("green")
                    if j == 2 : trtl.color("blue")
                    for i in range(startPt,startPt+numBarsPlot):
                        n = n + 1
                        movAvgVal = 0
                        for k in range(i-movAvgParams[j],i):
                            movAvgVal = movAvgVal + c[k] * scaleMult
                        if movAvgParams[j] !=0 :
                            movAvgVal = movAvgVal/movAvgParams[j]
                            if i == startPt : trtl.goto(n*10,movAvgVal)
                            trtl.pendown()
                            trtl.goto(n*10,movAvgVal)
                trtl.penup()
#       print("PlotTrades : ",plotTrades)
        if trades.draw:
            debugTradeDate = tradeDate[0]
            debugDate = d[startPt]
            n = 0
            while debugTradeDate <= debugDate:
                n +=1
                debugTradeDate = tradeDate[n]

            m = 0
            for i in range(startPt,startPt+numBarsPlot):
                m = m + 1
                debugDate = d[i]
                if debugDate == debugTradeDate:
                    trtl.penup()
                    tradeValue = tradePrice[n]
                    if tradeType[n] == "buy": 
                        trtl.color("Green")                    
                        trtl.goto(m*10-5,tradeValue - hhllDiff *.03)
                        trtl.pensize(3)
                        trtl.pendown()
                        trtl.goto(m*10,tradeValue)
                        trtl.goto(m*10+5,tradeValue - hhllDiff *.03)
                        trtl.penup()
                    if tradeType[n] == "sell":
                        trtl.color("Red")
                        trtl.goto(m*10-5,tradeValue + hhllDiff *.03)
                        trtl.pensize(3)
                        trtl.pendown()
                        trtl.goto(m*10,tradeValue)
                        trtl.goto(m*10+5,tradeValue + hhllDiff *.03)
                        trtl.penup()
                    if tradeType[n] == "longLiq":
                        trtl.color("Blue")
                        trtl.penup()
                        trtl.goto(m*10-5, tradeValue)
                        trtl.pensize(3) 
                        trtl.pendown()
                        trtl.goto(m*10+5, tradeValue)
                        trtl.penup()                       
                    trtl.pensize(1)
                    print("Found a trade: ",tradeValue," ",debugTradeDate," m= ",m," ",tradeValue-hhllDiff*.05)
                    n+=1
                    if n < len(tradeDate): debugTradeDate = tradeDate[n]
                
        

        trtl.color("black")
        trtl.goto(-10,botOfChart)
        trtl.pendown()
        trtl.goto(673,botOfChart)
        trtl.penup()
        trtl.goto(-10,botOfChart)


        m = 0
        for i in range(startPt,startPt+numBarsPlot):
            if i % 10 == 0 :
                m = m + 1
                trtl.pendown()
                trtl.write(str(d[i]), font=("Arial", 8, "bold")) # chosing the font
                trtl.penup()
                trtl.goto(m*100,botOfChart)

        trtl.penup()
        trtl.goto(628,highestHigh)
        trtl.pendown()
        trtl.goto(628,botOfChart)
        trtl.penup()
        m = 0
        vertIncrement = hhllDiff/10
        for i in range(0,11):
            trtl.goto(630,highestHigh - m*vertIncrement)
            trtl.pendown()
            trtl.write(str(highestHigh - m * vertIncrement),font=("Arial", 8, "bold"))
            trtl.penup()
            m +=1




        # turtle.done()
        screen.onscreenclick(get_mouse_click_coor)
    ##    turtle.mainloop()




def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import PSBChart
    PSBChart.vp_start_gui()
