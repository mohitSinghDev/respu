# # your code goes here
# def maxPro(arr,n):
# 	product=0
# 	for i in range (n):
# 		for j in range(i+1,n):
#             (arr[i]*(n+1))
# 			product = product + (arr[i]*(j+1))%10^9+7
# 	return product
		
		
# if __name__=="__main__":
# 	arr = [1,2,3]
# 	n=len(arr)
# 	print(maxPro(arr,n))
	
		
n = int(input())
a = list(map(int,input().split()))
ans= 1
for i in a:
    ans = (ans*(i**(n+1)))%1000000007
print(ans)             