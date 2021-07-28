'''2 4 10 10 10 18 20
Enter the key : 10
O/P : 3'''
def binarySearch(arr, l, r, x):
	if (r < l):
		return -1

	mid = int( l + (r - l) / 2)

	# If the element is present
	# at the middle itself
	if arr[mid] == x:
		return mid

	# If element is smaller than
	# mid, then it can only be
	# present in left subarray
	if arr[mid] > x:
		return binarySearch(arr, l,
							mid - 1, x)

	# Else the element
	# can only be present
	# in right subarray
	return binarySearch(arr, mid + 1,
								r, x)

# Returns number of times
# x occurs in arr[0..n-1]
def countOccurrences(arr, n, x):
	ind = binarySearch(arr, 0, n - 1, x)

	# If element is not present
	if ind == -1:
		return 0

	# Count elements
	# on left side.
	count = 1
	left = ind - 1
	while (left >= 0 and
		arr[left] == x):
		count += 1
		left -= 1

	# Count elements on
	# right side.
	right = ind + 1;
	while (right < n and
		arr[right] == x):
		count += 1
		right += 1

	return count
arr = list(map(int,input().split( )))
n = len(arr)
x = int(input("Enter the key : "))
print(countOccurrences(arr, n, x))
