"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""

"""Code with Explanation of each step


    if __name__ == '__main__':  # This condition ensures that the code runs only when this script is executed directly, not when it's imported as a module.
    n = int(input())  # Reads an integer input from the user, which represents the number of elements in the list.
    
    # Reads the next line of input as space-separated integers, maps them to int, and converts the result to a list.
    arr = map(int, input().split())  # 'map' applies the int() function to each input, converting strings to integers.
    arr = list(arr)  # Converts the map object to a list of integers.

    # Initialize 'Snd_Max' with the smallest value in the list.
    # This will track the second largest number in the array.
    Snd_Max = min(arr)  # 'min(arr)' finds the smallest value in the list, so 'Snd_Max' starts as the minimum value.

    # Find the maximum value in the list. This will be the largest number in the list.
    max_value = max(arr)  # 'max(arr)' finds the largest number in the list.

    # Loop through each element of the array 'arr' by index to compare its value.
    for i in range(len(arr)):  # 'len(arr)' gives the total number of elements in the list, and 'i' is the index for each element.
        
        # This condition checks if the current element is:
        # 1. Greater than 'Snd_Max' (the current second largest candidate).
        # 2. Not equal to 'max_value' (so we exclude the largest value).
        if int(arr[i]) > Snd_Max and arr[i] != max_value:  
            Snd_Max = arr[i]  # Update 'Snd_Max' to the current element if both conditions are met.
    
    # After the loop, 'Snd_Max' will hold the second largest value.
    print(Snd_Max)  # Prints the second largest number in the list.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    Snd_Max=min(arr)
    max_value=max(arr)
    for i in range(len(arr)):    
       if int(arr[i])>Snd_Max and arr[i]!=max_value:
           Snd_Max=arr[i]

           
    print(Snd_Max)

    