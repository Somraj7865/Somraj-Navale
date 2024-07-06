#File I/O

try:
  with open ('somraj1.txt','r') as file:
    print(file.read())

except FileNotFoundError as fnfe:
    print("I am not able to find the file")

finally:
    print("Closing a file")
    try:
      file.close()
    except NameError as ne:
        print(ne)