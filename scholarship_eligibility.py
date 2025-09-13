print('SCHOLARSHIP BY GOVERNMENT OF INDIA')
print("Enter the marks obtained in Maths, Physics, Chemistry: ")
maths=int(input('Maths: '))
phy=int(input('Physics: '))
chem = int(input('Chemistry: '))
if maths<=0 or phy<=0 or chem <= 0:
  print('Invalid!')
average = (maths+phy+ chem)/3;
print('Average mark obtained in maths, physics and chemistry : ',average)
first_grad=int(input('Are you the first graduate in your family?(1 for Yes, 0 for No): '))
if average >= 98 and first_grad == 1:
  print('Eligible for Scholarship.')
else:
  print('Not Eligible.')