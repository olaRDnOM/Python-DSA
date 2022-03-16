# Make sure you're not adding or deleting any lines of code! 
# I was stuck on this but failed to see that note in the problem description. The three changes made to this solution are:

def findZigZagSequence(a, n):
    a.sort()
    middle = int((n + 1)/2) # The mid calculation was off by 1, and needs to be shifted left (-1 added)
    a[middle], a[n-1] = a[n-1], a[middle]

    start = middle + 1
    end = n - 2 # The ed calculation needs to point at the second to last element rather than the last. 
                # This is because at the start we swapped the middle number and the largest number, 
                # meaning the middle number is already in the correct location (4 needs to be at the end).


    while(start <= end):
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1 # Finally the while loop modification of ed needs to be negative rather than positive.

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



