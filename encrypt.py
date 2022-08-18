# Imports
from cryptography.fernet import Fernet
import base64
from tkinter import *
import tkinter.messagebox as box
import os
import sys

#Resource Path Script
def resource_path(relative_path):
	absolute_path = os.path.abspath(__file__)
	root_path = os.path.dirname(absolute_path)
	base_path = getattr(sys, '_MEIPASS', root_path)
	return os.path.join(base_path, relative_path)

window = Tk() # Create window
window.title('Magnus Encryptor') # Title Window
window.geometry('700x300') # Set the Window width and height
window.iconbitmap(resource_path('icon.ico')) # Set Window Icon

label_result = Text(window, height = 10, borderwidth = 3) # Create result label

msg_entry = Entry(window) # Create message entry

key_entry = Entry(window) # Create key entry

def tog():

	key = str(key_entry.get()) # Get key from entry

	label_result.config(state = 'normal')

	if len(key) != 32: # Check if key doesn't have 32 digits
		box.showerror('Magnus Encryptor', 'Key Must Have 32 Digits Exactly')
	else:

		try:

			cipher_suite = Fernet(base64.urlsafe_b64encode(bytes(key, 'utf-8'))) # Make Cipher "Object" With Custom Key and encode it with base64 (Must be bytes)
			
			message = str(msg_entry.get()) # Get Message from entry

			encoded_text = cipher_suite.encrypt(bytes(message, 'utf-8')) # Encrypt the string

			label_result.delete('1.0', 'end') # Delete any old text

			label_result.insert(1.0, 'Encrypted Text: ' + encoded_text.decode('utf-8')) # Save Final Result To Label
			label_result.config(state = 'disabled') # configure textbox to readonly
		except:
			box.showerror('Magnus Encryptor', 'Key Invalid') #If any error occurs show this


encrypt_button = Button(window, text = 'Encrypt', command = tog) # Create Decrypt Buttton

msg_entry_label = Label(window, text = 'Message:') # Create Message Entry Label
key_entry_label = Label(window, text = 'Key:') # Create Key Entry Label

# Pack Everything
key_entry_label.pack(side = TOP)
key_entry.pack(side = TOP)
msg_entry_label.pack(side = TOP)
msg_entry.pack(side = TOP)
encrypt_button.pack(side = TOP, pady = 5)
label_result.pack(side = TOP)

# Window Mainloop
window.mainloop()