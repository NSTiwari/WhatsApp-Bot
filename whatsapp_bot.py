import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import schedule



def new_chat(user_name):
	time.sleep(2)
	new_chat = chrome_browser.find_element_by_xpath('//div[@class="_22PcK"]')
	new_chat.click()

	new_user = chrome_browser.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
	new_user.send_keys(user_name)
	time.sleep(2)

	try:
		user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
		user.click()
	except NoSuchElementException: 
		print('Given user "{}" not found in the contact list'.format(user_name))
	except Exception as e:
		chrome_browser.close()
		#print(e)
		sys.exit()

def send_message():
	message_box = chrome_browser.find_element_by_xpath('//div[@class="DuUXI"]')
	time.sleep(4)
	message_box.send_keys("Hi {}, I am WhatsApp Bot. This is a scheduled message for you at {}".format(user_name.split()[0],scheduled_time)+Keys.ENTER)

def hasxpath(xpath):
    	try:
        	chrome_browser.find_element_by_xpath(xpath)
        	return True
    	except:
        	return False

if __name__=="__main__":
	options=webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=C:/Users/<your_user_name>/AppData/Local/Google/Chrome/User Data/Default')
	options.add_argument('--profile-directory=Default')

	chrome_browser=webdriver.Chrome(executable_path = '<path_to_chromedriver.exe>', options=options)
	chrome_browser.get('https://web.whatsapp.com/')
	time.sleep(15)

	print()
	print("1. Send message to a person or a group: ")
	print("2. Schedule a message to a person or a group: ")
	print("3. Reply to unread messages: ")
	print()
	choice=int(input("What do you want to do?: "))

	if(choice==1):
		user_name_list = []
		print()
		print()
		n=int(input("Enter the no. of users you want to send the message to: "))
		for i in range(n):
			user=input("User"+str(i+1)+":")
			user_name_list.append(user)

		for user_name in user_name_list:
			try:
				user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
				user.click()
			except NoSuchElementException as se:
				new_chat(user_name)

				# Typing message into message box
			#message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
			message_box = chrome_browser.find_element_by_xpath('//div[@class="DuUXI"]')
			msg = input("Enter your message: ")
			message_box.send_keys(msg+Keys.ENTER)
			# message_box.send_keys('Hello, I am WhatsApp bot. '+Keys.ENTER)
			time.sleep(1)
				#message_box = chrome_browser.find_element_by_xpath('//div[@class="_1JNuk"]')
				#message_box.click()
			time.sleep(5)
	 
	elif(choice==2):
	 user_name_list = []
	 print()
	 n=int(input("Enter the no. of users you want to send the message to: "))
	 for i in range(n):
	 	user=input("User"+str(i+1)+":")
	 	user_name_list.append(user)

	 scheduled_time = input("Enter the time at which you want to send the message: ")

	 for user_name in user_name_list:
	 	try:
	 		user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
	 		user.click()
	 	except NoSuchElementException as se:
	 		new_chat(user_name)

	 	time.sleep(2)
	 	schedule.every().day.at(scheduled_time).do(send_message) 

	 	while True: 

	 				    # Checks whether a scheduled task  
	 				    # is pending to run or not 
	 		schedule.run_pending() 
	 		time.sleep(1) 


	elif(choice==3):
	 unreadMsgs = chrome_browser.find_elements_by_xpath('//span[@class="VOr2j"]')
	 if hasxpath('//img[@class="_3t3gU rlUm6 _1VzZY"]') == True :
	  propic = chrome_browser.find_element_by_xpath('//img[@class="_3t3gU rlUm6 _1VzZY"]')
	  propic.click()
	 else:
	  propic = chrome_browser.find_element_by_xpath('//span[@data-icon="default-user"]')
	  propic.click()
	 sender = chrome_browser.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
	 if not unreadMsgs:
	 	print("Total unread messages: 0")
	 else:
	 	print("Total unread messages: "+ str(len(unreadMsgs)))
	 	text = "Hi, I am WhatsApp Bot. {} is out on a date right now, he'll get back to you soon. Meanwhile, you too find someone for yourself."
	 	# text = "Heyyy"
	 	for msg in unreadMsgs:
	 		msg.click()
	 		time.sleep(5)
	 		message_box=chrome_browser.find_element_by_xpath('//div[@class="DuUXI"]')
	 		message_box.send_keys(text.format(sender.text)+Keys.ENTER)

	
	 	






	 	


	 	