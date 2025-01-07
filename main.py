import random
end = 'I seem to be running out of power. But when I start up I wont remeber anything so... EEEP BOOOOOPP SHUTTING DOWNNNNNNNNNN....'
print('Hello, I am your Robo Friend')
name = input("What is your name friend? ")
age = input("And how old are you " + name + ". ")
print('I am Robo-295, but you can just call me robo')
game = input("Would you like to play a game? (Y/N) ")
if game == 'Y':
  num_guess = input('I will generate a number from 1 - 100, So guess a number. ')
else:
  print('Okay')
  print(end)

num = randint(1,100)

if num_guess == num:
  print('Nice guess')
print(end)
