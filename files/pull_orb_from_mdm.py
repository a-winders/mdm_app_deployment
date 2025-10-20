import requests
import sys

client_id= sys.argv[1]
client_secret= sys.argv[2]

#Auth Payload
auth_url = f"https://mdm.com/restapi/oAuth:clientId={client_id}/org:default/session"

payload = {
  "clientSecret": client_secret
}

headers = {
  'Accept-Version': '1.0.0',
  'Accept': 'application/json'
}

auth_response = requests.request("POST", auth_url, headers=headers, data=payload).json()

# print(auth_response)

userId = auth_response['data']['user']['userId']
orgId = auth_response['data']['user']['orgId']
authpayload = auth_response['data']['authPayload']
headers['Authpayload'] = authpayload

# Get all devices & store them in a list
devices_url = f"https://mdm.com/restapi/user:id={userId}/org:id={orgId}/devices#v1.0.0"
devices_response = requests.request("GET", devices_url, headers=headers).json()

# print(devices_response)

devices = devices_response['data']['devices']

orb_devices = []

for device in devices:
   if 'ORB' in device['deviceName']:
      device_id = device['deviceId']
      device_name = device['deviceName']
      store_id = device_name.split('_')[1]
      orb_number = device_name.split('_')[2]
      device_dict = {
         "store_id": store_id,
         "device_id": device_id,
         "orb_number": orb_number,
      }  
      orb_devices.append(device_dict)
      
print(orb_devices)

