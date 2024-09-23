"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]"""

if __name__ == '__main__':
    list_one=[]
    N = int(input())
    
    for i in range(N):
        query=(input().split(" "))
        if "insert" in query:
            for item in query:
                query_pos=int(query[1])
                query_item=int(query[2])
            list_one.insert(query_pos,query_item)

        if "print" in query:
            print(list_one)
        
        if "remove" in query:
            for item in query:
                query_item=int(query[1])
            list_one.remove(query_item)
        
        if "sort" in query:
            list_one=(sorted(list_one))
        
        if "pop" in query:
            list_one.pop()

        if "reverse" in query:
            list_one.reverse()

        if "append" in query:
            for item in query:
                query_item=int(query[1])
            list_one.append(query_item)

        
#Chat GPT generated code
"""
if __name__ == '__main__':
    list_one = []
    N = int(input())  # Read the number of commands

    for i in range(N):
        query = input().split()

        # Handle each command
        command = query[0]

        if command == "insert":
            pos = int(query[1])
            val = int(query[2])
            list_one.insert(pos, val)

        elif command == "print":
            print(list_one)

        elif command == "remove":
            val = int(query[1])
            list_one.remove(val)

        elif command == "append":
            val = int(query[1])
            list_one.append(val)

        elif command == "sort":
            list_one.sort()

        elif command == "pop":
            list_one.pop()

        elif command == "reverse":
            list_one.reverse()
"""  
            

            





