
"""
Author: Mageza Shalom
Cohort: 2
Retake Assessment: 3
Part I : Recursion

"""
#SOLUTION


# Here I define a function to count even and odd digits
def CountEvenOrOdd(string):
    def Function(FunctionInput):
        if len(FunctionInput) == 0:
            return 0, 0
            
        odd, even = Function(FunctionInput[1:])

        # Here is where I defined the variables even and odd and alos added... 
        # a count to increases when a digit with this specification is spotted
        if int(FunctionInput[0]) % 2 == 0:
            even += 1

        else:
            odd += 1  
        return odd, even
            

    # Finally, here I defined what will be displayed based on what the program has counted
    odd, even = Function(string)
   
    if even > odd:
        return f'There are more even digits than odd digits.\n ===> {even} > {odd}'
    elif even == odd:
        return f'There are equal number of odd and even digits. \n ===> {even} = {odd} '
    else:
        return f'There are more odd digits than even digits.\n ===> {odd} > {even}'
        

#Here I prompt the user o add any digit and call the function for that number
number = input("Insert any number here: ")
print(CountEvenOrOdd(number))

