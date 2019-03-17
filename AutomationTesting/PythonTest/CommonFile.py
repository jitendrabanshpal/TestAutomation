'''
Created on 25 feb 2019

@author: Jitendra Banshpal
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
import time
import os, platform
import yaml
import string
import random
from random import randint
from builtins import str
import sys



class GenericFunction(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''


# ===========================================
global result1
driver = None

'''
UserDefinedWait(inputtime) function works as mentioned below
To provide the forced wait time  
if UserDefinedWait(10) ----> execution will wait for 10 second
'''

def UserDefinedWait(inputtime):
    time.sleep(inputtime)

'''
load_driver() function works as mentioned below
To load driver please check the prereq.yml file 
if Browser = IE ----> opens IE Driver
if Browser = Chrome ----> opens Chrome Driver
if Browser = FireFox ----> opens FireFox Driver
'''

def load_driver():
    try:
        global driver
        with open('prereq.yml', 'r') as f:
            doc = yaml.load(f,Loader=yaml.FullLoader)
        if (doc["EnvironmentDetails"]["Browser"] == "IE"):
            driver = webdriver.Ie((doc["EnvironmentDetails"]["dirpath"] + "IEDriverServer.exe"))
            UserDefinedWait(2)
            driver.get(doc["EnvironmentDetails"]["TestEnvUrl"])
            driver.maximize_window()
            return (driver)
        elif (doc["EnvironmentDetails"]["Browser"] == "FireFox"):
            driver = webdriver.Firefox()
            driver.get(doc["EnvironmentDetails"]["TestEnvUrl"])
            driver.maximize_window()
            return (driver)
        elif (doc["EnvironmentDetails"]["Browser"] == "Chrome"):
            driver = webdriver.Chrome(doc["EnvironmentDetails"]["dirpath"] + "chromedriver.exe")
            driver.get(doc["EnvironmentDetails"]["TestEnvUrl"])
            driver.maximize_window()
            return (driver)
    except Exception as e:
        print(e)
        raise e

def Logger(text):
    createreport(text)
    print(text)

def createreport(text):
    with open('config.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    filename = doc["EnvironmentDetails"]["reportfile"]
    if os.path.exists(filename) == True:
        fileopen = open(filename, "a+")
        fileopen.write(text)
        fileopen.write("\n")
    else:
        fileopen = open(filename, "a+")
        fileopen.write(text)
        fileopen.write("\n")


def directorylocation(loc):
    with open('prereq.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    if loc == "DATA":
        locationpath = str(doc["EnvironmentDetails"]["dirpath"])
        return (locationpath)
    elif loc == "CMS":
        locationpath = str(doc["EnvironmentDetails"]["cardpath"])
        return (locationpath)


'''
unique_string_generator() function works as mentioned below
It generates the six char string with all in upper case

