'''
Created on 13 Mar 2019

@author: Jitendra Banshpal
'''
from PythonTest.CommonFile import Logger,createreport
import winreg
import platform

class ClientMachineDetails(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
def Machine_OS_Details():
    Logger("************************* Client Machine Operating System Details Start *******************************")
    Logger("Test Machine Platform Details: "+platform.platform())
    if platform.uname().processor.find('Intel64') != -1:
        Logger("Test Machine is 64 bit Architecture")
    else:
        Logger("Test Machine is 32 bit Architecture")
        Logger("************************* Client Machine Operating System Details End *************************************")

keypath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
def subkeys(key):
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            yield subkey
            i+=1
        except WindowsError as e:
            print(e)
            break


def traverse_registry_tree_soft1_64bit(hkey, keypath, tabs=0):

    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, keypath, 0, winreg.KEY_READ|winreg.KEY_WOW64_64KEY)
    for subkeyname in subkeys(key):
        subkeypath = "%s\%s" % (keypath, subkeyname)
        if subkeyname == "{F2B7F75B-0BE7-476C-A1A9-F227D25C9439}" : # need to provide exect subkey name for required software
            try:
                newkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkeypath, 0, winreg.KEY_READ|winreg.KEY_WOW64_64KEY)
                DisplayName = winreg.QueryValueEx(newkey, "DisplayName")
                DisplayVersion = winreg.QueryValueEx(newkey, "DisplayVersion")
                Soft1Details = (DisplayName[0]+" Version is : "+DisplayVersion[0])
                createreport("software soft1 details: "+str(Soft1Details))
            except WindowsError:
                pass
            break
        else:
            continue        
        traverse_registry_treesoft1(hkey, subkeypath, tabs+1)


def traverse_registry_tree_soft2_32bit(hkey, keypath, tabs=0):
 
    key = winreg.OpenKey(hkey, keypath, 0, winreg.KEY_READ|winreg.KEY_WOW64_32KEY)
    for subkeyname in subkeys(key):
        subkeypath = "%s\%s" % (keypath, subkeyname)
        if subkeyname == "{961D8F5A-603C-40E9-BEDD-91F6990C43F0}" : # need to provide exect subkey name for required software
            try:
                newkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkeypath, 0, winreg.KEY_READ|winreg.KEY_WOW64_32KEY)
                DisplayName = winreg.QueryValueEx(newkey, "DisplayName")
                DisplayVersion = winreg.QueryValueEx(newkey, "DisplayVersion")
                Soft2Details = (DisplayName[0]+" Version is : "+DisplayVersion[0])
                createreport("software soft2 details: "+str(Soft2Details))
            except WindowsError:
                pass
            break
        else:
            continue
            traverse_registry_tree_soft2_32bit(winreg.HKEY_LOCAL_MACHINE, subkeypath, tabs+1)


def FullClientMachineDetails():
    Logger("************************* Client Machine Software Details Start *************************************")
    Machine_OS_Details()
    traverse_registry_tree_soft1_64bit(winreg.HKEY_LOCAL_MACHINE, keypath)
    traverse_registry_tree_soft2_32bit(winreg.HKEY_LOCAL_MACHINE, keypath)
    Logger("************************* Client Machine Software Details End *************************************")

