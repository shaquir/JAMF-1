#!/usr/bin/python
# Written by Heiko Horn on 2018.03.06
# This script get the vpp information for all computer applications in Jamf Pro using JSON.

import urllib2, json, plistlib

strJamfUrl = plistlib.readPlist('/Library/Preferences/com.jamfsoftware.jamf.plist')['jss_url'] + '/JSSResource'
#strJamfUrl = 'https://xxx.xxx.xxx:8443/JSSResource'
strApiUrl = strJamfUrl + '/macapplications'
base64Auth = ''

request = urllib2.Request(strApiUrl)
request.add_header('Authorization', 'Basic ' + base64Auth)
request.add_header('Accept', 'application/json')

objJson=json.loads(urllib2.urlopen(request).read())
for item in objJson['mac_applications']:
	intId=item['id']
	strName=item['name']
	strApiUrlApp=strApiUrl + '/id/' + str (intId)
	appRequest=urllib2.Request(strApiUrlApp)
	appRequest.add_header('Authorization', 'Basic ' + base64Auth)
	appRequest.add_header('Accept', 'application/json')
	objJsonApp=json.loads(urllib2.urlopen(appRequest).read())
	if objJsonApp['mac_application']['vpp']['vpp_admin_account_id'] == 1:
		print ('ID: ' + str (intId))
		print ('Name: ' + strName)
		print ('Vpp account Id: ' + str (objJsonApp['mac_application']['vpp']['vpp_admin_account_id']))
		print ('Tolal licenses: ' + str (objJsonApp['mac_application']['vpp']['total_vpp_licenses']))
		print ('Used licenses: ' + str (objJsonApp['mac_application']['vpp']['used_vpp_licenses']))
		print ('Free: ' + str (objJsonApp['mac_application']['general']['is_free']))
		print ('')