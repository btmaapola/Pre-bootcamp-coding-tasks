
# Task 1
x = 0
y = 1
print(x)
print(y)
x += 3
y += x
print(x)
print(y)

#Task 2 
o = 1
p = 2
x = o+o*p
y = (o+o)*p
z = x 
a =  y/p
b =  x/p

#Task 3 
a, b = input("Enter a two numbers to determine if the input or sum is 65: ").split()
a = float(a)
b = float(b)

def input_or_sum_of_sixtyfive(n,l):
    if n+l == 65 or n == 65 or l == 65 :
        return True
    else:
        return False

print(input_or_sum_of_sixtyfive(a,b))

#Task 4 
c, d = input("Enter two numbers to determine if the input is and sum has 3: ").split()
c = float(c)
d = float(d)

def input_of_and_sum_with_three(n,l):
    set1 = set(str(n+l))
    if (n == 3 or l == 3) and ("3" in set1): 
        return True
    else: 
        return False

print(input_of_and_sum_with_three(c,d))

#Task 5 

e = int(18)
f = int(12)
g = int(20)

def area_of_triangle(n,l,u): 
    s = 1/2 *(e+f+g)                            #semiperimeter of triangle 
    Area = (s*(s-e)*(s-f)*(s-g)) ** (1/2)
    Area = round(Area)
    print("The area of the triangle is " + str(Area))

area_of_triangle(e,f,g)

#Task 6
def length_function(string):
    j = 0
    n = 0
    for n in string : 
        j +=1 
        n +=1
    return j 

x = list(map(int, input("Enter any multiple numbers to find the maximum number: ").split()))
print(x)

def max_number_function(inputs):
    i = 0
    list1 = []
    index = 0
    length_x = length_function(x)
    while i < float("inf"):
        if i in inputs:
            list1.insert(index, i)
            index += 1
        i += 1
        J = length_function(list1)
        if J == length_x : 
            k = J -1
            maximum_number = list1[k]
            print("The maximum number is " + str(maximum_number))
            break

max_number_function(x)

#Task 7 

temp_celsius = int(0) 

def celsius_to_fahrenheit(temperature_celsius): 
    temp_fahrenheit_output = (temperature_celsius * (9/5)) + 32
    print("The input celsius temp is equal to " + str(temp_fahrenheit_output) + " Fahrenheit" )
    return temp_fahrenheit_output

celsius_to_fahrenheit(temp_celsius)

temp_fahrenheit_input = int(134)

def fahrenheit_to_celsius(temperature_fahrenheit): 
    temperature_celsius_output = (temperature_fahrenheit - 32)* (5/9)
    temperature_celsius_output = round(temperature_celsius_output)
    print("The input fahrenheit temp is equal to " + str(temperature_celsius_output) + " Celsius" )
    return temperature_celsius_output

fahrenheit_to_celsius(temp_fahrenheit_input)

#Task 8
q = int(input("Please enter any number representing time: "))

def time_converting_function(input_time):
    hours = input_time // 60 
    minutes = input_time % 60 
    print ( "Converted time is " + str(hours) + " hours and " + str(minutes) + " minutes")

time_converting_function(q)

#Task 9 

no_of_multiples_5 = (1000//5) - 1  #number of multiples of 5 in 995
no_of_multiples_3 = (1000//3)   #number of multiples of 3 in 1000

def multiples_function(input1,input2):
    list_C = []
    list_B = []
    i =0
    j = 0
    index = 0
    index2 = 0
    while i <= input1 and j <= input2 : 
        multiples_of_5 = 5*i 
        multiples_of_3 = 3*j
        list_C.insert(index, multiples_of_5)
        list_B.insert(index2,multiples_of_3)
        i += 1 
        j += 1 
        index +=1 
        index2 +=1
    new_list = list_C + list_B
    new_list.sort()
    new_list = list(set(new_list)) #removing duplicate numbers
    sum_of_multiples = sum(new_list)
    print ("The sum of multiples of 3 and 5 below 1000 is: " + str(sum_of_multiples))

multiples_function(no_of_multiples_5, no_of_multiples_3)


#Task 10 

CountryName = str("Eutopia")

def vowels_in_string(String):
    list_A = []
    for letters in String:
        if letters in 'AaEeIiOoUu':
            list_A.append(letters)
    
    print("The vowels in the word " + CountryName + " are: " + str(list_A))

vowels_in_string(CountryName)

#Task 11

Word = input("Enter any word: ")
Word2 = input("Enter another word to compare with first word: " )

def common_characters_in_words(String1,String2):
    list_B = []
    for letters in String1:
        if letters in String2:
            list_B.append(letters)
            
    print("Common letters in both words are " + str(list_B))

common_characters_in_words(Word,Word2)
