import json, requests, tkinter.messagebox
def writejson(filename, dictionary):
    if ".json" not in filename:
        filename=filename+".json"
    print(f"Writing {dictionary} to {filename}")
    with open(filename, 'w') as f:
        json.dump(dictionary, f, indent=2)

def readjson(filename):
    if ".json" not in filename:
        filename=filename+".json"
    print(f"Reading {filename}")
    with open(filename, 'r') as f:
        file=json.load(f)
    return file

def downloadjson(filename, url="https://github.com/DaCosySheeep/Fact-Downloader/raw/main/", windowtitle="Fact Downloader JSON Manager", silent=None):
    print("Downloading", url+filename)
    try:
        download=requests.get(url+filename)
        file=json.loads(download.text)
        return file
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        if silent != True:
            tkinter.messagebox.showerror(title=windowtitle, message="Error. Please check your internet connection")
        return None
