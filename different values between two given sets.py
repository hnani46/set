.....
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
.....
coed:
......

set1_input = input("Enter the first set of values separated by space: ")
set1 = set(map(int, set1_input.split()))


set2_input = input("Enter the second set of values separated by space: ")
set2 = set(map(int, set2_input.split()))


difference = set1 - set2


output = ' '.join(map(str, sorted(difference)))
print("Output values:", output)
....
output:
......
Enter the first set of values separated by space: 1 2 3 4
Enter the second set of values separated by space: 2 4 6 8 
Output values: 1 3

=== Code Execution Successful ===
