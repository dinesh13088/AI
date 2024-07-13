# name=input("what is yout name?")
# print("hello " +name) 
# old_age=22
# age=input("what is your age?")
# new_age=old_age+int(age)
# print(new_age)

#name ='Krishmata Tamang'
#print(name.find(' '))# it is used to find the space or it can be used to find any substring or character
#print(name.replace('Krishmata','Dinesh'))#this replace function can replace substring as well as character
#print('m' in name)# it is used to check whether the m exist in the name or not:if exist then it returns true
# age=input("enter your age:")
# age=int(age)
# if age>19:
#     print('you are eligble to vote:')
# else:
#     print("you are not eligble to vote")
first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))
operator=input('Enter the operator')

if operator=="+":
    print(first_number+second_number)
elif operator=="-":
    print(first_number-second_number)
elif operator=="/":
    print(first_number/second_number)
elif operator =="*":
    print(first_number*second_number)
else:
    print("Please make the valid choice")

