# WhatsApp-Bot
WhatsApp Bot is a Python-based chatbot for WhatsApp to automate the process of sending messages to one or more person or a group.

## Steps:

1. Clone the repository on your local machine.

2. Install `Selenium` and `Schedule` packages in Python using the following commands:
   - `pip install selenium`
   - `pip install schedule`
   
3. Open the `whatsapp_bot.py` file and edit **Line 43** by replacing `<your_user_name>` with the username of your machine. Also edit **Line 46** by replacing `<path_to_chromedriver.exe>` with the actual path of `chromedriver.exe` on your machine.

4. Once all the setup is done, run the command `python whatsapp_bot.py`.


**Note:** 
- The `whatsapp_bot.py` code is subject to change with different versions of Google Chrome. The current code is compatible for Chrome version 88 only and the corresponding [Chrome Driver](https://github.com/NSTiwari/WhatsApp-Bot/blob/main/chromedriver.exe) is included in the repository.

- For a different version, download Chrome Driver from [here](https://chromedriver.chromium.org/downloads).

## Output:

With this application, you can do the following interesting things:
- Send message to a person or a group.
- Schedule a message at a given time to a person or a group.
- Automated reply to unread messages.


### Send a message.

![GitHub Logo](/screenshots/cmd_send_message.png)

![GitHub Logo](/screenshots/send_message.png)



### Schedule a message.

![GitHub Logo](/screenshots/cmd_schedule_message.png)

![GitHub Logo](/screenshots/schedule_message.png)



### Reply to unread messages.

![GitHub Logo](/screenshots/cmd_reply_unread_message.png)

![GitHub Logo](/screenshots/reply_unread_message.png)

