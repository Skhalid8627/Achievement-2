#Here I ask for user input and store it as a string data type
print("Please enter your unique string combination(Hint: NO NUMBERS)")
user_string = str(input())
#final_str is where i am going to store the iterated string which will be converted 
final_str = ''
#I have chosen to use for loop to iterate through the string input and convert letter by letter
#storing them in final_str
for i in (user_string):
    if i.isupper() == True:
        final_str += i.lower()
    elif i.islower() == True:
        final_str += i.upper()
#Lastly I am printing final_str (the converted string) as my final output
print(final_str)