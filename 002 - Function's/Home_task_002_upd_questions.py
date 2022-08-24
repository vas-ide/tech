

q_and_a = {'What language we are learning ? ': 'python',
           'What IDE we a going to use? ': 'pycharm',
           'What additional language we are going to use? ': 'javascript',
           'What language needed for created site? ': 'html',
           'What language we need to learn for generate style in site? ': 'css',
           'Everything in Python ?  ': 'object',
           'What Python actual version ? ': 3,
           'What type in input? ': 'string',
           'What method we use? ': 'lower',
           'What opposite method we known? ': 'upper'}
counter = 0
for question, answer in q_and_a.items():
    pull = input(question)
    if pull.lower() == answer:
        counter += 1
        print(f'Your\'s answer is {pull} True')
    else:
        print(f'Your\'s answer is {pull} False')
print(f'Number of question\'s are {len(q_and_a)} - write answers\'s are {counter}')







