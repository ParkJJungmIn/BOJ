n = int(input())

def hanoi( n, left , mid, right ):
   # 종료시점 만들기
   if n == 1:
      print(left, right)
      return
   
   hanoi(n-1, left , right, mid)
   hanoi(1, left, mid, right)
   hanoi(n-1, mid, left, right) 


print(2**n-1)
if n <= 20:
   hanoi(n,1,2,3)
