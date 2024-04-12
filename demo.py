from random import randint
words=['bus','cricket','pen','paper','football', 'newspaper', 'mathematics', 'python']
word=words[randint(0,len(words)-1)]

name=input('Enter your name:- ')
print('Good Luck!', name)
print('Guess the word\n')
print('\t\t*****RULE BOOK*****')
print('1) Enter only lowercase single alphabet, input like "swn" is invalid')
print('2) You have 10 tries to accomplish you target.')
print('3) It is guaranted that the lucky word is in lowercase only.\n\n')

turns=10
guess=''

while turns!=0:
    count=0
    for i in word:
        if i in guess:
            print(i, end=' ')
        else:
            print('-', end=' ')
            count+=1

    if count==0:
        print('\nHurray, you won!')
        print('Congartulations', name)
        print('The word is', word)
        break
    
    current_guess=cguess=input('\tEnter a single lowercase alphabet:- ')
    guess+=cguess

    if cguess not in word:
        turns-=1
        print('Be careful\nYou have only', turns, 'left.\n\n')
        if turns==0:
            print('You lose, Better luck next time!')

