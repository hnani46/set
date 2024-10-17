......
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
.....
code:
......

input_values = input("Enter the values separated by space (including duplicates): ")


unique_values_set = set(input_values.split())


print("Number of unique elements:", len(unique_values_set))

......
output:
.......
Enter the values separated by space (including duplicates): 1 2 3 4 5 1 2 3
Number of unique elements: 5

=== Code Execution Successful ===
