# insta-pie-api

## A flask server that

1. Accepts GET request in form of:
    1.  /api/v1/users/__*username*__ 
    2.  /api/v1/users/images/__*username*__ 
    3.  /api/v1/users/followers/__*your_username*__ /__*your_password*__ /__*username*__ 
2. After that it: 
    1. Creates selenium bot
        1. Bot may login to instagram with your credentials, if it is needed
    2. Bot goes to instagram.com/__*username*__
    3. Parses page for data
    4. Answers the request in json format

## This is how standart responce looks:

![Image of response](https://i.imgur.com/Sbvh1SG.png) 

## What you need right now:
__*App is dockerized*__

Just install Docker.
## How to start the server: 

In your chosen directory
```bash
git clone git@github.com:QTtrash/insta-pie-api.git
cd insta-pie-api
chmod +rx bin/build
chmod +rx bin/run # So you could just run it as a script.
# Build the image and run the container with it
bin/build
bin/run
```
Server will run locally on port 5000. You can freely send requests now. 

## Future plans: 

* Builds for various OS 
* Better GUI
* faster response times
* more accepted requests like:
    * Images 
    * Followers/Following names and photos
    * Likes
    * Hashtags used
    * Even if account is private bot would be able to log-in to some account, subscribe and still view the requests

## Contacts: 

Email: smouchsiadis@gmail.com <br>
LinkedIn: [Suren Mouchsiadis at LinkedIn](https://www.linkedin.com/in/surenmouchsiadis/) <br>
Twitter: [Suren Mouchsiadis at Twitter](https://twitter.com/QTTrash_) <br>