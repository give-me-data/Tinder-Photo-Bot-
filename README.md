# Tinder Photo Bot

Tinder Photo Bot 

-- Perfect to get data to train your Machine Learning Models ;) --

Download unlimited Tinder Photos from your account. 
No Selenium, only Requests!

-- 19 Apr 2020 --

My script follows details laid out in Sanskar Jethi's [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44) about a Tinder API vulnerability.

# Settings inside get_pictures.py:

path = "/Your/Photo/Folder/"

X_Auth_Token  = 'Your Token'

df_path "/Your/DataFrame/Path/df.json" 

request_iter = 20




# Variable Information

## path

Path of the folder where you want to save pictures.

"/Users/username/Desktop/tinder_collection/"

## df_path

Path of DataFrame and DataFrame name - export as json. Create Df if not exist, else append new tinderellas (users) and drop duplicates.

"/Users/username/Desktop/tinder_df.json"

Features: 

- _id (You can build a like bot with following get request - same HEADERS: https://api.gotinder.com/like/{_id}?locale=de)
- bio (str)
- birth_date (str)
- photos (list)

## X_Auth_Token (as string)

To get your own X_Auth_Token:  [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44)

## request_iter

Number of accounts you want to get photos from:

request_iter * 15 Accounts = Accounts

A test with request_iter = 20 (300 Accounts) results in more than 1 GB Photos (2k files)
