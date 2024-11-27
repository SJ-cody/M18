# Right angled triangle
#Take input
print(" Pyramid Pattern of Stars in right angle shape(*):")
n = int(input("enter the number of rows you want to print/ display: "))
#outer loop to handle number of rows
for i in range(n): 
  #inner loop to handle number of columns
    for j in range(i+1):
      #display result
        print("* ", end="")
    print()