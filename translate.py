#!/Users/shahardekel/opt/anaconda3/bin/python3

import keyboard
import pyperclip
from langdetect import detect, detect_langs
import sys

eng_to_heb = {
    'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק',
    'f': 'כ', 'g': 'ע', 'h': 'י', 'i': 'ן', 'j': 'ח',
    'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ', 'o': 'ם',
    'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א',
    'u': 'ו', 'v': 'ה', 'w': '׳', 'x': 'ס', 'y': 'ט',
    'z': 'ז', ',': 'ת', '.': 'ץ', ';': 'ף', ' ': ' ', 
    '[': ']', ']': '[', '-': '-', '=': '=','/':'.'
}

heb_to_eng = {value: key for key, value in eng_to_heb.items()}

def detect_lang(key):
    if not key or all(char in "!?@#$%^&*()_+{}|\\<> 0123456789" for char in key):
        return 'symbol'
    elif key=='׳':
        return 'w'
    elif key=="'":
        return ','
    elif key==',':
        return 'ת'
    elif key=='״' or key=='"':
        return '"'
    elif key=='/':
        return '.'
    else: 
        return detect(key)

def translate_key(key):
    new_key=''
    for l in key:
        #print(l)
        if detect_lang(l)=='he':
            new_key+=heb_to_eng[l]
        elif detect_lang(l)=='w':
            new_key+='w'
        elif detect_lang(l)=='"':
            new_key+='"'
        elif detect_lang(l)==",":
            new_key+=','
        elif detect_lang(l)=='symbol':
            new_key+=l
        else:
            
            new_key+=eng_to_heb[l.lower()]

    return new_key


def main():
    # Read selected text from stdin
    selected_text = sys.stdin.read().strip()
    if not selected_text:
        print("No text selected.")
        return

    # Translate the text
    translated_text = translate_key(selected_text)

    # Output translated text to stdout
    print(translated_text)

if __name__ == "__main__":
    main()
