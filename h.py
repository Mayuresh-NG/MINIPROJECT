

f = open("note.txt","r")


def check():
   cnt=0
   li = list(line.split(" "))
   if '@' in li:
      cnt = cnt+1
   if cnt>=2:
      print("Error")


for line in f:
   if '@' in line:
      cnt = 0
      li = list(line.split(" "))
      for i in li:
         if i == '@':
            cnt = cnt + 1
      if cnt>=2:
         print("Error")
      else:
         print(line)

   else:
      print("Error")

f.close()

