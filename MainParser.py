import os

from selenium import webdriver

from BaseParser import getHrefsJobs, getUrls, writeResToFile
from HrefParser import writeUrlsToFile, getHrefsJobsFromFile

phantomjs_path = "D:\phantomjs.exe"
chromedriver_path = "D:\chromedriver.exe"

#driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
driver = webdriver.Chrome(executable_path=chromedriver_path, service_log_path=os.path.devnull)

baseUrl = 'https://geo.craigslist.org/iso/us/'

listOfStates = [['Alabama', 'AL'], ['Alaska', 'AK'], ['Arizona', 'AZ'], ['Arkansas', 'AR'], ['California', 'CA'], ['Colorado', 'CO'], [ 'Connecticut', 'CT'],
                ['Delaware', 'DE'], ['Florida', 'FL'], ['Georgia', 'GA'], ['Hawaii', 'HI'], ['Idaho', 'ID'], ['Illinois', 'IL'], ['Indiana', 'IN'], ['Iowa', 'IA'],
                ['Kansas', 'KS'], ['Kentucky[E]', 'KY'], ['Louisiana', 'LA'], ['Maine', 'ME'], ['Maryland', 'MD'], ['Massachusetts', 'MA'], ['Michigan', 'MI'],
                ['Minnesota', 'MN'], ['Mississippi', 'MS'], ['Missouri', 'MO'], ['Montana', 'MT'], ['Nebraska', 'NE'], ['Nevada', 'NV'], ['New Hampshire', 'NH'],
                ['New Jersey', 'NJ'], ['New Mexico', 'NM'], ['New York', 'NY'], ['North Carolina', 'NC'], ['North Dakota', 'ND'], ['Ohio', 'OH'], ['Oklahoma', 'OK'],
                ['Oregon', 'OR'], ['Pennsylvania[G]', 'PA'], ['Rhode Island[H]', 'RI'], ['South Carolina', 'SC'], ['South Dakota', 'SD'], ['Tennessee', 'TN'],
                ['Texas', 'TX'], ['Utah', 'UT'], ['Vermont', 'VT'], ['Virginia[I]', 'VA'], ['Washington', 'WA'], ['West Virginia', 'WV'], ['Wisconsin', 'WI'],
                ['Wyoming', 'WY']]

listOfStates = [['Alabama', 'AL'], ['Alaska', 'AK'], ['Arizona', 'AZ'], ['Arkansas', 'AR'], ['California', 'CA'], ['Colorado', 'CO'], [ 'Connecticut', 'CT'],
                 ['Florida', 'FL'], ['Georgia', 'GA'], ['Idaho', 'ID'], ['Illinois', 'IL'], ['Indiana', 'IN'], ['Iowa', 'IA'],
                ['Kansas', 'KS'], ['Kentucky[E]', 'KY'], ['Louisiana', 'LA'], ['Maryland', 'MD'], ['Massachusetts', 'MA'], ['Michigan', 'MI'],
                ['Minnesota', 'MN'], ['Mississippi', 'MS'], ['Missouri', 'MO'], ['Montana', 'MT'], ['Nebraska', 'NE'], ['Nevada', 'NV'],
                ['New Jersey', 'NJ'], ['New Mexico', 'NM'], ['New York', 'NY'], ['North Carolina', 'NC'], ['North Dakota', 'ND'], ['Ohio', 'OH'], ['Oklahoma', 'OK'],
                ['Oregon', 'OR'], ['Pennsylvania[G]', 'PA'], ['South Carolina', 'SC'], ['South Dakota', 'SD'], ['Tennessee', 'TN'],
                ['Texas', 'TX'], ['Utah', 'UT'], ['Virginia[I]', 'VA'], ['Washington', 'WA'], ['West Virginia', 'WV'], ['Wisconsin', 'WI']]

setOfHrefsRegion = ['https://sfbay.craigslist.org/', 'https://losangeles.craigslist.org/', 'https://newyork.craigslist.org/',
                    'https://chicago.craigslist.org/', 'https://miami.craigslist.org/', 'https://montreal.craigslist.ca/',
                    'https://seattle.craigslist.org/', 'https://toronto.craigslist.ca/', 'https://vancouver.craigslist.ca/',
                    'https://washingtondc.craigslist.org/', 'https://boston.craigslist.org/']

setOfHrefsRegion = ['https://sfbay.craigslist.org/', 'https://losangeles.craigslist.org/', 'https://newyork.craigslist.org/',
                    'https://chicago.craigslist.org/', 'https://miami.craigslist.org/', 'https://montreal.craigslist.ca/',
                    'https://seattle.craigslist.org/', 'https://toronto.craigslist.ca/', 'https://vancouver.craigslist.ca/',
                    'https://washingtondc.craigslist.org/', 'https://boston.craigslist.org/']

setOfHrefsJobsWebInfoDesign = {}

param = 'software-qa-dba-etc/search/sof'
keyWords = ['react']
keyWords = ['urgent*', 'quick*', 'immediate*', 'full stack', 'fullstack', 'fullstack*', 'java', 'spring boot', 'front end', 'react*', 'react', 'google-map',
            'google-map*', 'googlemap*', 'googlemap', 'oauth', 'jwt', 'rest assured', 'cryptocur*']
#writeUrlsToFile(listOfStates, driver, baseUrl, setOfHrefsRegion)
#setOfHrefsJobsSoftwareDbQa = getUrls(listOfStates, driver, baseUrl, setOfHrefsRegion)
setOfHrefsJobsSoftwareDbQa = getHrefsJobsFromFile()
setOfJobsHrefsSoftwareDbQa = getHrefsJobs(driver, keyWords, param, setOfHrefsJobsSoftwareDbQa)
writeResToFile(driver, param, setOfJobsHrefsSoftwareDbQa, keyWords)



driver.close()

# fileName = 'Manufacturing'
# listFromFile = parseXlsxForIcGc(fileName)
# #listFromFile = removeAndSortRepeatedElements(listFromFile, fileName)
# addDescToXlsx(driver, listFromFile, fileName)




#Цикл for используется для повторения чего-нибудь n-ное количество раз

#В основном этот опереатор используют по умолчнаию, т к  он выполняется гораздо быстрее цикла while.

# Этот цикл производит итерацию по строке, кортежу, списку(например строке или Кортежу(содержит любой неизменяемый тип данных), словари(в качестве итерируемого объекта - мы получим ключи), списки(изменяемые)),

#Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)

#Оператор break досрочно прерывает цикл.

# for i in listFromFile:
#     print("111 " + str(i))

# a_dict = {"one": 1, "two": 2, "three": 3}
# #
# # for key in a_dict:
# #     print(key)
# #
# for i in range(1, 10, 3):
#    print(i)
#
# # for i in 10:
# #     print(i)
#
# for i in "hallo":
#     print('asdsds')
#
#     #driver.close()