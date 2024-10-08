import sys
sys.set_int_max_str_digits(999999999)
num=str(input("enter a number ").replace('enter a number ', '', 1));
if(num.isdigit()):
    num=(int(num))
    if(num>1):
        numnum=num
        for x in range(num-1):
            num-=1
            numnum = num*numnum
        print(numnum)
    elif(num<0):
        num=abs(num)
        numnum=abs(num)
        for x in range(num-1):
            num-=1
            numnum = num*numnum
        sys.set_int_max_str_digits(numnum)
        print('-'+str(numnum))
    else:
        print(num)
else:
    print("your response does not contain only numbers")