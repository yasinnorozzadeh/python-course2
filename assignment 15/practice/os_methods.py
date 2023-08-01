import os
 
# Open file
fd = os.open("file.txt", os.O_RDWR|os.O_CREAT)

#print the file system representation of a path
print (os.fspath("file.txt"))

# Duplicate File descriptor
duplicatefd = os.dup(fd)

#print both descriptors
print ("Orignal file descriptor:", fd)
print ("Duplicate file descriptor:", duplicatefd)

# Get a file object for the file
fdo = os.fdopen(fd, "w+")

# Write something on open file
fdo.write( "This is a test content for w3schools")

#Encode filename
encode = os.fsencode("file.txt")

#Print the encoded filename
print(encode)

# Close file
fdo.close()

#Print the number of CPUs
print("Number of CPUs in the system:", os.cpu_count())
