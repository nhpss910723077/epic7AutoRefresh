import time

class SimulatorControl:
    def __init__(self, imageControl, simulator):
        self.imageControl = imageControl
        self.simulator = simulator
        
        self.imgFolder = "images/"
        
        self.book = {};
        self.book["covenant"] = self.imgFolder + "covenant.png"
        self.book["mystic"] = self.imgFolder + "mystic.png"
        self.buy = self.imgFolder + "buy.png"
        self.refreshButton = self.imgFolder + "refreshButton.png"
        self.refreshConfirm = self.imgFolder + "refreshConfirm.png"

    # 搜尋是否有指定書籤 有則點擊進入購買畫面
    # bookType = covenant 及 mystic 
    def matchBook(self, bookType):
        match_result = self.imageControl.matchImages(self.book[bookType], 0.9)
        if(match_result != None):
            x, y = match_result
            x += 700
            y += 30
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            time.sleep(3)
            
            # 確認是否成功進入購買畫面
            while not self.buyBook():
                time.sleep(0.5)
            
            return True
        
        else: 
            return False
            
    # 確定是否進入購買畫面 成功進入則點擊購買
    def buyBook(self):
        match_result = self.imageControl.matchImages(self.buy, 0.9)
        if(match_result != None):
            print("進入購買畫面成功");
            x = 900
            y = 630
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            
            time.sleep(5)
            
            return True
        else:
            print("進入購買畫面失敗");
            return False
            time.sleep(99999)
    
    # 刷新商店-按鈕
    def refreshShop(self):
        # 確認是否有刷新按鈕
        match_result = self.imageControl.matchImages(self.refreshButton, 0.9)
        if(match_result != None):
            print("搜尋刷新按鈕成功");
            x = 290
            y = 830
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            
            # 確認是否成功進入刷新畫面 如果失敗達5次則重新嘗試進入刷新畫面
            refreshShopConfirmTime = 0
            while not self.refreshShopConfirm():
                if refreshShopConfirmTime >= 5:
                    return False
                else:
                    time.sleep(0.5)
                    refreshShopConfirmTime += 1
                
            return True
            
        else:
            print("搜尋刷新按鈕失敗");
            return False
            time.sleep(99999)
    
    # 刷新商店-確認
    def refreshShopConfirm(self):
        # 確認是否成功進入刷新畫面
        match_result = self.imageControl.matchImages(self.refreshConfirm, 0.9)
        if(match_result != None):
            print("進入刷新畫面成功");
            x = 930
            y = 560
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            
            # 確認商店刷新是否完成
            while not self.confirmRefresh():
                time.sleep(0.5)
            #time.sleep(5)
            
            return True
            
        else:
            print("進入刷新畫面失敗");
            return False
            #time.sleep(99999)
            
    # 確認商店刷新是否完成
    def confirmRefresh(self):
        # 確認是否有刷新按鈕
        match_result = self.imageControl.matchImages(self.refreshButton, 0.9)
        if(match_result != None):
            print("刷新已完成")
            time.sleep(1)
            return True
        else:
            print("刷新尚未完成")
            return False
    
    def swipeShop(self):
        start_x = 900
        start_y = 600
        end_x = 900
        end_y = 300
        self.simulator.swipe(start_x, start_y, end_x, end_y, duration=0.1)
        time.sleep(1)