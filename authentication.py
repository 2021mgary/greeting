# user input
name = input("what is your name? ")
password = input("what is your password? ")

# control flow
# two equals signs means "do these two things match?""
if name == "michaela" and password == "mkaydagoat":
  print("wassup mkay kay")
elif name == "michaela":
  print("yo michaela, that's not the right password. try again")
  password = input("try another password ")
  if password == "mkaydagoat":
    print("that's correct!")

# not michaela, print greeting
else:
  print("hello, " + name)

question2 = input("do you eat ice cream?")
question1 = input("what's your favorite type?")

if question1 == "yes" and question2 == "cookies and cream":
 print("ohhhh tasty")
elif question1 == "yes":
    print("no way, you're lying")
    question1 = input("tell the truth")
    if question1 == "yes":
        print("i knew it")