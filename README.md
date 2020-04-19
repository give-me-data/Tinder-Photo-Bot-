# Tinder-Photo-Bot-
Tinder Photo Bot 

Download unlimited Tinder Photos from your account. 
No Selenium, only Requests!

My script follows details laid out in Sanskar Jethi's [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44) about a Tinder API vulnerability.

# Settings inside get_pictures.py:

path = "/Your/Photo/Folder/"

X_Auth_Token  = 'Your Token'

df_path "/Your/DataFrame/Path/df.json" 

request_iter = 20




# Variable Information 

## path

Path of folder where you want to safe pictures. 

## df_path
Path of DataFrame and DataFrame name - export as json. 
Create Df if not exist, else append new tinderellas and drop duplicates. 

## X_Auth_Token

To get your own X_Auth_Token: [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44) 

## request_iter

How many Accounts do you want to get photos from:

request_iter * 15 Accounts = Accounts

A test with request_iter = 20 result in more than 1 gb Photos (2k files)

