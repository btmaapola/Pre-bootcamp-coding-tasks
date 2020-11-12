
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
print(x,y,z,a,b)

#Task 3 
a, b = input("Enter a two values: ").split() 
a = float(a)
b = float(b)
def function(n,l):
    if n+l == 65 or n == 65 or l == 65 :
        return True
    else:
        return False

print(function(a,b))

#Task 4 
c, d = input("Enter two values: ").split() 
c = float(c)
d = float(d)

def function1(n,l):
    set1 = set(str(c+d))
    if n == 3 or l == 3 or "3" in set1 : 
        return True
    else: 
        return False

print(function1(c,d))

#Task 5 

#e, f, g = input("Enter three sides of a triangle: ").split()
e = 7
f = 9
g = 7
e = float(e)
f = float(f)
g = float(g)

def AreaFunction(n,l,u): 
    s = 1/2 *(e+f+g)                            #semiperimeter of triangle 
    Area = (s*(s-e)*(s-f)*(s-g)) ** (1/2)
    #Area = round(Area, 0)
    print(Area)

AreaFunction(e,f,g)

#Task 6
h, i, j = input("Enter three numbers: ").split()
h = float(h)
i = float(i)
j = float(j)

count = 0
ind = 0
set01 = []

def MaxNumberFunction(num1,num2,num3, counter, index, set1):
    while counter < float("inf") : 
        if counter == num1: 
            set1.insert(index, num1)
            index += 1 
        if counter == num2: 
            set1.insert(index, num2)
            index += 1 
        if counter == num3: 
            set1.insert(index, num3)
            index += 1 
        counter += 1 
        if len(set1) == 3:
            MaxNo = set1[2]
            print (str(MaxNo) + " is a maximum number")
            break

MaxNumberFunction(h,i,j, count, ind, set01)

#Task 7 

#TempC = input("Please enter temperature value in Celsius: ")
TempC = 0 
TempC = float(TempC)

def TempFunction(TemperatureCelsius): 
    TempF = (TemperatureCelsius * (9/5)) + 32
    print( str(TempF) + " Fahrenheit" )
    return TempF

TempFunction(TempC)

TempF = 134
TempF = float(TempF)

def TempFunction1(TemperatureFahrenheit): 
    TempC = (TemperatureFahrenheit - 32)* (5/9)
    print( str(TempC) + " Celsius" )
    return TempC

TempFunction1(TempF)

#Task 8
q = float(input("Please enter any number representing time: "))
q = round(q)

def TimeFunction(InputTime):
    hours = InputTime // 60 
    minutes = InputTime % 60 
    print ( "Converted time is " + str(hours) + " hours and " + str(minutes) + "minutes")

TimeFunction(q)

#Task 9 
value = 1000 
num1 = 3 
num2 = 5 
multiNo = (1000//5) #number of multiples of 5 in 1000 
multi2No = (1000//3) +1 #number of multiples of 3 in 1000 + 1 extra

count = 1
count2 = 1
ind = 0
ind2 = 0
ind3 = 0
set01 = [] 
set02 = []
set03 = []
import math

def MultiplesFunction(multiple1,multiple2,multiple1No,multiple2No,counter, counter2, index, index2, set1,set2):
    while counter2 < multiple1No and counter < multiple2No: 
        multiples2 = counter2*multiple2 
        multiples1 = counter*multiple1 
        set1.insert(index, multiples1)
        set2.insert(index2, multiples2)
        index2 += 1 
        counter2 += 1
        index += 1 
        counter += 1
    
    set4 = set1 + set2
    set4.sort()
    
    #removing duplicate numbers
    set4 = list(set(set4)) 
    
    print (sum(set4))

 
MultiplesFunction(num1,num2,multiNo,multi2No,count,count2,ind,ind2,set01,set02)


#Task 10 

CountryName = str("Eutopia")
print (CountryName)
setA = []
for letters in CountryName:
    if letters in 'AaEeIiOoUu':
        setA.append(letters)


print("The vowels the country name entered are: " + str(setA))

#Task 11

Word = input('Enter any word: ' )
Word2 = input('Enter any word2: ' )

setB = []
for letters in Word:
    if letters in Word2:
        setB.append(letters)

#print(setB)
print("Common letters in both words are " + str(setB))
