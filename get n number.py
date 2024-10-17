.....
1) Write a program to get n number of values in separate line for set and print the values with space separation.
...
code:
....
n = int(input("Enter the number of values: "))
values_set = set()
print("Enter the values (one per line):")
for _ in range(n):
    value = input()
    values_set.add(value)
output = ' '.join(sorted(values_set))
print("Output values:", output)
....
output:
....
Enter the number of values: 5
Enter the values (one per line):
3
1
4
6
3
Output values: 1 3 4 6
