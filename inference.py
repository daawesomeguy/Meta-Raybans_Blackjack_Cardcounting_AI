import ultralytics
import selenium
import time
import pickle
import pandas
from selenium import webdriver
from ultralytics import YOLO
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
from twilio.rest import Client
import pywhatkit as pwk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
currentCount = 0
fullCount=0
cardValue = ""
cards = {
  "K": 10,
  "Q": 10,
  "A": 10,
  "J": 10,
  "1": 10,
  "9": 9,
  "8": 9,
  "7": 9,
  "6": 6,
  "5": 6,
  "4": 6,
  "3": 6,
  "2": 6,
}
usedCards = set()

def getCount(string,currentCount):

    if string not in usedCards:
        cardValue = string[0:1]
        if cards[cardValue] == 10:
            currentCount = currentCount-1
        if cards[cardValue] == 6:
            currentCount += 1
        usedCards.add(string)
    return currentCount


options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Github\python-whatsapp-messages\whatsapp-web\data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
serv = Service(r'C:\Users\Jack\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv,options=options)
#,options=chrome_options\
#driver.get('https://web.whatsapp.com/')
#time.sleep(50)

#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#   driver.add_cookie(cookie)
model = YOLO(r"C:\Users\Jack\Desktop\blackjack\yolov8m_synthetic.pt")

print('test')
while 1:
    #rl=input('live link:')
    driver.get('https://www.instagram.com/')
    #time.sleep(50)
    #pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    #driver.get(url)
    driver.get('https://www.instagram.com/jnuge25/live/')
    time.sleep(0.1)
    #driver.find_element(By.CSS_SELECTOR,'body').click()
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/section/button'))).click()

    for i in range(10):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/section/div/div/div[1]/div/div[1]/div'))).screenshot(f'{i}.png')
        '#mount_0_0_N9 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div:nth-child(1) > section > div > div > div.x6ikm8r.x10wlt62 > div > div.xdj266r.x1avx3u8.xat24cr.x1mh8g0r > div'
        '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/section/div/div/div[1]/div/div[1]/div'
        'x1l6l660 x1blamy6 xmwbt37 xyk2qbn xoah1ao x1hq5gj4 xqui205 x6ikm8r x10wlt62'
        image = Image.open(f"{i}.png")
        w,h=image.size
        new_image = image.crop((34,332,w-33,h-333))


    # Save the resized image
        print(new_image.size)
        new_image.save(f"{i}.png")
    # Resize the image
        #new_image = image.crop((0,),())

    # Save the resized image
        #new_image.save(f"{i}.png")
        results = model.predict(f'{i}.png',conf=0.65)
        #boxes = results.xyxy[0]
        #print(boxes)
        #print(results.pred)
        
        for result in results:
            # Get class names
            class_names = model.names
            
            # Iterate over each detected object
            for box in result.boxes:
                # Bounding box coordinates (xyxy format)
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                # Confidence score
                confidence = box.conf[0].item()
                
                # Class ID
                class_id = int(box.cls[0])
                
                # Class name
                class_name = class_names[class_id]
                
                print(f"Detected {class_name} {confidence:.2f}")
                print(f'count={getCount(class_name,currentCount)}')

        result.save(filename=f"result{i}.png") 
        time.sleep(2)

    #time.sleep(0.1)
    driver.get("https://web.whatsapp.com/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[3]/div[1]/div/div/div[1]'))).click()
    #time.sleep(0.2)
    print(usedCards)
    for i in usedCards:
        if cards[i[0:1]]==10:
            fullCount= fullCount-1
        if cards[i[0:1]]==6:
            fullCount+=1
    #[i for i in usedCards if cards[i[0:1]]]
    print(fullCount)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))).send_keys(fullCount)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]/button'))).click()
    #time.sleep(0.1)