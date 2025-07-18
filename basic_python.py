print("hello world")
print("all are done")
print("in one line"," it is work")
print(23)
print(23+12)
name = "partho"     # comment
age = 23
price = 25.99
print(name)
print(price)
print(age)
print("My name is",name)
print("My age is",age)
print("price is ",price)



# swap program

a=2
b=5
c=a
a=b
b=c
print(a)
print(b)
print(type(name))          # show data type of name variable
print(type(age))           # show data type of age variable
print(type(price))         # show data type of price variable



# Total  5  of Data type (int,float,string,boolean,None)

name1= 'partho'            # string also in single cotation 
name2= "partho"            # string also in double cotation
name3= '''partho'''        # string also in triple cotation

print(name1)
print(name2)
print(name3)

age1=23
BMI=20.5
old = False
a = None
d ='A'                     # no character in python all are string

print(type(old))
print(type(a))
print(old)
print(a)
print(age1)
print(BMI)
print(type(d))             # show data type of d variable



#sum,sub print 
x=2
y=5
sum=x+y
sub=x-y
print(sub)
print(sum)


"""
multiline 
comment

"""



# Arithmetric Operation ( + , - , * , / , % , ** , // )

aa=5
bb=2

print(aa+bb)
print(aa-bb)
print(aa*bb)
print(aa/bb)   # in div always show in float 
print(aa%bb)   # modulas / remainder
print(aa**bb)  # power a^b 
print(aa//bb)  # floor the div value 



# Relational/Comparison Operation ( == , != , > , < , <= , >= )

num1=50
num2=30
num3=50

print(num1==num2)   # True / False show only
print(num1!=num2)   # True / False show only
print(num1<num2)    # True / False show only
print(num1>num2)    # True / False show only
print(num1<=num2)   # True / False show only
print(num1>=num2)   # True / False show only
print(num1==num3)   # True / False show only



# Assignment Operation ( = , += , -= , *= , /= , %= , **= )

n1=10
n1+=10   # n1=n1+10
print("n1 is :",n1)

n2=10
n2-=10  # n2=n2-10
print("n2 is :",n2)

n3=10
n3*=10  # n3=n3*10
print("n3 is :",n3)

n4=10
n4/=10  # n4=n4/10
print("n4 is :",n4)

n5=10
n5%=10  # n5=n5%10
print("n5 is :",n5)

n6=10
n6**=10 # n6=n6**10
print("n6 is :",n6)



# Logical Operators ( not , and , or )

print(not True)
print(not False)

a1= 50
b1= 20
print(not (a1>b1))   # not(true) = false
print(not (a1<b1))   # not(false)= true

val1=True
val2=True
val3=False
val4=False
print("val1 and val2 is :",val1 and val2)
print("val1 and val3 is :",val1 and val3)
print("val3 and val4 is :",val3 and val4)
print("val1 or  val2 is :",val1 or val2)
print("val1 or  val3 is :",val1 or val3)
print("val3 or  val4 is :",val3 or val4)

print("(a1==b1) or (a1>b1) is :", (a1==b1) or (a1>b1) )


# Type Conversion (implecite , explecite)

# implecite (Automatic conversion)
z1=3        # int value 
z2=5.4      # float value
sum1=z1+z2
print(sum1)  #  float value
"""
z1= "3"        # string value 
z2=5.4      # float value
sum1=z1+z2
print(sum1)  #  error
"""
# explecite (Manual)
x1=float("3")  # type casting string to float
x2=4.6
s2=x1+x2
print(s2)

x3=int("3")  # type casting string to int
x4=4.6
s3=x3+x4
print(s3)  # auto float value

x5=int("3")  # type casting string to int
x6=4
s4=x5+x6
print(s4)

q1=2.3     # type casting  num to string
q2=str(q1)
print("q1 is string :", q2)
print(type(q2))



# user input 

input("Enter your name : ")          # string value

variable = input("Enter you name again : ")    # string value input 
print("welcome,",variable)

variable1 = int(input("Enter the number : "))     # int value input
print("string to int value input : ",variable1)

variable2 = float(input("Enter the number again : "))
print("string to float value input : ",variable2)


names = input("Enter name : ")
ages = int(input("Enter age :"))
marks = float(input("Enter marks : "))
print("welcome, ",names)
print("your age is :",ages)
print("yours marks is :",marks)