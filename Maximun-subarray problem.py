#the maximum-subarray problem solved by recurrence

def Find_Max_Crossing_Subarray(A, low, mid, high):
    left_sum = 0
    sum = 0
    max_left = mid
    left_len = mid - low +1
    for i in range(0, left_len-1):
        sum = sum + int(A[mid-i])
        if sum > left_sum:
            left_sum = sum
            max_left = mid-i

    right_sum = 0
    sum = 0
    max_right = mid+1
    for j in range(mid+1,high):
        sum = sum + int(A[j])
        if sum > right_sum:
            right_sum = sum
            max_right = j
    print (max_left, max_right, left_sum+right_sum)
    return (max_left, max_right, left_sum+right_sum)

def Find_Maximum_Subarray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid = (high+low)/2
        (left_low, left_high, left_sum) = Find_Maximum_Subarray(A,low,mid)
        (right_low, right_high, right_sum) = Find_Maximum_Subarray(A,mid+1,high)
        (cross_low, cross_high, cross_sum) = Find_Max_Crossing_Subarray(A,low,mid,high)
        if int(left_sum)>int(right_sum) and int(left_sum)>=int(cross_sum):
            return (left_low, left_high, left_sum)
        elif int(right_sum)>int(left_sum) and int(right_sum)>=int(cross_sum):
            return (right_low, right_high, right_sum)
        else: return (cross_low, cross_high, cross_sum)

x = raw_input("please input the array:")
A = x.split()
(low, high, sum) = Find_Maximum_Subarray(A, 0, len(A)-1)
print "the maximum subarray is:", A[low:high+1]
print "the sum is:", sum