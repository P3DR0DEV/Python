print('--'*20)
print('Welcome to my computer quiz!'.center(40))
print('--'*20)

correct = 0

while True:
    playing = str(input('Do you want to play a quiz game?[s/n] '))
    if playing[0] in 'sS':
        print('Let\'s play')
        
        answer = str(input('What does CPU stand for? '))
        if answer.lower() == "central processing unit":
            print('Correct!')
            correct +=1
        else:
            print('Incorrect!')
            
        answer = str(input('What does GPU stand for? '))
        if answer.lower() == "graphics processing unit":
            print('Correct!')
            correct +=1
        else:
            print('Incorrect!')
            
        answer = str(input('What does RAM stand for? '))
        if answer.lower() == "random acces memory":
            print('Correct!')
            correct += 1
        else:
            print('Incorrect!')  
        
        answer = str(input('What does PSU stand for? '))
        if answer.lower() == "power suply":
            print('Correct!')
            correct +=  1
        else:
            print('Incorrect!')  
        print(f'You have ansewared {correct} questions correct!')
        print('--'*20)
        break
    elif playing[0] in 'nN':
        print('You choose to Leave the game.')
        break
    else:
        continue