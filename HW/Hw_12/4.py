import json
from bs4 import BeautifulSoup
from unidecode import unidecode
from datetime import datetime
import requests

URL = "https://www.time.ir/"
r = requests.get(URL)
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_pnlHorizontalMode")
job_elements = result.find_all("span", class_="inlineBlock ltr text-nowrap")

i = 0
for job in job_elements:
    if i == 0:
        azan_sobh = unidecode(job.text)
    elif i == 1:
        tolooe_khorshid = unidecode(job.text)
    elif i == 2:
        azan_zohr = unidecode(job.text)
    elif i == 3:
        ghoroobe_khorshid = unidecode(job.text)
    elif i == 4:
        azane_maghreb = unidecode(job.text)
    elif i == 5:
        nime_shab = unidecode(job.text)
    i += 1
azan_sobh = datetime.strptime(azan_sobh.replace(" ", ""), "%H:%M")
azan_sobh.strftime("%H:%M")
print("azan_sobh", azan_sobh)
tolooe_khorshid = datetime.strptime(tolooe_khorshid.replace(" ", ""), "%H:%M")
tolooe_khorshid.strftime("%H:%M")
print("tolooe_khorshid", tolooe_khorshid)
azan_zohr = datetime.strptime(azan_zohr.replace(" ", ""), "%H:%M")
azan_zohr.strftime("%H:%M")
print("azan_zohr", azan_zohr)
ghoroobe_khorshid = datetime.strptime(ghoroobe_khorshid.replace(" ", ""), "%H:%M")
ghoroobe_khorshid.strftime("%H:%M")
print("ghorob_khorshid", ghoroobe_khorshid)
azane_maghreb = datetime.strptime(azane_maghreb.replace(" ", ""), "%H:%M")
azane_maghreb.strftime("%H:%M")
print("azane_maghreb", azane_maghreb)
print("nime_shab", nime_shab.replace(" ", ""))
database = {"azan_sobh": (azan_sobh.ctime()),
            "tolooe_khorshid": tolooe_khorshid.ctime(),
            "azan_zohr": azan_zohr.ctime(),
            "ghoroob_khorshid": ghoroobe_khorshid.ctime(),
            "azan_maghreb": azane_maghreb.ctime(),
            "nime_shab": nime_shab}
filename = "4.json"
with open(filename, "r") as file:
    data = json.load(file)
data.append(database)
with open(filename, "w") as file:
    json.dump(data, file)
