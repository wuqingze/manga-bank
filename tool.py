import requests
import time

base_url = 'https://cdn.readdetectiveconan.com/file/mangapill/i/{0}.jpg'
for i in range(852,5080):
    print(base_url.format(i))
    try:
        img_data = requests.get(base_url.format(i), timeout=3).content
        with open(str(i)+".jpg", 'wb') as handler:
            handler.write(img_data)
    except:
        print(base_url.format(i)+" ---  failed")

