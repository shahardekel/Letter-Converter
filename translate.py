#!/Users/shahardekel/opt/anaconda3/bin/python3

import keyboard
import pyperclip
from langdetect import detect, detect_langs
import sys
from langdetect.lang_detect_exception import LangDetectException #adding handling with exceptions

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


# Main function- handling with 'enter' and unknown keys
def main():
    # Try reading input from stdin
    selected_text = sys.stdin.read().strip() if not sys.stdin.isatty() else None

    # Fallback to clipboard if stdin is empty or not piped
    # handles with 'enter' key
    if not selected_text:
        print("No input from stdin. Falling back to clipboard content.")
        try:
            selected_text = pyperclip.paste().strip()
        except Exception as e:
            print(f"Error reading from clipboard: {e}. Try row by row converting")
            return

    # Check if input is still empty
    if not selected_text:
        print("No text available for translation.")
        return

    # Translate the input text
    try:
        translated_text = translate_key(selected_text)
        print(translated_text)
        pyperclip.copy(translated_text)
    except Exception as e:
        print(f"Error during translation: {e}. Try row by row converting")

if __name__ == "__main__":
    main()
