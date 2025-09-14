a=12.2
print(type(a))
d=14/2
print(type(d))
e=45j
print(type(e))
g='123456dcabgsder@!#$%&'
print(type(g))
h=True
print(type(h))
j='A'
print(ord(j))
k=65
print(chr(k))
q="Sher"
print(q[1])
r="Sher"
print(r[-3])
s='Sher'
print(s[2],s[-1])
a="Sher Coder"
print(a[0:4:1])
b="Sher Coder"
print(b[5:10:1])
c="Sher Coder"
print(c[0:10:1])
d="Sher Coder"
print(d[::])
e="Dog Shop"
print(e[4:7:1])
f=12
f=str(f)
print(type(f))
g=12
g=bool(g)
print(type(g))
f=""

f=bool(f)
print(bool(f))
g=0.0
g=bool(g)
print(bool(g))
name="roshini" #output using multiple strings
age="18"
print("hello my name is",name,"and my age is",age)
name="roshini"#output using formatted string(only one string)
age="18"
print(f"my name is {name} and my age is {age}")
a=int(input("hello my age is"))#input function
print(a)
a=12#arithmetic operators#addition operator
b=24
print(a+b)
a=23
b=45
print(a*b)
a=67
b=56
print(b/a)
a=5#floor division operator
b=20
print(b//a)
a=5
b=2
print(a**b)
a=32#mod operator
b=5
print(a%b)
a=20#reaasigning values
a=a+20
a=a+40
print(a)
a=20#compound assignment opearations
a+=20
a+=40
print(a)
a=23#comparison operator
b=23
print(a==b)
a=45
b=45
print(a!=b)
print("A">"B")#comparision operators using strings using ASCII values
print("ABC">"BCD")#comparison operators using multiple ASCII values
print(12==12 and 23>21 and 56>52)#logical "AND" operator
print(12==12 and 45<67 and 56>76)
print(12==13 or 34==78 or 78==78)#logical "OR" operator
print(not 12==12)#logical "NOT" operator
print(126>130)#practice trivial questions
print((456==456)!=(235==236))
print(12<10 or 45==56 or 69>70 or 15!=13)
print(True and bool(0))
a=13#"if" conditional statement
if a>10:
    print("I will do task A")
a=23
if a<10:
    print("I will do task A")
a=6#"if-else" conditional statement
if a>10:
    print("I will do task A")
else:
    print("I will do task B")
a=30#"if-elif-else" conditional statement
if a>35:
    print("I will do task A")
elif a>40:
    print("I will do task B")
else:
    print("I will do task C")
year=2800
if year%100==0 and year%400==0:
    print("centurion leap year")
elif year%100!=0 and year%4==0:
    print("normal leap year")
else:
    print("normal year")
a=range(1,23,1)#for loop
for i in a:
    print(i) 
b=range(1,50,1)
for i in b:
    print(i)
a=range(16,0,-1)#for loop in reverse order
for i in a:
    print(i)
for i in range(5,51,5):#print 5 table using for loop
    print(i)
a="SHERYIAN"#for loop for strings using index values
for i in range(0,8,1):
    print(a[i])
a="SHERYIANS TEACHES INDUSTRY THINGS"#length of string
print(len(a))
a="SHERYIANS TEACHES INDUSTRY THINGS"
for i in range(0,33,1):
    print(a[i])
a="SHERYIANS IS COOL"#iterating directly over string without index values using for loop
for i in a:
    print(i)
for i in range(1,21,1): #break statement using for loop  
    if i==15:
     break
    print(i)
for i in range(1,21,1): #continue statement using for loop
    if i==15:
        continue
    print(i)
for i in range(1,21,1): #else statement using for loop
    if i==56:
        print("break statement is executed")
        break
    print(i)
else:
    print("break statement is not executed")
for i in range(1,21,1):
    if i==16:
        print("break statement is executed")
        break
    print(i)
else:
    print("break statement is not executed")
n=int(input("please tell your number")) #for loop questions
for i in range(n):
    print("Hello World")
n=int(input("please tell your number"))
for i in range(1,n+1,1):
    print(i)
for i in range(n,0,-1):
    print(i)
n=int(input("please tell your number"))
for i in range(n,(n*10)+1):
    print(i)
n=int(input("please tell your number"))#sum of n terms using for loop
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(f"your sum is {sum}")
n=int(input("please tell your number"))#factorial of a number using for loop
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(f"your factorial is {fact} ")
n=int(input("please tell your number"))#sum of even and odd numbers in given number range
even=0
odd=0
for i in range(1,n+1,1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(f"your even and odd sum are {even},{odd}")
n=int(input("please enter your number"))#finding factors of a number using for loop
for i in range(1,n+1,1):
    if n%i==0:
        print(i)
n=int(input("check your number is perfect or not"))#to check perfect number using for loop
sum=0
for i in range(1,n,1):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")
n=int(input("check if given number is prime or not"))
for i in range(1,n+1,1):
    if n%1==0 and n%n==0:
        print("prime number")
    else:
        print("not a prime number")
n=int(input("check your number is prime or not"))#check if number is prime using for loop
count=0
for i in range(1,n+1,1):
    if n%i==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("not a prime number")
a="SHERYIANS"
for i in range(8,-1,-1):
    print(a[i])
a="SHERYIANS"#reverse a string using for loop
b=""
for i in range(8,-1,-1):
    b=b+a[i]
print(b)
a="NAMAN"#to check given string is palindrome or not using for loop
b=""
for i in range(4,-1,-1):
    b=b+a[i]
if b==a:
    print("palindrome")
else:
    print("not a palindrome")
a="sdfsogn12413@#$%^&u"#count all digits,characters,special characters using for loop
dig=0
char=0
spchar=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(f"your digits are{dig},your characters are{char} and your special characters are{spchar}")
a=1# while loop
while a<=30:
    print(a)
    a=a+1
a=256#while loop questions
while a>0:
    print(a%10)
    a=a//10
a=576#reversing a number using while loop
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10
print(rev)
if rev==a:#checking if number is palindrome or not
    print("palindrome")
else:
    print("not a palindrome")
n=7689
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(f"your sum is {sum}")
for i in range(20,1,-2):
    print(i)
a=234#sum of digits given in number using while loop
sum=0
while a>0:
    r=a%10
    a=a//10
    sum=sum+r
print(f"your sum is {sum}")
n=int(input("please tell your number"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(f"your average is {sum/10}")
for i in range(100,500,1):#numbers divisible by 11 and not by 2 b/w 100 and 500 checking using for loop
    if i%11==0 and i%2!=0:
        print(i)
def sum(a,b):#function parameters and arguments
    print(f"your sum is {a+b}")
sum(12,13)#positional argument
def hello(name,age):#key word argument
    print(f"your name is {name} and your age is {age}")
hello(age=12,name="akarsh")
def sum(a,b=45):#default arguments
    print(f"your sum is {sum}")
sum(44,34)
def palindrome(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev=rev+str[i]
    if rev==str:
       print("palindrome")
    else:
       print("not a palindrome")
palindrome("naman")
palindrome("format")
n=20
for i in range(1,20,1):
    if i%3==0 and i%5==0:
        print(i)
def hello():#functions
    return "hello how are you"
print(hello())
a=12,13,14,15,16#data structures we use them to store multiple values in the variable
print(a)
a=[12,13,14,12.6,print()]
print(a[0:5])
a=[12,13,14,14.5,15]
for i in range(len(a)):
    print(a[i])
a=[7,9,8,0]
print(a[0:3])
l=[1,2,3,6]#append in list
l.append(4)
print(l)
a=[1,3,5,8]#insert in list
a.insert(1,2)
print(a)
l=[1,789,987,765]
largest=l[0]
index=0
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"your largest number is {largest} at index {index}")
l=[34,67,5678,7890]
largest=l[1]
for i in range(len(l)):
    if l[i]>l[1]:
        largest=l[i]
print(f"your largest number is {largest}")
l=[12,16,13,19,17]
largest=l[0]
sec_largest=l[0]
for i in l:
    if i>largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
print(f"your largest number is {largest} and your second largest number is {sec_largest}")
l=[0,16,19,23,25]
for i in range(len(l)-1):
    if l[0]<l[1] and l[1]<l[2] and l[2]<l[3] and l[3]<l[4]:
        print("list is sorted")
    else:
        print("list is not sorted")
a=(1,5,8,9)
print(type(a))
a=(1,2,3,4,5,5,6,print(),"hello")
count=a.count(5)
print(count)
a=hash("hello")
print(a)
a=hash(2)
print(a)
a={"hello":2}
print(type(a))
a=[5,7,1,3]
largest=a[0]
sec_largest=a[0]
smallest=a[0]
sec_smallest=a[0]
for i in a:
    if i>largest:
        sec_largest=largest
        largest=i
    if i<smallest:
        sec_smallest=smallest
        smallest=i
    elif i<sec_smallest:
        sec_smallest=i
print(f"your largest number is {largest} and your second largest number is {sec_largest} and your smallest number is {smallest} and your second smallest number is {sec_smallest}")

a={1:100,2:200,3:300}#merge two dictionaries
b={4:400,5:500,6:600}
for i in b:
    a[i]=b[i]
print(a)
d={10:100,20:200,30:300}#sum of values in dictionary
sum=0
for i in d:
    sum=sum+d[i]
print(f"your sum is {sum}")
d=[1,1,1,2,2,3,3,3,4,4,5,6,6,7]
count=0
for i in d:
    if i==1:
        count=count+1
    if i==2:
        count=count+1
    if i==3:
        count=count+1
    if i==4:
        count=count+1
print(f"count is {count}")
d1={10:100,20:200,30:300}
d2={30:400,40:500,20:600}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
a=5
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")
else:
    print("no exception")
finally:
    print("run no matter what")
print("division")
class Factory:#OOPS
    a=12
    def hello(self):
        print("hello")
obj=Factory()
obj.hello()
obj2=Factory()
obj3=Factory()
print(obj2.a)
class Factory:
    def__init__(self,material,zips,pockets):
       pass
Factory(material,zips,pockets)






    











    



    


    

        











    

    

      
               


