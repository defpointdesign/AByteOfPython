number = 23
running = True
while running:
    guess = int(input('Enter an integer: '))
    if guess == number:
        print('Congratulation, you guessed in!')
        running = False
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('no, it is a little lower than that')
else:
    print ('While loop is over')
print ('Done')

