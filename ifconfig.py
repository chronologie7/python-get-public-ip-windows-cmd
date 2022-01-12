import urllib.request , json

url = "https://ifconfig.me/all.json"
try:
    with urllib.request.urlopen(url) as urldata:
        data = json.loads(urldata.read())
    print(f"Your public ipv4: {data['ip_addr']}")
except:
    print("connection failed.")
