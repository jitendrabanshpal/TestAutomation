'''
Created on 07 Mar 2019

@author: Jitendra Banshpal
'''
from PythonTest.CommonFile import *
# import yaml
# import sys, traceback


class FlightBook():
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

def Registration():
    Logger("****Registration Test Start here****")
    try:
        driver =load_driver()
        UserDefinedWait(1)
        if objectexistance("XPATH","/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a") == True:
            objectoperation("XPATH", "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a", "LINK", "CLICK", "")
        else:
            Logger("REGISTER Link is not visible")
        with open('data.yml', 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
        firstname = str(doc["UserDetails"]["FirstName"])
        lastname = str(doc["UserDetails"]["LastName"])
        phoneno = str(doc["UserDetails"]["PhoneNo"])
        email = str(doc["UserDetails"]["Email"])
        add1 = str(doc["UserDetails"]["Add1"])
        add2 = str(doc["UserDetails"]["Add2"])
        city = str(doc["UserDetails"]["City"])
        state = str(doc["UserDetails"]["State"])
        postcode = str(doc["UserDetails"]["PostCode"])
        country = str(doc["UserDetails"]["Country"])
        usename = str(doc["UserDetails"]["UserName"])
        password = str(doc["UserDetails"]["Password"])
        confirmpassword = str(doc["UserDetails"]["ConfirmPassword"])
        objectoperation("NAME", "firstName", "TEXT", "TYPE", firstname)
        objectoperation("NAME", "lastName", "TEXT", "TYPE", lastname)
        objectoperation("NAME", "phone", "TEXT", "TYPE", phoneno)
        objectoperation("ID", "userName", "TEXT", "TYPE", email)
        objectoperation("NAME", "address1", "TEXT", "TYPE", add1)
        objectoperation("NAME", "address2", "TEXT", "TYPE", add2)
        objectoperation("NAME", "city", "TEXT", "TYPE", city)
        objectoperation("NAME", "state", "TEXT", "TYPE", state)
        objectoperation("NAME", "postalCode", "TEXT", "TYPE", postcode)
        objectoperation("NAME", "country", "LISTBOX", "SELECT", country)
        objectoperation("NAME", "email", "TEXT", "TYPE", usename)
        objectoperation("NAME", "password", "TEXT", "TYPE", password)
        objectoperation("NAME", "confirmPassword", "TEXT", "TYPE", confirmpassword)
        objectoperation("NAME", "register", "IMAGE", "CLICK", "")
        Logger("[PASS]")
        Logger("*********************** REGISTRATION TEST PASS ***********************")
        takescreenshot("PASS")
        closeexecution()
    except Exception as e:
        Logger("[FAIL]")
        takescreenshot("FAIL")
        print(e)
        raise e

def Login():
    Logger("****Login Test Start here****")
    try:
        driver =load_driver()
        UserDefinedWait(1)
        if objectexistance("XPATH","/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a") == True:
            objectoperation("XPATH", "/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a","LINK", "CLICK", "")
        else:
            Logger("HOME Link is not visible")
        with open('data.yml', 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
        username = str(doc["UserDetails"]["UserName"])
        password = str(doc["UserDetails"]["Password"])
        objectoperation("NAME", "userName", "TEXT", "TYPE", username)
        objectoperation("NAME", "password", "TEXT", "TYPE", username)
        objectoperation("NAME", "login", "IMAGE", "CLICK", "")
        WaitForBrowserTitleDisplay("Find a Flight: MercuryTours:",10)
        assert driver.title == "Find a Flight: MercuryTours:"
        Logger("[PASS]")
        Logger("*********************** LOGIN TEST PASS ***********************")
        takescreenshot("PASS")
        closeexecution()
    except Exception as e:
        Logger("[FAIL]")
        takescreenshot("FAIL")
        print(e)
        raise e