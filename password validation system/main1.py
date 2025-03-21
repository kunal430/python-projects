#importing a library of re (re stands for regular expression)
import re
def pass_validation(set_password):
    #this user defined function will checks if the password fulfill the requirments
    #it will take argument as set_password

  check_password=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*])[a-zA-Z\d!@#$%&*]{6,20}$"

  return bool (re.search(check_password,set_password))

#returns in boolean data type if true when password is valid , otherwise false

def main():
  while True:
      set_password=(input("enter your password:-"))
      if pass_validation(set_password):
           print("your password is valid")
           break
      else:
           print("ohh ! your password is invallid")
           print("- Password must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit, and 1 special character.")
           print("- Password must contains characters between6 - 20.")
           print("- Password cannot be the same as the username.")
           print("please try again")



if __name__ == "__main__":
  main()



#explaination of check_password code
#(?=.*[a-z]): check if at least one lowercase letter.
#(?=.*[A-Z]): check if at least one uppercase letter.
#(?=.*\d): check if at least one digit.
#(?=.*[!@#$%&*]): check if at least one special character.
#[a-zA-Z\d!@#$%&*]{6,20}: Matches the password pattern (6-20 characters).
