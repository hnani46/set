.......
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1 
.....
code:
......

set_input = input("Enter the set of values separated by space: ")


values_set = set(map(int, set_input.split()))


max_value = max(values_set)
min_value = min(values_set)


print("Maximum:", max_value)
print("Minimum:", min_value)
......
output:
.....
Enter the set of values separated by space: 1 2 3
Maximum: 3
Minimum: 1

=== Code Execution Successful ===
