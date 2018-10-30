# Digital-signage

Django-site : contains code for Django Application

Content management system :
Django appliction Facilitate media contents upload.It also provide the url to download images and Json Response.

JSON RESPONSE:Json responce for account is displayed on fixed url:"Ip adrress:9012/download".This response is required to 
distinguish between Active and Inactive assets.Json response render the name,duration,id and url  to download the particular file.

file Download:To Download each active file Json response must be parsed.File can be downloaded by  
url: "IPaddress:9012/fetching_asset/id "// note 'id' here is the one which is parsed from json Response for each media file.
 


Response.py //this file is for on Device(Raspberry pi)Pulling of populated content in application.
Raspberry Pi: Ondevice Software using Python.
1)This code pulls the json response and parses it.
2)Then the file are downloaded by appending the 'ID' of each file to the file download url.this renders the Media file.
3)This file are displayed as per the duration in the Json response on a monitor.
