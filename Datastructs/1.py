
number = 0
while True: ## this loop will catch any non-ints/float numbers inputted
    try: #test the number
        numberinput = int(input("enter a number a number between 1 and 20: "))  #user enters #
        assert numberinput > 0  #make sure the number is between your limits
        assert numberinput <= 20  #make sure the number is between your limits
        number = numberinput  #set the number == to our vetted numberInput
        break #exit infinite loop
    except:  #if any errors in above, we enter this clause
        print('Please enter a valid number between 1 and 19') #tell user to try another number
        continue #continue sends us to the top of the loop (starting with try)

def factorial(number):
    value=1  #initial value
    stringOfCalculations= ''  #empty string that we can build on as we loop through
    for i in range(1, number + 1): 
        value *= i 
        if i == 1:  #if the value is 1, we dont want to do * i in the string, we want to just add i to the string since we start with 1
            stringOfCalculations += f'{i}' #we add i to the start of the string. This is called an f' string, similar to .format() but cleaner
        else: #if the number is not 1
            stringOfCalculations += f' * {i}' # we want to add * i, since were doing math these steps that aren't 1*1

    stringOfCalculations += f' = {value}' # after looping, our value is the total, so we append '= value' to our string
    print(stringOfCalculations) # print the full string
    return #you chose to return nothing here, but you could also return the value


factorial(number) #no need for the if clause since we check the number is between 1-19 in the try block
