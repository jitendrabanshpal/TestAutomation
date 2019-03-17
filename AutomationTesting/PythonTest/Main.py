'''
Created on 15 Mar 2019

@author: Jitendra Banshpal
'''

from PythonTest.CommonFile import *
from PythonTest.Test1_Web import Login,Registration
from PythonTest.Autoit import NotePad
import time
import datetime
from PythonTest.ClientMachineDetails import FullClientMachineDetails

if __name__ == '__main__':
    pass
try:
    executionstarttime()
    generatefilename()
    trucatereportfile()
    FullClientMachineDetails()
    Registration()
    NotePad()
    datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    createreport("Test Execution Completed " + str(datetoday))
    time.sleep(5)
    executionendtime()
except Exception as e:
    print(e)
    closeexecutionfailure()