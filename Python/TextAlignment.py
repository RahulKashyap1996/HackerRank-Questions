"""In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
.center(width)

This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
.rjust(width)

This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

Constraints

The thickness must be an odd number.

Output Format

Output the desired logo.

Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H """

# Write your code here the answer is at line 100 
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

print(('H'*1).rjust(n,' '))
print(('H'*3).rjust(n+1,' '))
print(('H'*5).rjust(n+2,' '))
print(('H'*7).rjust(n+3,' '))
print(('H'*9).rjust(n+4,' '))

print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))
print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))
print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))
print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))
print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))
print(('H'*n+" "*(3*n)+'H'*n).rjust(n*6-3,' '))

print(('H'*(n*n+n-2)).rjust(n*6,' '))
print(('H'*(n*n+n-2)).rjust(n*6,' '))
print(('H'*(n*n+n-2)).rjust(n*6,' '))

print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))
print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))
print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))
print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))
print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))
print(('H'*n+" "*n*3+'H'*n).rjust(n*(n+1)-(n-2),' '))

print(('H'*1).rjust(n*n,' '))
print(('H'*3).rjust(n*n+1,' '))
print(('H'*5).rjust(n*n+2,' '))
print(('H'*7).rjust(n*n+3,' '))
print(('H'*9).rjust(n*n+4,' '))



























