import requests

for i in range(1,112):
    print("i: " + str(i))
    url = "https://github.com/kmw1704/form_photos/blob/main/f1_"+ str(i) + ".jpg?raw=true"

    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
            print("✅ URL returned an image")
        else:
            print(f"⚠️ Not an image. Status: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching URL:", e)



