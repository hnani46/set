.....
 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
.....
code:
.......

input_values = []


n = int(input("Enter the number of values: "))


print("Enter the values (one per line):")
for _ in range(n):
    value = input()
    input_values.append(value)


value_count = {}
for value in input_values:
    if value in value_count:
        value_count[value] += 1
    else:
        value_count[value] = 1


duplicate_count = sum(count - 1 for count in value_count.values() if count > 1)


unique_values_set = set(input_values)


print("Duplicate Values:", duplicate_count)
print(' '.join(sorted(unique_values_set, key=int)))

......
output:
.......
Enter the number of values: 6
Enter the values (one per line):
1
2
1
6
2
3
Duplicate Values: 2
1 2 3 6

=== Code Execution Successful ===
