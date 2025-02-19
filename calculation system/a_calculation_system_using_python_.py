#defining fuctions for simple calculation
def add(a,b):
  add=a+b
  print(a,"+",b,"=",add)

def sub(a,b):
  sub=a-b
  print(a,"-",b,"=",sub)

def mul(a,b):
  mul=a+b
  print(a,"*",b,"=",mul)

def div(a,b):
  add=a/b
  print(a,"/",b,"=",div)

#defining function using lambda functions to calculate parameter
p_circle=lambda radius: 2 * 3.14

p_rectangle=lambda hight,weadth : 2 * (hight + weadth)

p_square=lambda side: 4 * side

#defining function using lambda functions to calculate parameter
a_circle=lambda radius: 3.14 * radius * radius

a_rectangle=lambda hight,weadth: hight * weadth

a_square=lambda side: side * side

#this is a greeting massage to user
print("welcome to calculator")

#this is a main manu of the calculation system
while True:
  print("\nmain")
  print("1.simple calculator")
  print("2.parameter calculator")
  print("3.area calculator")
  print("4.exit")
  option1=int(input("enter your option 1,2,3,4"))

#this is a manu of simple calculation
  if option1 == 1:
    print("\nyou enterd in simple calculator ")
    print("1.addition")
    print("2.substration")
    print("3.multiplicatio")
    print("4.division")
    print("5.exit")
    option2=int(input("enter your option 1,2,3,4,5"))

    if option2 ==1:
      print("\naddition")
      a=float(input("1st num"))
      b=float(input("2nd num"))
      add(a,b)
    elif option2==2:
      print("\nsubstration")
      a=float(input("1st num"))
      b=float(input("2nd num"))
      sub(a,b)

    elif option2==3:
      print("\nmultipliction")
      a=float(input("1st num"))
      b=float(input("2nd num"))
      mul(a,b)

    elif option2==4:
      print("\ndivision")
      a=float(input("1st num"))
      b=float(input("2nd num"))
      div(a,b)

    elif option2==5:
      print("\nyou exited")
      break
    else:
      print("ohh ! you enterd wrong option")

#this is a manu of parameter calculation
  if option1 == 2:
    print("\nyou enterd parameter calculator")
    print("1.circle")
    print("2.rectangle")
    print("3.square")
    print("4.exit")
    option3=int(input("enter your option 1,2,3,4,5"))

    if option3 == 1:
      print("\n parameter of circle")
      radius=float(input("enter the radius"))
      print("the parameter of circle is :",a_circle(radius))

    elif option3 == 2:
      print("\n parameter of rectangle")
      hight=int(input("enter the hight"))
      weadth=int(input("enter the weadth"))
      print("the parameter of rectangle is :",p_rectangle(hight,weadth))

    elif option3 == 3:
      print("\n parameter of square")
      side=int(input("enter side "))
      print("the parameter of square is :",p_square(side))

    elif option3 == 4:
      print("you exited")
      break
    else :
      print(" ohh ! you enterd wrong option")

#this is a manu of area calculation
  if option1 == 3:
    print("\nyou enterd area calculator")
    print("1.circle")
    print("2.rectangle")
    print("3.square")
    print("4.exit")
    option4=int(input("enter your option 1,2,3,4,5"))

    if option4 == 1:
      print("\n area of circle")
      radius=float(input("enter the radius"))
      print("area of circle is :",a_circle(radius))

    elif option4 == 2:
      print("\n area of rectangle")
      hight=int(input("enter the hight"))
      weadth=int(input("enter the weadth"))
      print("the area of rectangle is :",a_rectangle(hight,weadth))

    elif option4 == 3:
      print("\n area of square")
      side=int(input("enter the side"))
      print("the area of square is :",a_square(side))

    elif option4 == 4:
      print("you exited")
      break
    else :
      print(" ohh ! you enterd wrong option")

#this is a ending with the massage
  elif option1 == 4:
    print("you exited")
    print("thank you !")
    break
  else:
    print("ohh ! you entered wrong choice")