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
