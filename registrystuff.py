import winreg, tkinter.messagebox

def readreg(valuename, key="Auto", subkey="Software\\DaCosySheeep\\Fact Downloader", silent=None, type="string"):
    #user can be "CurrentUser", "LocalMachine", or "Auto"
    print("Reading registry")
    def readregistry(key, subkey, valuename):
        try:
            registry_key=winreg.OpenKey(key, subkey, 0, winreg.KEY_READ)
            value, valuetype=winreg.QueryValueEx(registry_key, valuename)
            print("Valuetype:", valuetype)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            print("Error reading registry")
            #if silent !=True:
                #tkinter.messagebox.showerror(title="Fact Downloader", message=f"Error reading {valuename}.")
            return None
    if key.lower()=="currentuser":
        print("key=currentuser")
        registry_key=readregistry(key=winreg.HKEY_CURRENT_USER, subkey=subkey, valuename=valuename)
    elif key.lower()=="localmachine":
        print("key=localmachine")
        registry_key=readregistry(key=winreg.HKEY_LOCAL_MACHINE, subkey=subkey, valuename=valuename)
    elif key.lower()=="auto":
        print("key=auto")
        registry_key=readregistry(key=winreg.HKEY_CURRENT_USER, subkey=subkey, valuename=valuename)
        if registry_key==None:
            registry_key=readregistry(key=winreg.HKEY_LOCAL_MACHINE, subkey=subkey, valuename=valuename)
    else:
        print("key=Unknown")
        print("key must be CurrentUser, LocalMachine or Auto")
        return
    if registry_key==None and (type.lower() != "bool" and type.lower() != "boolean"):
        #print("Error reading registry. Value doesn't exist")
        if silent != True:
            tkinter.messagebox.showerror("Fact Downloader", f"Error reading {valuename}.")
        if type.lower()=="string" or type.lower()=="str":
            return "Unknown"
        if type.lower()=="int" or type.lower()=="integer":
            return -1
    elif type.lower()=="int" or type.lower()=="integer":
        return int(registry_key)
    else:
        return registry_key