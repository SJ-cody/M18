# HCF
#Take input from user
num1 = float(input(" Please Enter the First Number : "))
num2 = float(input(" Please Enter the Second Number : "))

#calculate the HCF of user entered number
while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1   
#display the result
print("HCF of num1 and num2 is",hcf)