import json
import os 
import urllib.request
import requests
from pathlib import Path
import pandas as pd 
import time
from tqdm import tqdm

path = "/Users/username/Desktop/tinder_collection/"
X_Auth_Token  = "your_tinder_x_auth_token"
df_path = "/Users/username/Desktop/tinder_df.json"
request_iter = 20


if not os.path.exists(df_path):
    df = pd.DataFrame(columns = ["_id", "bio", "birth_date", "name", "photos"])
else:
    df = pd.read_json(df_path, lines=True)

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'X-Auth-Token': str(X_Auth_Token),
    'app-version': '1023201',
    'platform': 'web',
    "user-session-id": "06dff4fa-c452-4fd2-abd2-8dbd82659da0"

}

for j in range(0,int(request_iter)):
    url = "https://api.gotinder.com/v2/recs/core?locale=de"
    r = requests.request("GET", url, headers=HEADERS)
    assert r.status_code == 200, "GET failed, check auth_token"

    json_resp = json.loads(r.text)

    for i in json_resp["data"]["results"]:
        user_info = {
        "_id": i.get("user").get("_id"),
        "bio": i.get("user").get("bio"),
        "birth_date": i.get("user").get("birth_date"),
        "name": i.get("user").get("name"),
        "photos": [x.get("url") for x in i.get("user").get("photos") if not None]}

        df = df.append(user_info, ignore_index=True)

df.drop_duplicates(subset = ["_id"])
df.to_json(df_path, orient="records", lines=True)

for i in tqdm(range(len(df))):
    for j in range(len(df["photos"][i])):
        if os.path.exists(str(path) + "{}_{}.jpg".format(df["_id"][i], j)):
            continue
        urllib.request.urlretrieve(str(df["photos"][i][j]), str(path) + "{}_{}.jpg".format(df["_id"][i], j))
        





    
