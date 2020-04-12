import requests
import json
import base64

/********************************************************************************
Get Posts
********************************************************************************/

url = "https://wholeblogs.com/wp-json/wp/v2/posts"

user = "your-username"
password = "your-application-password"

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

responce = requests.get(url , headers=header)

print(responce)

/********************************************************************************
Create Post
********************************************************************************/

url = "https://wholeblogs.com/wp-json/wp/v2/posts"

user = "your-username"
password = "your-application-password"

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {
	'title'   	: 'Hello World',
	'status'  	: 'publish', 
	'content' 	: 'This is my first post created using rest API',
	'categories': 5, // category ID
	'date' 		: '2020-01-05T10:00:00'
}

responce = requests.post(url , headers=header, json=post)

print(responce)

/********************************************************************************
Update Post
********************************************************************************/

url = "https://wholeblogs.com/wp-json/wp/v2/posts/"

postID = 1

user = "your-username"
password = "your-application-password"

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {
	'title'   	: 'Hello World Updated',
	'content' 	: 'This is my first post created using rest API Updated'
}

responce = requests.post(url + postID , headers=header, json=post)

print(responce)

/********************************************************************************
Delete Post
********************************************************************************/

url = "https://wholeblogs.com/wp-json/wp/v2/posts/"

user = "your-username"
password = "your-application-password"

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

responce = requests.delete(url + postID , headers=header)

print(responce)
