#!/usr/bin/env python3

base_url = "https://api.meraki.com/api/v1/"
API_KEY = "API key goes here"
src_org_name = "source organization name goes here"
dest_org_name = "destination organization name goes here"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": API_KEY
}

need_radius = False #if RADIUS servers are needed, change this to True
#Add RADIUS server credentials here, to add more radius servers, add more elements to the array
#If one of the keys is not needed, delete that line
#If no RADIUS servers are needed, delete this information
radius_servers = [
    {
        "openRoamingCertificateId": "id of the Openroaming Certificate attached to radius server",
        "port": "udp port the RADIUS server listens on for Access-requests",
        "caCertificate": "certificate used for authorization for the RADSEC Server",
        "host": "ip address of your RADIUS server",
        "secret": "RADIUS client shared secret",
        "radsecEnabled": False #Boolean value, change as needed
    }
]
