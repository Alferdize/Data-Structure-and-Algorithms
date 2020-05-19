def doIt(arr,n,k):
	arr.sort()
	min = arr[0]+arr[n-1]
	max = arr[0]+arr[n-1]

	for i,j in zip(range(0,(n//2),1), range(n-1,(n//2)-1,-1)):
		if(min > (arr[i]+arr[j])):
			min = arr[i]+arr[j]
		if(max < arr[i]+arr[j]):
			max = arr[i]+arr[j]
	diff = max-min
	print(diff)
	if(diff < k):
		print("Chick magnet Jhool!")
	elif(diff == k):
		print("Lucky chap!")
	elif(diff > k):
		print("No more girlfriends!")

def main():
	ntc = int(input())
	for i in range(0,ntc):		
		n,k = list (map (int ,input ().split(" ")))
		arr = list (map(int, input("").split(" ")))
		doIt(arr,n,k)

if __name__ == "__main__":
	main()