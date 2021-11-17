# MORSE CODE PROGRAM
# 

import winsound, time, random

global morse_signal_speed
global morse_signal_speed_options
global morse_signal_speed_options_strings
global dur_short
global dur_long
global morse_pitch

## Morse keys;
# key1: list of available character symbols
key1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.',',','?']
# key2: list of morse sequence corresponding to character symbols in key1. s = short ("."); l = long ("-")
key2 = ['sl','lsss','lsls','lss','s','ssls','lls','ssss','ss','slll','lsl','slss','ll','ls','lll','slls','llsl','sls','sss','l','ssl','sssl','sll','lssl','lsll','llss','sllll','sslll','sssll','ssssl','sssss','lssss','llsss','lllss','lllls','lllll','slslsl','llssll','ssllss']


with open("wordlist.txt") as f:
    wordlist = []
    for line in f:
        wordlist.append(line.strip())
   
        
with open("sentencelist.txt") as f:
    sentencelist = []
    for line in f:
        sentencelist.append(line.strip())


# Speed of signal played [short, long]
speed_low    = [200, 600]
speed_medium = [150, 450]
speed_high   = [100, 300]

morse_signal_speed      = speed_medium
dur_short  = morse_signal_speed[0]
dur_long   = morse_signal_speed[1]

morse_signal_speed_options         = [speed_low, speed_medium, speed_high]
morse_signal_speed_options_strings = ['low', 'medium', 'high'] 

morse_pitch = 600
#morse_pitch = 650

# Examples
example_string = 'morse code'
example_code = '-- --- .-. ... .   -.-. --- -.. . '
word = random.choice(wordlist)

str_mainMenu = '''
Available morse code functions:
morse_play(string)      -   play morse code of string
morse_code(string)      -   print morse code of string 
morse_translate(string) -   print translation of morse code string
morse_practice()        -   practice deciphering code
morse_settings()        -   change signal speed or pitch
'''
## Print instructions
print(str_mainMenu)

## Play function
# Plays morse code sequence associated with input string
def morse_play(string): # input string
    play_done = False
    for char in string: # for each character in the string
        if char == ' ':
            time.sleep(float((dur_long*4)/1000)) # pause between words
        else:
            try: # find morse code related to character
                key = key2[key1.index(char)] 
            except ValueError: # if error, try converting symbol to lowercase and try again
                char = char.lower()
                key = key2[key1.index(char)]            
            for tone in key:
                if tone == 's': # if a dot / short, play short tone
                    #dur = 200
                    winsound.Beep(morse_pitch,dur_short)
                elif tone == 'l': # else if a beep / long, play long tone
                    winsound.Beep(morse_pitch,dur_long)
            time.sleep(float((dur_long*3)/1000)) # pause between each symbol
    play_done = True
    

## String coding function
# Translates input string to corresponding morse code 
def morse_code(string): # input string
    resp = '' # reset output string
    for char in string:
        if char == ' ':
            resp = resp+' ' # add extra space between words
        else:
            try: # find morse code related to character
                key = key2[key1.index(char)]
            except: # if error, try converting symbol to lowercase and try again
                char = char.lower()
                key = key2[key1.index(char)]
            for tone in key:
                if tone == 's': # if short, add a dot to output string
                    resp = resp+'.'
                elif tone == 'l': # else if long, add a dash to output stirng
                    resp = resp+'-'    
        resp = resp+' ' # add space between keys
    return resp # return response output string


## Code translation function
# Translates input morse code sequence to string
def morse_translate(sequence):
    sequence += ' '
    resp = ''
    sign = ''
    empty = 0
    for char in sequence:
        if char in ['.','-','s','l']:
            empty = 0
            if char == '.' or char == 's':
                sign = sign+'s'
            elif char == '-' or char == 'l':
                sign = sign+'l'
        elif char == ' ':    
            empty += 1
            try:
                signa = key1[key2.index(sign)]
                resp = resp+signa # add extra space between words  
            except:    
                if empty == 3:
                    resp = resp+' '            
            sign = ''
    return resp


