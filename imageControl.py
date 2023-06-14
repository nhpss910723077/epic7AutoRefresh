import cv2
import numpy as np

class ImageControl:
    def __init__(self, simulator):
        self.simulator = simulator
        
    def matchImages(self, fileName, threshold=0.8):
        # 獲取螢幕截圖
        screenshot = self.simulator.screenshot()

        # 將uiautomator2截圖轉換為OpenCV圖像
        source_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        template_image = cv2.imread(fileName)
        
        # 將圖像轉換為灰階圖像
        gray_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
        
        # 獲取模板圖像的寬度和長度
        h, w = gray_template.shape

        # 使用模板匹配方法進行圖像匹配
        result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

        # 獲取匹配結果中的最大值及位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val)
        
        if max_val >= threshold:
            top_left = max_loc
            
            if(False):
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv2.rectangle(source_image, top_left, bottom_right, (0, 255, 0), 2)
                cv2.imshow('Result', source_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
            return top_left[0] + w / 2, top_left[1] + h / 2
        else:
            print("查無圖片")
            return None
                
        
        
        
        
        