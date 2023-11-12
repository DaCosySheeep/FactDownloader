from tkinter.messagebox import showerror, askyesno, showwarning
import requests, os, winreg, jsonstuff, subprocess
from registrystuff import readreg

def getcurrentv(silent=None):
    print("Running: 'getcurrentv'")
    currentv=readreg(valuename="Version", silent=silent)
    print("Current version is", currentv)
    return currentv

def getlatestv(silent=None):
    print("Running: 'getlatestv'")
    print("Getting latest version")
    return (jsonstuff.downloadjson(filename="latest.json", silent=silent))["version"]

def checkforupdate(silent=None, currentv=getcurrentv(), latestv=getlatestv()):
    print("Running: 'checkforupdate'")
    try:
        #currentv=getcurrentv()
        #latestv=getlatestv()
        print("Checking for update...")
        
        print("The latest version is", latestv)
        print("The current version is", currentv)
        if currentv == "Unknown":
            if silent != True:
                showerror(title="Version Error", message="There was an error checking the current version of Fact Downloader. Please try reinstalling or manually updating.")
            updateavailable = None
        elif currentv != latestv:
            updateavailable = True
        elif currentv == latestv:
            updateavailable = False
        else: 
            updateavailable=None

    except:
        print("Error")
        if silent != True:
            showerror(title="Unknown Error", message="There was an unknown error when checking for updates. Please try reinstalling or manually updating.")
        updateavailable=None

def installupdate(version=getlatestv(), silent=None, ProgDataDir="C:\\ProgramData\\DaCosySheeep\\Fact Downloader", windowtitle="Fact Downloader Update Service"):
    print("Running 'installupdate'")
    print("Preparing to install update")
    try:
        if version not in jsonstuff.downloadjson(filename="versions.json", silent=silent)["versions"]:
            if silent != True:
                showerror(title=windowtitle, message="Unable to update Fact Downloader. That version doesn't exist.")
            print(version, "Does not exist. Cancelling update.")
            return
        if version == getcurrentv():
            if silent != True:
                #showwarning(title="Fact Downloader Updater", message="You are already running the version you are trying to upgrade to. Would you like to continue?")
                update=askyesno(title=windowtitle, message=f"You are already running the version you are trying to upgrate to ({version}). Would you like to continue?", icon="warning")
                if update==False:
                    print("Cancelled update.")
                    return
            elif silent == True:
                print("Cancelled update due to matching versions")
                return
        file_size=jsonstuff.downloadjson(filename="versions.json", silent=silent)["sizes"][version]
        print(file_size)
        update=False
        if silent != True:
            update=askyesno(title=windowtitle, message=f"Are you sure to update from {getcurrentv()} to {version}? This will download {file_size} to your computer.")
        elif silent == True:
            update=True
        if update==True:
            print(f"Updating from {getcurrentv()} to {version}")    
            open(ProgDataDir+f'\\setupfiles\\factdownloader-{version}-setup.exe', 'wb').write((requests.get(f'https://github.com/DaCosySheeep/Fact-Downloader/raw/main/factdownloader-{version}-setup.exe')).content)
            subprocess.run([ProgDataDir+f"\\setupfiles\\factdownloader-{version}-setup.exe", "/SILENT", "/FORCECLOSEAPPLICATIONS"])
        else:
            return

    except requests.exceptions.ConnectionError:
        if silent != True:
            showerror(title=windowtitle, message="Error updating. Please check your internet connection.")
    except KeyError:
        if silent != True:
            showerror(title=windowtitle, message="Error reading value.")

#print(getlatestv())
