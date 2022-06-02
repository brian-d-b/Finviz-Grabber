from google.cloud import storage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time


hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
date_string = str(datetime.date.today()) + " %s-%s" % (hour,minute)

def getFinvizData():
    # This sets the options so Selenium uses a headless Firefox instance to get the image
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    time.sleep(3)
    driver.get('https://finviz.com/map.ashx?t=sec')
    time.sleep(10)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/canvas[2]')
    element.screenshot('foo.png')
    
def uploadToGoogleStorage():
    # Now we want to upload foo.png to our Google cloud storage bucket
    storage_client = storage.Client.from_service_account_json('triple-bonito-341905-b13c51726f6b.json')
    bucket = storage_client.bucket(bucket_name='finviz-heatmaps')
    blob = bucket.blob(date_string)
    blob.upload_from_filename('foo.png')

#This will get the data from finviz and download the heatmap as an image called foo.png
getFinvizData()

#This will upload foo.png to a specific bucket for finviz heatmaps in google storage
uploadToGoogleStorage()