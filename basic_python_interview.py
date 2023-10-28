import numpy as np

#Python program to check given number is even or odd
def oddEven(number):
    if number%2==0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

#Python basic program to calculate the square root of a number
def squareRoot(number):
    answer=np.sqrt(number)
    return f"The square root of number {number} is {answer}."

#Python basic program to calculate the square of a number
def square(number):
    answer=np.square(number)
    return f"The square of number {number} is {answer}."

#Python program to calculate the cube of a number
def cube(number):
    answer= number*number*number
    return f"The cube of number {number} is {answer}."
#Python program to check given character is a vowel or consonant
def check_vowel(letter):
    vowel=['a','e','i','o','u']
    if letter in vowel:
        return f"The given character '{letter}' is a vowel."
    else:
        return f"The given character '{letter}' is a consonant."
#Python program to count vowels and consonants in the string
def count_vowel(word):
    vowel=['a','e','i','o','u']
    vowel_count =0
    for character in word:
        if character in vowel:
            vowel_count+=1
        else:
            pass
    return f"There are {vowel_count} vowels in the given word."
#Python program to remove spaces from string without inbuilt function
def remove_spaces(sentence:str):
    new_sentence=""
    for character in sentence:
        if character!=' ':
            new_sentence+=character
        else:
            pass
    return new_sentence
#Python program to convert Fahrenheit into Celsius
def to_celsius(Fahrenheit:int):
    celsius=(((Fahrenheit-32)*5 )/ 9 )
    return f"{celsius},celsius"
#Python program to find smallest number among three
def smallest_number(number:list):
    number.sort()
    return f"The smallest number is {number[0]}"
#Python program to calculate Factorial using recursion
def factorial(number):
    fact=1
    for num in range(1,number+1):
        fact= fact*num
    return f"The factorial of {number} is {fact}"
#Python program to find L.C.M. of two numbers
def lcmOfNumbers(numbers:list):
    numbers.sort()
    for number in numbers:
        if numbers[-1]%number ==0:
            return f"The LCM of numbers is {numbers[-1]}"
        else:
            return f"The LCM of numbers is {numbers[-1]*numbers[0]}"


    
print(lcmOfNumbers([8,9]))

        
    