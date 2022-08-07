#given an integer, add one to all its even digit values and make all digits odd
#using of inbuit str convertertion will fail
#sample testcase 1 -> 123456
#sample output 1 -> 133557
#sample testcase 2 -> 4444
#sample output 2 -> 5555


def converter(number):
    #write your code here
    num=0
    j=0
    while number>0:
        a = number%10
        if a%2 == 0 :
            a+=1
        num+=a*(10**j)
        number//=10
        j+=1
    return num
    
        
    pass
