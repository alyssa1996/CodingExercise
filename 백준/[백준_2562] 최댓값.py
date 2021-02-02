max_num,max_index=(0,0)
for i in range(9):
    num=int(input())
    if num>max_num:
        max_num=num
        max_index=i
        
print(max_num)
print(max_index+1)
