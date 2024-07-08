from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://www.whitehouse.gov/briefing-room/speeches-remarks/2024/03/07/remarks-of-president-joe-biden-state-of-the-union-address-as-prepared-for-delivery-2/"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html")

sotu2024 = soup.find_all("p")

speech_combinded = [p.text for p in sotu2024]
string_speech = " ".join(speech_combinded)

string_speech_cleaned = string_speech.replace("\r\n//", " ")

speech_no_punc = re.sub(r"[^\w\s]", "", string_speech_cleaned)

speech_lower = speech_no_punc.lower()
speech_broken_out = re.split(r"\s+", speech_lower)

df = pd.DataFrame(speech_broken_out).value_counts()

df.to_csv(r"/Users/chris/Desktop/Projects/Project/Csv/State_of_The_Union2024.csv", header=["Counts"],
          index_label="Word")
