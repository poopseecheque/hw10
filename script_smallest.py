from smallest import find_two_smallest 
import lists

result_otp = 'result.txt'
file = open(result_otp, 'w')
all_lists = [lists.l1, lists.l2, lists.l3]

for i in all_lists: 
     file.write(f'{find_two_smallest(i)}\n')
file.close()