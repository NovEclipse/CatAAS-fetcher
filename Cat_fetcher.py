import requests
import webbrowser
tag = input("Enter the tag for a cat(e.g.: cute,blanket, adorable), just one.: ")
url = f"http://cataas.com/cat/{tag}"


resp = requests.get(url)
if resp.status_code == 200:
    print("Site online, opening a cat picture now...")
    webbrowser.open(url)
else:
    print("Appears that the site is not responding, or tag is not valid.")
