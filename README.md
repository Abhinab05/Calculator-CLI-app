First I defined four functions, 
1. add() for addition; 
2. sub() for subtraction; 
3. mul() for multiplication; &
4. div() for division with a check to handle division by zero.
Next, I used a while loop to repeatedly show a menu with options for the user to choose an operation.
The choice variable is used  to store the user’s selection.
If the choice is among 1 to 4, the program prompts the user to enter two numbers. This is done inside a try block to catch invalid inputs, using except ValueError for error handling.
Finally, based on the user’s choice, if-elif conditions are used to call the corresponding function and display the result.
If the user enters 5, the loop breaks, and the program ends.


# Calculator-CLI-app
