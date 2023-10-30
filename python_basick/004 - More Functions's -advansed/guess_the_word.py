import random
NAMES = ['Alexei', 'Ksenia', 'Leonid', 'Tatiana', 'Andrei', 'Viktoria', 'Olga', 'Kian', 'Ludmila', 'Luiza']

def create_word():
    # some_name_list = ['Alexei', 'Ksenia', 'Leonid', 'Tatiana', 'Andrei', 'Viktoria', 'Olga', 'Kian', 'Ludmila', 'Luiza']
    # random_position = random.randint(0, len(some_name_list))
    # guess_word_initial = some_name_list[random_position - 1]
    # print(guess_word_initial)
    # return guess_word_initial
    word = random.choice(NAMES)
    print(word)
    return word

def guess_word():
    word_printed = '-' * len(guess_word_general)
    counter = 0
    while counter < 10:
        word = ''
        letter = input('Input the Letter  !')
        for index, value in enumerate(guess_word_general):
            if value.upper() == letter.upper():
                word += value
            else:
                word += '_'
        for index, value in enumerate(word):
            if value.isalpha():
                if index == 0:
                    word_printed = f'{value}{word_printed[1:]}'
                                   #value + word_printed[1:]
                elif index == len(word_printed) - 1:
                    word_printed = f'{word_printed[0:-1]}{value}'
                                   #word_printed[0:-1] + value
                else:
                    word_printed = f'{word_printed[0: index]}{value}{word_printed[index + 1:]}'
                                   #word_printed[0: index] + value + word_printed[index + 1:]
        if word_printed == guess_word_general:
            print(f'You win congratulation !!! Next Name =>')
            break
        print(word_printed)
        counter += 1
        print(f'You have {10 - counter} try tu guess the word !')

while True:
    guess_word_general = create_word()
    guess_word()










