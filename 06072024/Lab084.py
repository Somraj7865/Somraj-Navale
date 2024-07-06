# #Read from file which is at another location

file=open(r"C:\Users\Admin\PycharmProjects\pythonProject6\06072024\somraj.txt", 'r')
content=file.read()
print(content)
file.close()

#or

file_path = r"C:\Users\Admin\PycharmProjects\pythonProject6\06072024\somraj.txt"
file = open(file_path, 'r')
content = file.read()
print(content)
file.close()
