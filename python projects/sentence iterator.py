import time

# sentence = input(f'Enter a sentence ')
# sentences = [x for x in sentence]
#
# print(sentences, end='')
# time.sleep(0.1)


sentence = input(f'Enter a sentence: ')
sentences = []

for x in sentence:
    sentences.append(x)
for item in sentences:
    print(sentences, end='')
    time.sleep(0.1)
