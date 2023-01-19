if (name in allowedUsers):
    password = input('Your password? \n')
    userId = allowedUsers.index(name)

    if (password == allowedPassword[userId]):
        from datetime import datetime
        now = datetime.now()
        print(now.strftime('%d/%m/%y %H:%M:%S'))
        
        
        print('Welcome %s' % name)
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: '))

        if(selectedOption == 1):
            int(input('How much would you like to withdraw? \n'))
            print('Take your cash')
        elif(selectedOption == 2):
            balance = 0
            deposit = int(input('How much would you like to deposit? \n'))
            balance += deposit 
            print('Your current balance is: %d' % balance )
        elif(selectedOption == 3):
            input('What issue will you like to report? \n')
            print('Thank you for contacting us.')
            #print('You selected %s' % selectedOption)
        else:
            print('Invalid option selected, please try again')
    
    else:
        print('Password incorrect, please try again')

else:
    print('Name not found, please try again')
