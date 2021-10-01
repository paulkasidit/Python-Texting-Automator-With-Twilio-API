# Python-Texting-Automator-With-Twilio-API
A program that automates texting at regular intervals via the Twilio API. You have a selection of times availble in eith morning or evening. 

Setup
--------
1. Setup a free Twilio account and obtain your account token and account sid. The program will not work without it. 
2. In your "twilio_credentials.py" input this information in the fields. 

- "cellphone" (number you want to send the text to).
- "twilio_number" (number that comes with your twilio account)
- twilio_account" (twilio account sid)  *SECRET
- "twilio token" (your twilio account token, which can be found in the account settings.) *SECRET 

3. Setup complete

Installation
--------------
- In the program directory run the folowing Terminal Command:

pip install -r requirements.tx

Running the program
--------------------

- In the program directory run the folowing Terminal Command:

python3 automate_texting.py 
