text_1=input('Enter the text to write to the file: ')
file= open('output.txt','w')
file.write(text_1 + '\n')
file.close()
print('Data successfully written to output.txt.')
text_2=input('Enter the additional text to append: ')
file=open('output.txt','a')
file.write(text_2 +'\n')
file.close()
print('Data successfully appended')
print('Final content of output.txt')
file =open('output.txt','r')
print(file.read())

