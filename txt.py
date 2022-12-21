

file1 = open("/media/Dave/Volume/Users/david/Desktop/Pay2Win/DB/Log.txt","a")

file1.writelines("\ntest")

file1.close()


file1 = open("/media/Dave/Volume/Users/david/Desktop/Pay2Win/DB/Log.txt","r")

print(file1.readlines())

file1.close()