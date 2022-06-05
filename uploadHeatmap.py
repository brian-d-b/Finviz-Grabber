from google.cloud import storage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time
from selenium.webdriver.common.by import By



hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
date_string = str(datetime.date.today()) + " %s-%s" % (hour,minute)

def getFinvizData():
    # This sets the options so Selenium uses a headless Firefox instance to get the image
    options = Options()

    # These are for if I figure out how to run this headless
    # options.headless = True
    options.add_argument("--window-size=640,480")

    # Create the selenium webdriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get('https://finviz.com/map.ashx?t=sec')
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/canvas[1]')
    element.screenshot('heatmap.png')
    
def uploadToGoogleStorage():
    # Now we want to upload heatmap.png to our Google cloud storage bucket
    storage_client = storage.Client.from_service_account_json('stonk-webapp-564c9cf1e4b6.json')
    def upload_stored():
        bucket = storage_client.bucket(bucket_name='finviz-heatmap-images')
        blob = bucket.blob(date_string)
        blob.upload_from_filename('heatmap.png')
    def upload_current():
        bucket = storage_client.bucket(bucket_name='current-finviz-image')
        blob = bucket.blob('current.png')
        blob.upload_from_filename('heatmap.png')
    upload_stored()
    upload_current()

#This will get the data from finviz and download the heatmap as an image called heatmap.png
getFinvizData()

#This will upload heatmap.png to a specific bucket for finviz heatmaps in google storage
uploadToGoogleStorage()