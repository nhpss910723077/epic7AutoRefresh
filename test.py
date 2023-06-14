import keyboard
import time
import uiautomator2 as u2

import imageControl as ic
import simulatorControl as sc

exitControl = True
def ExitControl(event):
    global exitControl
    if event.name == 'f1':
        exitControl = False

maxTime = int(input("輸入最大次數: "))

print("按下 F1 結束程式");
keyboard.on_press(ExitControl)

# 連接夜神模擬器
# simulator = u2.connect('127.0.0.1:62001')
simulator = u2.connect()

imageControl = ic.ImageControl(simulator)
simulatorControl = sc.SimulatorControl(imageControl, simulator)

totalTime = 0
totalCovenant = 0
totalMystic = 0

canBuyCovenant = True;
canBuyMystic = True;
while exitControl and totalTime <= maxTime:
    canBuyCovenant = True;
    canBuyMystic = True;
    
    if(canBuyCovenant):
        if(simulatorControl.matchBook("covenant")):
            canBuyCovenant = False
            totalCovenant += 1
            
    if(canBuyMystic):
        if(simulatorControl.matchBook("mystic")):
            canBuyMystic = False
            totalMystic += 1
            
    simulatorControl.swipeShop()
    
    if(canBuyCovenant):
        if(simulatorControl.matchBook("covenant")):
            canBuyCovenant = False
            totalCovenant += 1
            
    if(canBuyMystic):
        if(simulatorControl.matchBook("mystic")):
            canBuyMystic = False
            totalMystic += 1
            
    #刷新商店
    while not simulatorControl.refreshShop():
        time.sleep(0.5)
    
    totalTime += 1
    
print("已刷新次數 : " + str(totalTime))
print("已花費天空石 : " + str(totalTime * 3))
print("已取得聖約書籤 : " + str(totalCovenant * 5))
print("已取得神秘書籤 : " + str(totalMystic * 50))
print("聖約書籤機率 : " + str((totalCovenant / totalTime) * 100) + "%")
print("神秘書籤機率 : " + str((totalMystic / totalTime) * 100) + "%")
input("按下 Enter 關閉視窗...")