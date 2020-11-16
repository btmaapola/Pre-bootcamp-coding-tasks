
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
a, b = input("Enter a two values: ").split()
a = float(a)
b = float(b)

def input_or_sum_of_sixtyfive(n,l):
    if n+l == 65 or n == 65 or l == 65 :
        return True
    else:
        return False

print(input_or_sum_of_sixtyfive(a,b))

#Task 4 
c, d = input("Enter two values: ").split()
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
    print(Area)

area_of_triangle(e,f,g)

#Task 6
h, i, j = input("Enter three numbers to find the maximum number: ").split()
h = float(h)
i = float(i)
j = float(j)

def max_number_function(num1,num2,num3):
    counter = 0 
    index = 0 
    list_1 = []
    while counter < float("inf") : 
        if counter == num1: 
            list_1.insert(index, num1)
            index += 1 
        if counter == num2: 
            list_1.insert(index, num2)
            index += 1 
        if counter == num3: 
            list_1.insert(index, num3)
            index += 1 
        counter += 1 
        if len(list_1) == 3:
            MaxNo = list_1[2]
            print (str(MaxNo) + " is a maximum number")
            break

max_number_function(h,i,j)

#Task 7 

temp_celsius = int(0) 

def celsius_to_fahrenheit(temperature_celsius): 
    temp_fahrenheit_output = (temperature_celsius * (9/5)) + 32
    print( str(temp_fahrenheit_output) + " Fahrenheit" )
    return temp_fahrenheit_output

celsius_to_fahrenheit(temp_celsius)

temp_fahrenheit_input = int(134)

def fahrenheit_to_celsius(temperature_fahrenheit): 
    temperature_celsius_output = (temperature_fahrenheit - 32)* (5/9)
    print( str(temperature_celsius_output) + " Celsius" )
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
