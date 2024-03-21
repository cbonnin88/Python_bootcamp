from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import os
import time



def automated_crypto_pull():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    # Pulling our information from the crypto website
    crypto_name = soup.find("span",class_ = "sc-f70bb44c-0 jltoa").text
    crypto_price = soup.find('span', class_ = 'sc-f70bb44c-0 jxpCgO base-text').text
    final_price = crypto_price.replace("$","")

    # Creating a Time Stamp for our data
    date_time = datetime.now()

    # Creating our dictionary and data frame
    dict = {"Crypto Currency":crypto_name, "Price":final_price,"Time Stamp":date_time}
    df = pd.DataFrame([dict])

    # Pulling it into a CSV File
    if os.path.exists(r"/Users/chris/Desktop/Projects/Project/Csv/Automated_Cryto_Pull.csv"):
        df.to_csv(r"/Users/chris/Desktop/Projects/Project/Csv/Automated_Crypto_Pull.csv",mode ='a', header=False, index=False)
    else:
        df.to_csv(r"/Users/chris/Desktop/Projects/Project/Csv/Automated_Crypto_Pull.csv")
    print(df)
   

    
while True:    
    automated_crypto_pull()
    time.sleep(2)




