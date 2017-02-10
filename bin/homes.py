#!/usr/bin/python

import urllib, urllib2, json

# "https://my.tado.com/oauth/token" 
# -d client_id=tado-webapp -d grant_type=password -d password=yourPasssword -d scope=home.user -d username=you@yourEmail.whatever 
#  perl -pe 's/^.*"access_token"\s*:\s*"([^"]*).*/$1/' > /tmp/tadotoken

tadoemail = "nick.hills@gmail.com"
tadopassword = "kuSf4SMugtXw"

def main():
	token = getAuth(tadoemail, tadopassword)
	homeId = getHomeId(token)
	doRequest(token,homeId)

def getAuth(email, password):

	data = dict(client_id="tado-webapp",grant_type="password",password=password,scope="home.user", username=email )
	authUrl = "https://my.tado.com/oauth/token"
	method = "POST"
	handler = urllib2.HTTPHandler()
	opener = urllib2.build_opener(handler)
	data = urllib.urlencode(data)
	request = urllib2.Request(authUrl, data=data)
	request.get_method = lambda: method
	try:
    		connection = opener.open(request)
	except urllib2.HTTPError,e:
    		connection = e

	if connection.code == 200:
    		responseData = str(connection.read())
		jsonList = json.loads(responseData)

		return jsonList['access_token']
	else:
		print "errorCode="+str(connection.code)

def getHomeId(token):
	url = "https://my.tado.com/api/v2/me"

	req = urllib2.Request(url)
        req.add_header("Authorization","Bearer "+token)

        handler = urllib2.HTTPHandler()
        opener = urllib2.build_opener(handler)
        try:
                connection = opener.open(req)
        except urllib2.HTTPError,e:
                connection = e

        if 200 <= connection.code <= 207:
 		responseData = str(connection.read())
                jsonList = json.loads(responseData)

		return jsonList['homes'][0]['id']
        else:
                print "errorCode="+str(connection.code)

def doRequest(token,homeId):


	url = "https://my.tado.com/api/v2/homes/"+str(homeId)

	req = urllib2.Request(url)
	req.add_header("Authorization","Bearer "+token)

	handler = urllib2.HTTPHandler()
	opener = urllib2.build_opener(handler)
	try:
		connection = opener.open(req)
	except urllib2.HTTPError,e:
		connection = e

	if 200 <= connection.code <= 207:
		print connection.read()
	else:
		print "errorCode="+str(connection.code)

main()
