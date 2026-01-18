import time
import os
# sentence = input(f'Enter a sentence ')
# sentences = [x for x in sentence]
#
# print(sentences, end='')


sentence = input(f'Enter a sentence: ')
sentences = []

def read_write_line():
    for x in sentence:
        sentences.append(x)
    for item in sentences:
        print(item, end='')
        time.sleep(0.1)
    time.sleep(2)
    os.system("cls")       #clears terminal after printing; still looking for a better to wiping the entire terminal

read_write_line()
