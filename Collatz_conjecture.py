def collatz_conjecture():
    while True:
            try:
                num = int(input('\nEnter an integer to see collatz conjecture steps:\n'))
                if num > 1:
                    pass
                else:
                    print('\nplease enter a number greater than 1')
                    continue
            except:
                print('\nPlease enter a valid integer value:')
                continue
            else:
                break
    steps = 0
    initial_num = num
   
    while num != 1:
        if num%2 == 0:
            num = num/2
            steps += 1
        else:
            num = ((num*3)+1)/2
            steps += 1
     
    print (f'\nNumber {initial_num} took {steps} steps to reach 1 using collatz conjecture')

collatz_conjecture()        