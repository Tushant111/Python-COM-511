#odd even
# a=int(input())
# for i in range(1,a+1):
#  if i%2==0:
#     print("Even",i)
#  else:
#     print("Odd",i)
    
# a=int(input())
# for i in range(1,a+1):
#  if i%2==0:
#     print("Even",i)
# for i in range(0,a+1):
#     if i%2==1:
#      print("Odd",i)

for i in range(1,21):
  if(i%2==0 and i<21):
     print("Even",i)
  elif(i%2!=0 and i>10):
      j=i-10
      print("odd",j)  
