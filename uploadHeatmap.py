from google.cloud import storage
from selenium import webdriver
import datetime

date = datetime.date.today()

def getFinvizData():
    # This sets the options so Selenium uses a headless Firefox instance to get the image
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()

    browser = webdriver.Firefox(firefox_options=fireFoxOptions)
    browser.get('https://finviz.com/map.ashx?t=sec')
    element = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/canvas[2]')
    element.screenshot('foo.png')
    
def uploadToGoogleStorage():
    # Now we want to upload foo.png to our Google cloud storage bucket
    storage_client = storage.Client.from_service_account_json('triple-bonito-341905-b13c51726f6b.json')
    bucket = storage_client.bucket(bucket_name='finviz-heatmaps')
    blob = bucket.blob(str(date))
    blob.upload_from_filename('foo.png')
    
    
getFinvizData()
uploadToGoogleStorage()