## Practice deciphering code
# Choose between random word from list, or sequence of numbers
def morse_practice():
    practice_running = True
    play_done = False
    while practice_running:
        print ('''
        Morse code practice. Select your option:
        (1) Generate and play random word
        (2) Generate and play a sentence
        (3) Generate and play random number sequence
        (4) Quit''')
        option = input()
        if option == '4':
            practice_running = False
            print('Quitting practice...')
            print(str_mainMenu)
            break
        elif option in ['1','2','3']:
            if option == '1':
                word = random.choice(wordlist) # pick random word from list
            elif option == '2':
                word = random.choice(sentencelist) # pick random word from list                
            elif option == '3':
                word = n_len_rand(4, floor=1) # generate random number sequence
            word_done = False
            time.sleep(1)
            morse_play(word)
            play_done = True
            while word_done == False:
                if play_done:
                    resp = input('''What's the message? (input)
                    Do you want to hear it again? (1)
                    Do you want to see the morse code? (2)
                    Do you want the solution? (3)
                    Do you want to get a hint? (4)
                    ''')            
                    if resp == word:
                        print('Correct! The message is "'+word+'"!')
                        word_done = True
                        break                        
                    elif resp == '1':
                        time.sleep(1)
                        morse_play(word)
                        continue
                    elif resp == '2':
                        print ('The code is '+morse_code(word))
                        continue
                    elif resp == '3':
                        print ('The message is '+word)
                        word_done = True
                        break
                    elif resp == '4':
                        letter = random.randint(1,len(word))
                        print('Letter nr '+str(letter)+' is "' +word[letter-1]+'"')
                    else:
                        correctSymbols = countCorrectSymbols(resp, word)
                        print ('Wrong answer. Nr of correct symbols: ' + str(correctSymbols))


## Generate random number sequence of lengh len_ as string, including zeroes
def n_len_rand(len_, floor=1):
    top = 10**len_
    if floor > top:
        raise ValueError(f"Floor {floor} must be less than requested top {top}")
    return f'{random.randrange(floor, top):0{len_}}'


## Count number of correct symbols in response string
def countCorrectSymbols(str_input, str_correct):
    strIndex = 0
    counter_correct = 0
    for s in str_input: 
        try:
            if s == str_correct[strIndex]:
                counter_correct += 1
            strIndex += 1
        except:
            continue
    return counter_correct


def morse_settings():
    global morse_signal_speed
    global morse_signal_speed_options
    global morse_signal_speed_options_strings
    global dur_short
    global dur_long    
    global morse_pitch
    
    settings_running = True
    
    while settings_running: 
        print ('''
        Morse code settings menu. Select your option:
        (1) Manage signal speed
        (2) Manage signal pitch
        (3) Quit''')
        option = input()   
        if option == '1':
            while True:
                current_signal_speed = morse_signal_speed_options_strings[morse_signal_speed_options.index(morse_signal_speed)]
                print('Current signal speed: ' + current_signal_speed)
                print('''Select signal speed:
                (1) Low
                (2) Medium
                (3) High''')
                input_speed = input()
                if input_speed in ['1', '2', '3']:
                    morse_signal_speed = morse_signal_speed_options[int(input_speed) - 1]
                    dur_short  = morse_signal_speed[0]
                    dur_long   = morse_signal_speed[1]                    
                    print('New signal speed: ' + morse_signal_speed_options_strings[morse_signal_speed_options.index(morse_signal_speed)])
                    break
                else:
                    print('Invalid input. Try again')
        elif option == '2':
            while True:
                print('Current signal pitch: ' + str(morse_pitch))
                print('Please specify signal pitch (100 - 1000): ')
                input_pitch = input()
                if int(input_pitch) in range(100,1000):
                    morse_pitch = int(input_pitch)
                    print('New signal pitch: ' + str(morse_pitch))
                    break
                else:
                    print('Invalid input. Try again')
        elif option == '3':
            settings_running = False
            print('Quitting settings menu...')
            print(str_mainMenu)
            break            
        else:
            print('Invalid input. Try again')
            