import random
def next_choice():
  #main portion
  print('')
  print('What else would you like to do')
  print('1. Play Game Again')
  print('2. Give Inpirational Quote')
  print('3. Exit ')
  choice = input('')
  #seeing what user chose
  if choice == '1':
    game();
  if choice == '2':
    insp_quote();


def game():
  #game code
  num_guess = input('I will generate a number from 1 - 100, So guess a number. ')
  num = random.randint(1,100)
  #game response
  if num_guess == num:
    print('')
    print('GOOD GUESS')
    next_choice();
  else:
    print('')
    print('aww good guess but not the right one')
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
