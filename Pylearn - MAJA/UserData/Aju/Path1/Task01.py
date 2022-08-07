#create a max_newtion to find maximum value in an array
#don't use inbuilt max_newtion
#sample 1 -> max_new([1,2,3,4,5])
#sample 1 output -> 5
#sample 2 -> max_new([7,8,9,1,2,3])
#sample 2 output -> 9

def max_new(*arr):
	arr = list(arr)
	#enter your code here
	mx=arr[0]
	for i in range(1,len(arr)):
		if arr[i]>mx:
			mx =arr[i]
	return mx
	pass
