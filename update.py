......
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
.......
code:
......

set1_input = input("Enter the first set of values separated by space: ")
set1 = set(map(int, set1_input.split()))


set2_input = input("Enter the second set of values separated by space: ")
set2 = set(map(int, set2_input.split()))


set1.update(set2)


output = ' '.join(map(str, sorted(set1)))
print("Updated set values:", output)

......
output:
......
Enter the first set of values separated by space: 1 2 3
Enter the second set of values separated by space: 3 4 5
Updated set values: 1 2 3 4 5

=== Code Execution Successful ===
