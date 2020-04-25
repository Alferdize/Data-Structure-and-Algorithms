import math


def findmaxcross(A, l, m, h):

	# Include elements on left of mid.
	sm = 0; left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + A[i]
		if (sm > left_sum):
			left_sum, max_left = sm ,i
	# Include elements on right of mid 
	sm = 0; right_sum = -1000
	for i in range(m + 1, h + 1) : 
		sm = sm + A[i] 
		
		if (sm > right_sum) : 
			right_sum, max_right = sm, i
	

	# Return sum of elements on left and right of mid 
	# returning only left_sum + right_sum will fail for [-2, 1] 
	return ( max_left, max_right,left_sum + right_sum) 


def findmaximum(A, l, h):
    if h == l:
        return (l, h, A[l])
    else:
        m = (l + h) // 2
        (left_l, left_h, left_sum) = findmaximum(A, l, m)
        (right_l, right_h, right_sum) = findmaximum(A, m+1, h)
        (cross_l, cross_h, cross_sum) = findmaxcross(A, l, m, h)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_l, left_h, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_l, right_h, right_sum)
        else:
            return (cross_l, cross_h, cross_sum)


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
l = 0
h = len(A)
print(findmaximum(A, l, h-1))
