attendance = [18, 20, 19, 15, 21]
#Your tasks are:
#Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
#Count how many days the class was full.
#Calculate and print the total attendance for all 5 days.
for x in attendance:
    if x>=20:
     print("Full")
    else:
     print("Not full")

print(x)

sum = 0
count = 0
for x in attendance:
 sum += x
 if x >= 20:
   count  += 1
print("Total count is",count)     
print("Total attendance " ,sum)




     
     


 
 
