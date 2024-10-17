.....
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
.....
code:
......

set1_input = input("Enter the first set of values separated by space: ")
set1 = set(map(int, set1_input.split()))


set2_input = input("Enter the second set of values separated by space: ")
set2 = set(map(int, set2_input.split()))


common_values = set1.intersection(set2)


output = ' '.join(map(str, sorted(common_values)))
print("Common values:", output)
.......
output:
.....
Enter the first set of values separated by space: 1 2 3 4
Enter the second set of values separated by space: 2 4 6 8
Common values: 2 4

=== Code Execution Successful ===
