import os
# Create the file if it doesn't exist
if not os.path.exists("myphonebookfile.txt"):
    with open("myphonebookfile.txt", "a+") as myfile:
        pass
#this is a greeting massage for user
print("welcome to phonebook directory\n")

#defining a function for searching a contact
def search_contact():
  search_name=input("enter 1st name for contact search-\n").upper()


  with open("myphonebookfile.txt","r") as file:
    file_contacts=file.readlines()
    found=False

    for line in file_contacts:
      if search_name in line.upper():
        print("here's the Contact info you need\n",end=" ")
        print(line)
        found= True
        break

    if not found:
      print(f"your contact {search_contact} is not available !")

#this is function used for capitlize frist letter of names created by using lambda function
capitalize_first_letter= lambda s: s[0].upper() + s[1:].lower()

#this function gets the frist name from user
def input_frist_name():
  first=input("enter first name :-")
  return capitalize_first_letter(first)

#this function gets the last name from user
def input_last_name():
  last=input("enter last name :-")
  return capitalize_first_letter(last)

#this function adds a new contact in phonebook directry
def new_contact():
  frist_name=input_frist_name()
  last_name=input_last_name()
  phone_no=input("enter phone number :-")
  email_id=input("enter email ID :-")
  contact_details=f"[ {frist_name} {last_name},{phone_no},{email_id} ]\n"


  with open("myphonebookfile.txt", "a") as file:
    file.write(contact_details)
    print("The contact details you enterd :\n"+ contact_details +"\n has been stored succesfully ")


#this function delect the specific contact
def delect_contact():
  search_name=input("enter contact name to delect").upper()

  contacts=[]
  for i,contact in enumerate(contacts):
    if search_name in contacts:
      found = True
      del contacts[i]
      break

     #this code shows the updated list
    if found:
      with open("myphonebookfile.txt","w") as myfile:
        myfile.writelines(contacts)
      print(f"The contact {search_name} is delected succesfully")
    else:
      print(f"The contact with the name {search_name} was not found ")


#main mainu function
def main():
  print("\nMAIN MENU\n")
  print("1.show all contact")
  print("2.add new contact")
  print("3.delect a contact")
  print("4.search a contact")
  print("5.exit")
  option=int(input("enter any option 1,2,3,4,5:-"))


  if option == 1:
    with open("myphonebookfile.txt","r") as myfile:
      show_contact=myfile.read()
      if show_contact == 0:
        print("There is no contact in phonebook")

      else:
        print(show_contact)

  elif option == 2:
    new_contact()

  elif option == 3:
    delect_contact()

  elif option == 4:
    search_contact()

  elif option == 5:
    print("Thank you for using phonebook directory")
  else:
    print("please enter valid option")

    print("plese enter any option to continue")
    input()
    main()


if __name__=="__main__":
  main()