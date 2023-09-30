no=int(input(' please enter your mark: \n'))
if no<=100 and no>=90:
    print('excellent!')
elif no<=90 and no>=80:
    print('good')
elif no<=80 and no>=70:
    print('fair')
elif no<=70 and no>=60:
    print('meets expectations')    
elif no<=60:
    print('below par')
elif no<=0:
    print('invalid option')
else:
    print('sorry! you have failed')
