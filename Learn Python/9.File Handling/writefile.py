f = open("message.txt", "w")
f.write(" I am so happy now!!")
f.close

open_file = open("message.txt", "r")
print(open_file)
open_file.close