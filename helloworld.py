# This program says hello and asks for my name
print('hello world')
print('What is your name?')  # Asks for their name
myName = input()
print('It is good to meet you ' + myName)
print('The length of your name is ' + str(len(myName)))
print('What is your age?')  # Asks for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')