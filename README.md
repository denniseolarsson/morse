# morse
Python functions for practicing morse code

This script is meant to be used for practicing morse code, and translating text to code and code to text. 

The script uses dots ('.') and dashes ('-') for short and long signals respectively. Blank spaces between strings are coded as three blank spaces when translated to morse code.
Morse code is played as sequence of short and long tones. 

Words used in the practice function are read from a .txt file called "wordlist" saved in the same folder as the main script. Words can freely be added or removed from this list. The list of words is saved as the list variable "wordlist"
Sentences are read from "sentencelist.txt" and saved as the list variable "sentencelist"

Run each function by calling them in the command line. 
Available functions: 


>>> morse_play(string)

Plays input string variable (e.g. 'hello world')



>>> morse_code(string)

Prints morse code corresponding to input string variable (e.g. 'hello world')



>>> morse_translate(string)

Prints text translation of input string varible (e.g. '.... . .-.. .-.. ---')



>>> morse_practice()

Runs practice function, where you can ask it to pick and play the morse code of (1) a random word from the wordlist variable, (2) a random sentece from the sentencelist variable, or (3) a random sequence of four numbers. 


>>> morse_settings()

Options to change morse signal speed (three settings) and pitch (Hz)
