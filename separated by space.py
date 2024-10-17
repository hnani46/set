......
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5

....
code:
.....
input_values = input("Enter the values separated by space: ")
values_set = set(input_values.split())
sorted_values = sorted(map(int, values_set))
print("Output values:", ' '.join(map(str, sorted_values)))
......
output:
.....
Output values: 1 2 3 4 5
