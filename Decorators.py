# def func1():
#      print("Akash Das")

# func2 = func1
# # del func1
# func2()



# def func1(n):
#      if n==0:
#           return print
#      if n==1:
#           return sum

# a = func1(1)
# print(a)


def dec1(func1):
     def nowexc():
          print("Ext now")
          func1()
          print("Exted")
     return nowexc

@dec1
def a():
     print("Akash")

# a = dec1(a)
# a()

a()




