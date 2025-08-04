#task1
file1= open('sample.txt','r')
file_reading= file1.read()
print(file_reading)
file1.close()

# handle error
try:
    file1= open('my_file.txt','r')
    file_reading= file1.read()
    print(file_reading)
    file1.close()
except FileNotFoundError:
    print('error: the file"my_file.txt" was not found')

# task 2
txt= input('enter the input')
file1= open('sample.txt', 'w')
file_writing=file1.write(txt)
file1.close()
file1= open('sample.txt','r')
file_reading= file1.read()
print(file_reading)
file1.close()

#append data
file1= open('sample.txt','a')
file_append= file1.write('jai shree ram')
file1.close()

# reads and dispaly
file1= open('sample.txt','r')
file_reading= file1.read()
print(file_reading)
file1.close()






