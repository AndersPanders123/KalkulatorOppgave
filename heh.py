# Packages

from pynput.keyboard import Listener, Key
from threading import Thread
from os import _exit, system
from msvcrt import getch



# Functions

def clear(): system("cls")

def is_operator(char: str):
    return char in ["+", "-", "*", "/"]

def is_int(char: str):
    try:
        int(char)
        return True
    except: return False

def merge_numbers(chars: list[str]):
    formatted = chars
    pre_result = [""]
    for i in formatted:
        if is_operator(pre_result[-1]):
            pre_result.append("")
        if is_operator(i):
            pre_result.append(i)
        if not is_operator(pre_result[-1]) and not is_operator(i):
            pre_result[-1] += i
    post_result = []
    for i in pre_result:
        try: post_result.append(int(i))
        except: post_result.append(i)
    return post_result

def calculate(chars: list[str]):
    formatted = chars
    if is_operator(formatted[-1]):
        formatted = formatted[:-1]
    formatted = merge_numbers(formatted)
    result = formatted[0]
    for i in range(1, len(formatted), 2):
        match formatted[i]:
            case "+": result += formatted[i + 1]
            case "-": result -= formatted[i + 1]
            case "*": result *= formatted[i + 1]
            case "/": result /= formatted[i + 1]
    print(result)



# Main

chars = []

def format_chars(): return " ".join(chars)

clear()
print("Start typing your problem...")

def external_listener():
    global chars
    def on_press(key):
        global chars
        if key == Key.esc:
            print("Quit calculator!")
            _exit(0)
        elif key == Key.enter:
            calculate(chars)
            _exit(0)
        elif key == Key.backspace and len(chars) > 0:
            chars = chars[:-1]
            clear()
            print(format_chars() + "\n\tEnter a number or an operator...")

    with Listener(on_press=on_press) as listener:
        listener.join()

Thread(target=external_listener).start()

while True:
    char = getch().decode()
    if not is_int(char) and not is_operator(char):
        continue
    if is_operator(char) and is_operator(chars[-1]):
        continue
    if is_operator(char) and len(chars) == 0:
        continue
    chars.append(char)
    clear()
    print(format_chars() + "\n\tEnter a number or an operator...")