'''


def unique_string_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


'''
filenamegeneration(filestatus) function works as mentioned below
It generates the filename based on given parameters
if filestatus is PASS ---> generates screenshot file for pass
if filestatus is Fail ---> generates screenshot file for fail
'''


def filenamegeneration(filestatus):
    dateandtime = datetime.datetime.now()
    datetoday = ("%s-%s-%s-%s-%s-%s" % (
    dateandtime.year, dateandtime.month, dateandtime.day, dateandtime.hour, dateandtime.minute, dateandtime.second))
    if filestatus == "PASS":
        filename = str("Pass" + datetoday + ".png")
        return (filename)
    elif filestatus == "FAIL":
        filename = str("Fail" + datetoday + ".png")
        return (filename)
    else:
        filename = str("Unknown" + datetoday + ".png")
        return (filename)



'''
takescreenshot(Status) function works as mentioned below
It takes the status as PASS or FAIL --->
and takes screenshot and save in path where user wants (config.yaml file).
'''


def takescreenshot(status):
    with open('prereq.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    fpath = str(doc["EnvironmentDetails"]["dirpath"])
    fname = filenamegeneration(status)
    scpath = str(fpath)
    scfname = str(fname)
    scdetails = scpath + scfname
    driver.get_screenshot_as_file(scdetails)


'''
readvaluefromUI(objidtype, objid) function works as mentioned below
It takes the objidtype ---> e.g. (ID,CSS_SELECTOR,NAME etc)
It takes the objid ---> actual id of object
and retrun the text value of object
'''


def readvaluefromUI(objidtype, objid):
    try:
        if objidtype == "ID":
            element = driver.find_elements(objid).text
            return (element)
        elif objidtype == "CSS_SELECTOR":
            element = driver.find_element_by_css_selector(objid).text
            return (element)
        elif objidtype == "CLASS_NAME":
            element = driver.find_elements_by_class_name(objid).text
            return (element)
        elif objidtype == "XPATH":
            element = driver.find_element_by_xpath(objid).text
            return (element)
        elif objidtype == "TAGNAME":
            element = driver.find_elements_by_tag_name(objid).text
            return (element)
        elif objidtype == "NAME":
            element = driver.find_elements_by_name(objid).text
            return (element)
    except Exception as e:
        print(e)
        raise e


def objectexistance(objidtype, objid):
    try:
        if objidtype == "ID":
            if (driver.find_element_by_id(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
        elif objidtype == "CSS_SELECTOR":
            if (driver.find_element_by_css_selector(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
        elif objidtype == "CLASS_NAME":
            if (driver.find_elements_by_class_name(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
        elif objidtype == "XPATH":
            if (driver.find_element_by_xpath(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
        elif objidtype == "TAGNAME":
            if (driver.find_elements_by_tag_name(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
        elif objidtype == "NAME":
            if (driver.find_elements_by_name(objid).is_displayed() == True):
                return (True)
            else:
                return (False)
    except Exception as e:
        print(e)
        raise e

def objectoperation(objidtype, objid, objtype, Operationtype, inputtext):
    try:
        if objtype in ("BUTTON", "CBOX", "LINK", "RADIO", "IMAGE"):
            if Operationtype == "CLICK":
                if objidtype == "ID":
                    element = driver.find_element_by_id(objid)
                    element.click()
                elif objidtype == "CSS_SELECTOR":
                    element = driver.find_element_by_css_selector(objid)
                    element.click()
                elif objidtype == "CLASS_NAME":
                    element = driver.find_elements_by_class_name(objid)
                    element.click()
                elif objidtype == "XPATH":
                    element = driver.find_element_by_xpath(objid)
                    element.click()
                elif objidtype == "TAGNAME":
                    element = driver.find_element_by_tag_name(objid)
                    element.click()
                elif objidtype == "NAME":
                    element = driver.find_element_by_name(objid)
                    element.click()
        elif objtype in ("LCBOX"):
            if Operationtype == "CLICK":
                if objidtype == "ID":
                    element = driver.find_element_by_id(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
                elif objidtype == "CSS_SELECTOR":
                    element = driver.find_element_by_css_selector(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
                elif objidtype == "CLASS_NAME":
                    element = driver.find_elements_by_class_name(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
                elif objidtype == "XPATH":
                    element = driver.find_element_by_xpath(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
                elif objidtype == "TAGNAME":
                    element = driver.find_elements_by_tag_name(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
                elif objidtype == "NAME":
                    element = driver.find_elements_by_name(objid)
                    for x in range(0, len(element)):
                        if element[x].is_displayed():
                            element[x].click()
        elif objtype == "TEXT":
            if Operationtype == "CLICK":
                if objidtype == "ID":
                    element = driver.find_element_by_id(objid)
                    element.click()
                elif objidtype == "CSS_SELECTOR":
                    element = driver.find_element_by_css_selector(objid)
                    element.click()
                elif objidtype == "CLASS_NAME":
                    element = driver.find_element_by_class_name(objid)
                    element.click()
                elif objidtype == "XPATH":
                    element = driver.find_element_by_xpath(objid)
                    element.click()
                elif objidtype == "TAGNAME":
                    element = driver.find_element_by_tag_name(objid)
                    element.click()
                elif objidtype == "NAME":
                    element = driver.find_element_by_name(objid)
                    element.click()
            elif Operationtype == "TYPE":
                if objidtype == "ID":
                    driver.find_element_by_id(objid).send_keys(inputtext)
                elif objidtype == "CSS_SELECTOR":
                    driver.find_element_by_css_selector(objid).send_keys(inputtext)
                elif objidtype == "CLASS_NAME":
                    driver.find_element_by_class_name(objid).send_keys(inputtext)
                elif objidtype == "XPATH":
                    driver.find_element_by_xpath(objid).send_keys(inputtext)
                elif objidtype == "TAGNAME":
                    driver.find_element_by_tag_name(objid).send_keys(inputtext)
                elif objidtype == "NAME":
                    driver.find_element_by_name(objid).send_keys(inputtext)
        elif objtype == "LIST":
            listitem = inputtext
            if Operationtype == "CLICK":
                if objidtype == "ID":
                    element = driver.find_element_by_id(objid)
                    for option in element.find_elements_by_tag_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
                elif objidtype == "CSS_SELECTOR":
                    element = driver.find_element_by_css_selector(objid)
                    for option in element.find_elements_by_tag_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
                elif objidtype == "CLASS_NAME":
                    element = driver.find_element_by_class_name(objid)
                    for option in element.find_elements_by_tag_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
                elif objidtype == "XPATH":
                    element = driver.find_element_by_xpath(objid)
                    for option in element.find_elements_by_tag_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
                elif objidtype == "TAGNAME":
                    element = driver.find_element_by_tag_name(objid)
                    for option in element.find_elements_by_tag_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
                elif objidtype == "NAME":
                    element = driver.find_element_by_name(objid)
                    for option in element.find_elements_by_name('option'):
                        if option.text == listitem:
                            option.click()
                            break
        elif objtype == "LISTBOX":
            listitem = inputtext
            if Operationtype == "SELECT":
                if objidtype == "ID":
                    select = Select(driver.find_element_by_id(objid))
                    select.select_by_visible_text(listitem)
                elif objidtype == "CSS_SELECTOR":
                    select = Select(driver.find_element_by_css_selector(objid))
                    select.select_by_visible_text(listitem)
                elif objidtype == "CLASS_NAME":
                    select = Select(driver.find_element_by_class_name(objid))
                    select.select_by_visible_text(listitem)
                elif objidtype == "XPATH":
                    select = Select(driver.find_element_by_xpath(objid))
                    select.select_by_visible_text(listitem)
                elif objidtype == "TAGNAME":
                    select = Select(driver.find_element_by_tag_name(objid))
                    select.select_by_visible_text(listitem)
                elif objidtype == "NAME":
                    select = Select(driver.find_element_by_name(objid))
                    select.select_by_visible_text(listitem)
    except Exception as e:
        print(e)
        raise e


def waitobject(objidtype, objid, waittime):
    try:
        if objidtype == "ID":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.ID, objid)))
            return (element)
        elif objidtype == "CSS_SELECTOR":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, objid)))
            return (element)
        elif objidtype == "CLASS_NAME":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, objid)))
            return (element)
        elif objidtype == "XPATH":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, objid)))
            return (element)
        elif objidtype == "TAG_NAME":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, objid)))
            return (element)
        elif objidtype == "NAME":
            wait = WebDriverWait(driver, waittime)
            element = wait.until(EC.element_to_be_clickable((By.NAME, objid)))
            return (element)
    except Exception as e:
        print(e)
        raise e


def WaitForObjectToDisapper(objidtype, objid, waittime):
    try:
        if objidtype == "ID":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.ID, objid)))
        elif objidtype == "CSS_SELECTOR":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, objid)))
        elif objidtype == "CLASS_NAME":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, objid)))
        elif objidtype == "XPATH":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.XPATH, objid)))
        elif objidtype == "TAG_NAME":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.TAG_NAME, objid)))
        elif objidtype == "NAME":
            wait = WebDriverWait(driver, waittime)
            wait.until_not(EC.visibility_of_element_located((By.NAME, objid)))
    except Exception as e:
        print(e)
        raise e


def generate_rendom_name_with_Number(length):
    range_begin = 10 ** (length - 1)
    range_end = (10 ** length) - 1
    randnum = randint(range_begin, range_end)
    return 'Test' + str(randnum)


def findsystemdate():
    i = datetime.datetime.now()
    datetoday = ("%s/%s/%s" % (i.day, i.month, i.year))
    return (datetoday)


def closeexecution():
    driver.quit()


def generatefilename():
    with open('prereq.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    filename = doc["EnvironmentDetails"]["reportfile"]
    if os.path.exists(filename) == True:
        os.rename(filename, filename + ".old")
        datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        if platform.uname().processor.find('Intel64') != -1:
            osarch = "64bit"
        else:
            osarch = "32bit"
        Newfilename = (str(platform.platform()) + "-" + str(osarch) + "-" + str(datetoday) + ".txt")
        print("NewFileName: " + Newfilename)
        with open("prereq.yml") as f:
            doc = yaml.load(f,Loader=yaml.FullLoader)
            Path = doc["EnvironmentDetails"]["dirpath"]
            doc["EnvironmentDetails"]["reportfile"] = str(Path) + str(Newfilename)
            with open('prereq.yml', 'w') as f:
                yaml.dump(doc, f)
    else:
        datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        if platform.uname().processor.find('Intel64') != -1:
            osarch = "64bit"
        else:
            osarch = "32bit"
        Newfilename = (str(platform.platform()) + "-" + str(osarch) + "-" + str(datetoday) + ".txt")
        print("NewFileName: " + Newfilename)
        with open("prereq.yml") as f:
            doc = yaml.load(f)
            Path = doc["EnvironmentDetails"]["dirpath"]
            doc["EnvironmentDetails"]["reportfile"] = str(Path) + str(Newfilename)
            with open('prereq.yml', 'w') as f:
                yaml.dump(doc, f)


def trucatereportfile():
    with open('prereq.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    filename = doc["EnvironmentDetails"]["reportfile"]
    if os.path.exists(filename) == True:
        fileopen = open(filename, "w+")
        fileopen.truncate()
        fileopen.close()
        datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        createreport("Test Execution Started " + str(datetoday))
    else:
        fileopen = open(filename, "w+")
        fileopen.truncate()
        fileopen.close()
        datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        createreport("Test Execution Started " + str(datetoday))


def executionstarttime():
    global starttime
    starttime = datetime.datetime.now()
    print("Test Execution Start Time : " + str(starttime))


def executionendtime():
    ExecutionTime = datetime.datetime.now() - starttime
    ExecutionTime = str(ExecutionTime).split(".")
    ExecutionTime = str(ExecutionTime[0]).split(":")
    createreport("************************* Automation Text Execution Time *************************************")
    createreport("Total Time for Automation Execution is : " + str(ExecutionTime[0]) + "-Hours " + str(
        ExecutionTime[1]) + "-Minutes " + str(ExecutionTime[2]) + "-Seconds")


def createreport(text):
    with open('prereq.yml', 'r') as f:
        doc = yaml.load(f,Loader=yaml.FullLoader)
    filename = doc["EnvironmentDetails"]["reportfile"]
    if os.path.exists(filename) == True:
        fileopen = open(filename, "a+")
        fileopen.write(text)
        fileopen.write("\n")
    else:
        fileopen = open(filename, "a+")
        fileopen.write(text)
        fileopen.write("\n")


def closeexecutionfailure():
    takescreenshot("FAIL")
    driver.quit()
    datetoday = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    createreport("Test Execution Completed " + str(datetoday))
    executionendtime()
    sys.exit()


def WaitForBrowserTitleDisplay(text, delay):
    titletext = str(text)
    WebDriverWait(driver, delay).until(
        EC.title_is((titletext)))



