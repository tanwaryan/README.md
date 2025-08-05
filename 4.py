#task1
try:
    file1 = open('sample.txt', 'r')
    file_reading = file1.readlines()
    for line in file_reading:
        print(line)

    file1.close()
except FileNotFoundError:
    print('error: the file"my_file.txt" was not found')




# task 2
txt= input('enter the input')
file1= open('sample.txt', 'w')
file_writing=file1.write(txt)
file1.close()
print("data successfully  written to sample.txt")


#append data
file1= open('sample.txt','a')
append= input('enter the additional data to append')
file_append= file1.write(append)
file1.close()
# reads and dispaly
file1= open('sample.txt','r')
file_reading= file1.read()
print(file_reading)
file1.close()
print("data successfully appended")






