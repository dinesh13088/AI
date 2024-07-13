# # # # i=1
# # # # while i<10:
# # # #     i +=1
# # # #     print(i)

# # # for i in range(5):
# # #     print(i)
# marks =[22,24,89,34,22,11]
# # print(marks[1:4])
# marks.append(32)
# marks.insert(2,32)
# for score in marks:
#     print(score)

# print(24 in marks)#it checks if the corrosponding element is in the list or not and return bool value 
# print(len(marks))#it measures the length of the marks and print the number


marks =[88,87,92,97,98,100]
scores =0
while scores<len(marks):
    print(marks[scores])
    scores +=1

marks.clear()#it makes the list empty
print(marks)