import random
print('welcome to **Hangman** Game')
print('============================')

word_list = ['ardvark','baboon','camel','broken','world','lion','butter','bark','rubbish','monkey','apple']

choosen_word = random.choice(word_list)

a = '''
    _____
    0   |
        |
        |
        |
    '''
b = '''
    _____
    0   |
   /    |
        |
        |
    '''
c = '''
    _____
    0   |
   /|   |
        |
        |
    '''    
d = '''
    _____
    0   |
   /|\  |
        |
        |
    ''' 
e = '''
    _____
    0   |
   /|\  |
   /    |
        |
    ''' 
f = '''
    _____
    0   |
   /|\  |
   / \  |
        |
    '''     

life_lines = [f,e,d,c,b,a]
find = len(choosen_word)*'#'
print(f'Find the word : {find}')
    
life = len(life_lines)-1
result = ['#' for i in range(len(choosen_word))]
while True:
    count = 0
    
    guess = input('guess the word : ').lower()
    if guess not in choosen_word:
        life -= 1
    
    
    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            result[i] = guess
            # result+=i
            # result+= i
        # else:
        #     result+='#'
            # result.append('_')
            
    if life == 0 :
        print(f'Game Over \nthe correct word is {choosen_word}') 
        print(f'{life_lines[life]}')
        break 
    print(f'remaining life : {life_lines[life]}')             
    print(''.join(result))
    if choosen_word == ''.join(result):
        print(f'you win !!! \nyou find the correct word : {choosen_word}')
        break