            Armstrong number in interval
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    temp=i
    s=0
    while(temp>0):
       
        r=temp%10
        s+=r**3
        temp//=10
    if(i==s):
        print(i)
            Armstrong Number
n=int(input())
t=n
s=0
while(t>0):
    r=t%10
    s+=r**3
    t//=10
if(n==s):
    print("Yes")
else:
    print("No")
   (when testcase is not passed go to next one)            
            OR
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int n,r,sum=0,t;
    scanf("%d",&n);
    t=n;
    int c=0;
    while(t>0)
    {
        t/=10;
        ++c;
    }
    t=n;
    while(t>0)
    {
        r=t%10;
        sum=sum+pow(r,c);
        t=t/10;
    }
    if(n==sum)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }
    return 0;
}
Tom is working in a shop where he labels items. Each item is labelled with a number between num1 and num2(both inclusive). Since Tom is also a natural mathematician, he likes to observe patterns in numbers. Tom could observe that some of these label numbers are divisible by other label numbers.

Write a Python function to find out those label numbers that are divisible by another label number and display how many such label numbers are there totally.

Note:- Consider only the distinct label numbers. The list of those label numbers should be considered as a set.
def check_numbers(num1,num2):
    num_list=set()
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.add(i)
    count=len(num_list)
    return [num_list,count]
num1,num2=map(int,input().split())
print(check_numbers(num1, num2))
                  Reverse A Digit
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    long int n,r;
    long sum=0;
    scanf("%ld", &n);
    while(n>0)
    {
        r=n%10;
        sum=(sum*10)+r;
        n=n/10;
    }
    printf("%ld",sum);
    return 0;
}
                  Product Of Digit
n=int(input())
p=1
while(n>0):
    p*=n%10
    n//=10
print(p)
              fibonoci series
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n,a=0,b=1,c;
    scanf("%d", &n);
    for(int i=0;i<n;i++)
    {
        printf("%d ",a);
        c=a+b;
        a=b;
        b=c;
    }
    
    return 0;
}
                 infyfriday
def palindrome(a,c):
    a=str(a)
    r=str(a)
    r=r[::-1]
    if(r==a):
        print(c,a)
    else:
        c+=1
        a=int(a)+int(r)
        palindrome(a,c)
p=input()
palindrome(p,0)

          Romon To Dcimal
def star(r):
    if(r=='I'):
        return 1
    if(r=='V'):
        return 5 
    if(r=='X'):
        return 10
    if(r=='L'):
        return 50
    if(r=='C'):
        return 100
    if(r=='D'):
        return 500
    if(r=='M'):
        return 1000
    return -1
def RoToDe(s):
    r=0
    i=0
    while(i<len(s)):
        s1=star(s[i])
        if((i+1)<len(s)):
            s2=star(s[i+1])
            if(s1>=s2):
                r+=s1
                i+=1
            else:
                r+=s2-s1
                i+=2
        else:
            r+=s1
            i+=1
    return r
s=input()
print(RoToDe(s))

            Replace each value in a list with twice the preceding value (and the first value with 0)
            
number=list(map(int,input().split()))
print(0,end=" ")
for i in range(1,len(number)):
    print(number[i-1]*2,end=" ")            
 r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+','+str(j)
        n.append(temp)
    l.append(n)
print("[",end="")
print(*l,sep=',\n',end="")
print("]")  
Sample Input 0

4 3
Sample Output 0

[['0,0', '0,1', '0,2'],
['1,0', '1,1', '1,2'],
['2,0', '2,1', '2,2'],
['3,0', '3,1', '3,2']]
              Balanced Brackets
def isvalid_pair(left,right):
    if(left=="(" and right==")"):
        return True
    if(left=="{" and right=="}"):
        return True
    if(left=="[" and right=="]"):
        return True
    return False
def isBalanced(s):
    stack=[]
    for symbol in s:
        if(symbol=="(" or symbol=="{" or symbol=="["):
            stack.append(symbol)
        else:
            if(len(stack)==0):
                return False
            last=stack.pop()
            if not isvalid_pair(last,symbol):
                return False
    if(len(stack)!=0):
        return False
    return True
n=int(input())
for _ in range(n):
    s=input()
    if isBalanced(s):
        print("YES")
    else:
        print("NO")
