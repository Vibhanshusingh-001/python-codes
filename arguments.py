# def func(name):
#     print("hello",name)
# func("biomagician")

# DEFAULT ARGUMENTS--------------->
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# KEY ARGUMENTS---------------->
#
# name("vibhu","singh","gharwar")
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
#
# name(mname = "Peter", lname = "Wesker", fname = "Jade")

#REQUIRED ARGUMENTS---------------->
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

#
# name("Peter", "Quill","vibhu")

#VARIABLE LENGTH ARGUMENT---------------->
def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)



# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
#RETURN STATEMENT-------------->
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))

