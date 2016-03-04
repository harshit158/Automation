import time
import csv
import os
import sys
import datetime
import random
from helium.api import *
#opening file for writing
country='gurgaon'
reading=open(country,'rb')
# reader=csv.reader(reading)
writing=open('firms_status','a')
# writer=csv.writer(writing, delimiter=',')
cover_file=open('cover_letter.txt','r')
cover=cover_file.read()

start_chrome()
# go_to('https://chrome.google.com/webstore/detail/contactmonkey-email-analy/dlppikdhbkdinhpfbneekdbjhgphknad')
# click('ADD TO CHROME')
# press(LEFT)
# press(ENTER)
#click(Button('Add Extension'))
go_to("gmail.com")
click("Sign in")
write(<username>, into="Enter your email")
press(ENTER)
write(<password>, into="Password")
press(ENTER)

def send_message(email_id, name):
	click(Button("COMPOSE"))
	write(email_id, into=TextField(to_right_of="To"))
	write("Application for Internship", into="Subject")
	press(TAB)
	write(cover.replace('archi_firm',name))
	drag_file('C:\Users\HS\Desktop\int\CV.pdf', to="Drop files here")
	drag_file('C:\Users\HS\Desktop\int\Portfolio.pdf', to="Drop files here")
	click("Send")
	wait_until(Text("Your message has been sent.").exists, timeout_secs=120)



no_mails=0
choice=raw_input("1.Manually\n2.From file\n")
if choice=='1':

	rep='y'# getting inputs from user
	
	while(rep=='y'):
		os.system('cls')
		if no_mails%10==9:
			random_time=random.randrange(300,360)
			print '\nsleeping for '+str(random_time)+' seconds'
			time.sleep(random_time)
		email_id=raw_input("Enter email-id\n")
		name=raw_input("Enter name\n")
		print str(no_mails+1)+'. Sending mail to '+name+' ......'
		send_message(email_id, name)
		print '   Sent'
		writing.write(country+'\t'+email_id+'\t'+name+'\t'+ str(datetime.date.today())+'\n')
		# writer.writerow([email_id,name,'sent',str(datetime.date.today())])
		no_mails+=1
		rep=raw_input("Want to continue ?")
		if rep=='n':
			print 'You have sent '+str(no_mails) +' mails'
		
	

elif choice=='2':
	os.system('cls')
	for line in reading:
		if no_mails%10==9:
			random_time=random.randrange(300,360)
			print '\nsleeping for '+str(random_time)+' seconds'
			time.sleep(random_time)
		splitted=line.split('\t')
		email_id=splitted[0].strip()
		name=splitted[1].strip()
		print str(no_mails+1)+'. Sending mail to '+name+' ......'
		send_message(email_id, name)
		print '   Sent'
		writing.write(country+'\t'+email_id+'\t'+name+'\t'+ str(datetime.date.today())+'\n')
		# writer.writerow([email_id,name,'sent',str(datetime.date.today())])
		no_mails+=1
	print 'You have sent '+str(no_mails) +' mails'

#writing.close()
#reading.close()


