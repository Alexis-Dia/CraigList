from selenium import webdriver
import os

from BaseParser import getUrls, createFile, savePageData, readFile

phantomjs_path = "D:\phantomjs.exe"
chromedriver_path = "D:\chromedriver.exe"

#driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
driver = webdriver.Chrome(executable_path=chromedriver_path, service_log_path=os.path.devnull)

fileName = 'listOfHrefs'
def writeUrlsToFile(listOfStates, driver, baseUrl, setOfHrefsRegion):
    setOfHrefsJobsSoftwareDbQa = getUrls(listOfStates, driver, baseUrl, setOfHrefsRegion)
    createFile(fileName)
    for i in setOfHrefsJobsSoftwareDbQa:
        savePageData(fileName, i, '', '')

def getHrefsJobsFromFile():
    return readFile(fileName)