#Question: create a replace_newtion similiar to existing inbuilt replace replace_newtion
#using inbuilt replace replace_newtion will cause fail,should return output string
#sample test case
# TC01 : replace_new('This is india','is','was')
# Output -> 'This was india'
# TC02 : replace_new('This area is too cool.isn't this?','is','was')
# Output -> 'This area was too cool,wasn't this?'
def replace_new(string,change_str,new_str):
    #enter your code here
    new_string = ''
    i=0
   
    while i<len(string)-len(change_str)+1:
        if string[i:i+len(change_str)] == change_str:
            
            new_string+=new_str
            i+=len(change_str)
        else:
            new_string+=string[i]
            i+=1
        val = -1
    if string[val:]!=change_str:
            new_string+=string[val:]
     
     
    return new_string


print(replace_new('Hii','i','j'))
