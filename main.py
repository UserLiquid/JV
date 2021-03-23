loop = 0

"""
I know nothing special. But it's my first try xd
"""

if loop == 0:
  while loop < 100:
    file = open("Loop ma boy" + str(loop) + ".txt", "x") 
    file.write("Fuck you\n " * 1000000) 
    loop += 1 
    file.close() 
else:
  print("***It look like value i is already full/deleted***")
