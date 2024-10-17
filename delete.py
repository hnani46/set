.......
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
......
code:
.....

set_input = input("Enter the set of values separated by space: ")
values_set = set(map(int, set_input.split()))


element_to_delete = int(input("Enter the element to delete: "))


if element_to_delete in values_set:
    values_set.remove(element_to_delete)
    
    output = ' '.join(map(str, sorted(values_set)))
    print("Updated set values:", output)
else:
    print("Given value is not present in the set list.")

.....
output:
......
Enter the set of values separated by space: 1 2 3 4
Enter the element to delete: 2
Updated set values: 1 3 4

=== Code Execution Successful ===
