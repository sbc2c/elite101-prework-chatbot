import random
def next_choice():
  #main portion
  print('')
  print('What else would you like to do \n')
  print('1. Play Game Again \n')
  print('2. Give Inpirational Quote \n')
  print('3. Exit \n')
  choice = input('')
  #seeing what user chose
  if choice == '1':
    guessing_game();
  if choice == '2':
    insp_quote();
  else:
     quit


def guessing_game():
    counter = 0
    comp_max_num = 100;
    comp_min_num = 1;
    #getting random number
    comp_gen_num = random.randint(1, comp_max_num);
    print(comp_gen_num)
    user_guess = -1
    #instructions for the game
    print('I have generated a number from 1 - 100 \n')
    print('You have to guess a number and I will tell you higher or lower \n')
    print('enter q to quit \n')
    print('Guess a number 1 - 100\n')
    while comp_gen_num != user_guess:
        #takes user input
        user_guess = input('');
        #check if user wants to break
        if user_guess == 'q':
            break
            next_choice();
        try:
            user_guess = int(user_guess);
        except:
            print('Sorry you didnt enter a number in the range of 1 - 100 \n')
            print('Try again\n')
            continue
        #compares user input to computer generated number
        if user_guess > comp_max_num or user_guess < comp_min_num:
            print('''\nSorry the number you entered isn't in the valid range of 1 - 100 \n''')
            continue
        if comp_gen_num < user_guess:
            #compares if user input is too high
            print('\nYour guessing too high!\n')
            counter = counter + 1
        elif comp_gen_num > user_guess:
            #compares if user input is too low
            print('\nYour guessing too low!\n')
            counter = counter + 1
        else:
            #win message
            print('\n Spot on!')
            counter = counter + 1
            print('\n You guessed it in ' + str(counter) + ' guess(es)\n');
            next_choice();


def insp_quote():
  insp1 = '''Try not to become a man of success, but rather become a man of value. - Albert Einstein'''
  insp2 = '''The only way to do great work is to love what you do. - Steve Jobs'''
  insp3 = '''Believe you can and you're halfway there. - Theodore Roosevelt'''
  randnum = random.randint(1,4)
  if randnum == 1:
    print('')
    print(insp1)
  if randnum == 2:
    print('')
    print(insp2)
  if randnum == 3:
    print('')
    print(insp3)
  next_choice();


#introduction
print('Hello, I am your Robo Friend')
name = input("What is your name friend? ")
age = input("And how old are you " + name + ". ")
print('I am Robo-295, but you can just call me robo')
next_choice();
