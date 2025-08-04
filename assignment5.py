#task 1
dict={'aryan': 78, 'vishal':98,'prashant':99, 'divesh': 97}
student= input(' enter the student name')

if student in dict:
    marks = dict[student]
    print( student,"'s marks :",marks)
else:
    print('student not found')



    # task 2

list=[i for i in range(1,11)]
list1=list[0:6]
print(list1)
list2=list1[::-1]
print(list2)


