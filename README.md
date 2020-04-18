# wordpress with python

Example of WordPress REST API with Python. we will fetch all posts, create one new post, update it and delete it using REST API with Python.

## Authentication 🔒
First of all, we need basic authentication for performing crud operation and it won’t work until you install a special plugin named application password to get the application password.
Go to your dashboard -> plugin -> Add new and type application password in the search box.

Once you installed plugin go to your profile settings and scroll to the bottom. You will see one application password field will be added there. Type you application name and hit enter and popup will appear with a password. Copy generated password from popup.

## It’s time to go through the python 👽
Now, Create one file with the .py extension. You can give it any name (for example app.py).
```
Import some required packages:
import requests
import json
import base64
```

## Fetch Posts 📮
```
url = "https://example.com/wp-json/wp/v2/posts"
user = "your-username"
password = "your-application-password"
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
responce = requests.get(url , headers=header)
print(responce)
```
Let’s understand this code.
URL is the URL of the site from which you want to fetch posts.
user is your admin username.
password is the application password that you have generated just before.
Encode your credentials and pass them in header authorization as shown in code.
At the bottom of the line we are printing our response to see what we are getting.
Now, open your terminal and run your app.py file.
python app.py

## Create Post 📮
To create a post we need to make the post request with some required parameters like URL, your JSON data. Let’s do that:
```
url = "https://example.com/wp-json/wp/v2/posts"
user = "your-username"
password = "your-application-password"
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
post = {
 'title'    : 'Hello World',
 'status'   : 'publish', 
 'content'  : 'This is my first post created using rest API',
 'categories': 5, // category ID
 'date'   : '2020-01-05T10:00:00'
}
responce = requests.post(url , headers=header, json=post)
print(responce)
```

## Update Post 📮
To update post you need to pass post id to tell REST API which post you want to update. Let’s see how to do that.
```
url = "https://example.com/wp-json/wp/v2/posts/"
postID = 1
user = "your-username"
password = "your-application-password"
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
post = {
 'title'    : 'Hello World Updated',
 'content'  : 'This is my first post created using rest API Updated'
}
responce = requests.post(url + postID , headers=header, json=post)
print(responce)
```
Here, postID is the id of the post you want to update.

## Delete Post 📮
To delete a post we need to use delete requests provided by python.
```
url = "https://example.com/wp-json/wp/v2/posts/"
user = "your-username"
password = "your-application-password"
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
responce = requests.delete(url + postID , headers=header)
print(responce)
```

 ## Useful Blogs:
   1. [Create Single Page Application With React js and WordPress REST API](http://wholeblogs.com/how-to-create-a-single-page-applicationspa-with-react-js-and-wordpress-rest-api/)
   2. [How to create custom Gutenberg block as a begginer](https://medium.com/@brijeshdhanani/steps-to-create-custom-gutenberg-block-as-a-beginner-62e13e1d5e1c)
   3. [WordPress REST API With Python](https://wholeblogs.com/wordpress-rest-api-with-python/)
   
Please follow me on [Medium](https://medium.com/@brijeshdhanani) and [github](https://github.com/BRdhanani) 🙏
