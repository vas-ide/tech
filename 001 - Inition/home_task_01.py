



while True:
    counter_answers = 0
    users_input = input('What language we are learning ? ').lower()
    answer = 'python'
    # _____1_____
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____2_____
    users_input = input('What IDE we a going to use? ').lower()
    answer = 'pycharm'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____3_____
    users_input = input('What additional language we are going to use? ').lower()
    answer = 'javascript'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____4_____
    users_input = input('What language needed for created site? ').lower()
    answer = 'html'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____5_____
    users_input = input('What language we need to learn for generate style in site? ').lower()
    answer = 'css'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____6_____
    users_input = input('Everything in Python ?  ').lower()
    answer = 'object'
    # _____1_____
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____7_____
    users_input = input('What Python actual version ? ')
    if float(users_input) >= 3:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____8_____
    users_input = input('What type in input? ').lower()
    answer = 'string'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____9_____
    users_input = input('What method we use? ').lower()
    answer = 'lower'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
    else:
        print('%s - Is a wrong answer.' % users_input)
    # _____10_____
    users_input = input('What opposite method we known? ').lower()
    answer = 'upper'
    if users_input == answer:
        print('%s - is true' % users_input)
        counter_answers += 1
        print(f'Из 10 вопросов {counter_answers} правильных ответов')
        break
    else:
        print('%s - Is a wrong answer.' % users_input)
        print(f'Из 10 вопросов {counter_answers} правильных ответов')
        break




