

file1 = open("/media/usr/Volume/Users/usr/Desktop/Pay2Win/DB/Log.txt","a")

file1.writelines("\ntest")

file1.close()


file1 = open("/media/usr/Volume/Users/usr/Desktop/Pay2Win/DB/Log.txt","r")

print(file1.readlines())

file1.close()
