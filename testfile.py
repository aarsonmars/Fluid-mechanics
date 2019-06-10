import draw as dw
dw.draw_plain_network([0,2,4,2,0],[2,0,2,4,2],[2,2],[0,4])    
r=[]
print('Enter the values of r for the respectives pipes 1,2,3,4,5')
for i in range(5):
    r.append(float(input("Enter value of r for pipe- {}  = ".format(i+1))))

flow=[]
i=0
print('Enter the values of in/out flow at respective nodes A,B,C,D')
for i in ('A','B','C','D'):
     flow.append(float(input('Enter value of flow for node- {}  = '.format(i))))
     