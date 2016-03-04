# reading firms.csv file
import os
import datetime
import csv
reading=open('firms.csv','rb')
writing=open('firms_status.csv','a')
reader=csv.reader(reading)
writer=csv.writer(writing, delimiter=',')

# reading cover letter
cover_file=open('cover_letter.txt','r')
cover=cover_file.read()

# selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# driver=webdriver.Chrome(executable_path=r'H:\Chrome downloads\chromedriver_win32\chromedriver.exe')
driver=webdriver.Firefox()
driver.get("http://www.gmail.com")
element=driver.find_element_by_id("Email")
element.send_keys(<username>, Keys.RETURN) # username
driver.implicitly_wait(2)
element=driver.find_element_by_id("Passwd") #password
element.send_keys(<password>, Keys.RETURN)
driver.implicitly_wait(10)

rep='y'# getting inputs from user
no_mails=0
while(rep=='y'):
	
	os.system('cls')
	# **** composing email for each firm ****
	driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3").click()   # compose button
	email_id=raw_input("Enter email-id\n")
	name=raw_input("Enter name\n")
	driver.implicitly_wait(2)
	driver.find_element_by_name("to").send_keys(email_id)  # recipient
	driver.find_element_by_name("subjectbox").send_keys("Application for Internship")  #subject
	cover.replace('CV','\033[1m'+'CV'+'\033[0m')
	driver.find_element_by_css_selector(".Am.Al.editable.LW-avf").send_keys(cover.replace('archi_firm',name))  # email content

	# **** attaching  files **** 
	driver.find_element_by_css_selector(".a1.aaA.aMZ").click()  
	os.system('uploadcv.exe') #uploading cv
	driver.find_element_by_css_selector(".a1.aaA.aMZ").click()
	os.system('uploadport.exe') #uploading portfolio

	time.sleep(10)
	driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3").click()
	writer.writerow([email_id,name,'sent',str(datetime.date.today())])
	no_mails+=1
	rep=raw_input("Want to continue ?")
	if rep=='n':
		print 'You have sent '+str(no_mails) +' mails'


writing.close()


# compose.send_keys(Keys.RETURN)
