largest  = None
smallest = None
while True :
    num = input('Please Enter Your Number: ')
    if num =='done' :
        break
    try:
        num = int(num) 
    except: 
        print('Invalid Entry Please Try Again')
        continue
if largest is None:
    largest = num
    largest > num
    print (largest)   

if smallest is None:
    smallest = num
    smallest < num 
    print (smallest)    

print ('Maximum', largest)
print ('Minimum',  smallest)   
