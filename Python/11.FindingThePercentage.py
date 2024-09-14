"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50"""


if __name__ == '__main__':
    
    n = int(input())    #here you will input the number of names you will be taking as input
    student_marks = {} #Here you will initialise a dictionary
    for _ in range(n): #here you will create a loop to take the var provided in teh output cli and map them to the dict var
        name, *line = input().split()   # here you are trying to split the input and store it into name and *line
        scores = list(map(float, line)) # here the float valies are mapped to the list scores
        student_marks[name] = scores # here the values var is mapped to key Var that is name
    query_name = input() # here the query name is the one where you find out the averge marks for that person
    

    

    def student_marks_for_student(query_name):
        sum_of_scores=0
        marks_count=0
        
        for item in student_marks[query_name]:
            sum_of_scores+=item
            marks_count+=1
        return "{:.2f}".format(sum_of_scores/marks_count)         
            
                      
    student_marks_for_student(query_name)

    print(f"The total avg of the score for the student\
        {query_name} is {student_marks_for_student(query_name)}") #n

    #print(student_marks)


