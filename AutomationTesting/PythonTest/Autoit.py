'''
Created on 17 Mar 2019

@author: Jitendra Banshpal
'''
import autoit
from PythonTest.CommonFile import *

class Autoit():
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

def NotePad():
    Logger("****Notepad Test Start here****")
    try:
        import subprocess as sp
        programName = "notepad.exe"
        sp.Popen([programName])
        UserDefinedWait(1)
        autoit.win_activate("Untitled - Notepad")
        autoit.send("Autoit Testing")
        autoit.win_close("Untitled - Notepad")
        autoit.control_click("Notepad","[CLASS:Button; INSTANCE:2]")
        Logger("[PASS]")
        Logger("*********************** NotePad TEST PASS ***********************")
    except Exception as e:
        Logger("[FAIL]")
        print(e)
        raise e