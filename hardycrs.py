import draw as draw
import numpy as np

    
np.r1=[1,3,2]
np.r2=[2,1,3]
value_of_r1=3
np.discharge_at_node= [100,-25,-75,0]
a= np.discharge_at_node[0]/2
c1=(a+np.discharge_at_node[1])/2
d=-a   
c2=-c1
b=c1
e=-(c1-d+np.discharge_at_node[3])
np.flow_rate_in_pipe2=[b,e,c2]

np.flow_rate_in_pipe1=[60,15,-40]
np.flow_rate_in_pipe2=[20,-55,-15]
for i in range(1,5):
    
    np.head_lossx=np.multiply(np.r1,np.flow_rate_in_pipe1)
    np.head_loss1=np.multiply(np.head_lossx,np.flow_rate_in_pipe1)
    
    np.ratio1= np.divide(np.head_loss1,np.flow_rate_in_pipe1)
    np.ratio1=np.absolute(np.ratio1)
    for ii in range(3):
        if np.flow_rate_in_pipe1[ii]<0:
            np.head_loss1[ii]=-np.head_loss1[ii]
     
    np.head_lossx=np.multiply(np.r2,np.flow_rate_in_pipe2)
    np.head_loss2=np.multiply(np.head_lossx,np.flow_rate_in_pipe2)
    np.ratio2= np.divide(np.head_loss2,np.flow_rate_in_pipe2)
    np.ratio2=np.absolute(np.ratio2)    
    for ii in range(3):
        if np.flow_rate_in_pipe2[ii]<0:
            np.head_loss2[ii]=-np.head_loss2[ii]
    dis1=np.sum(np.head_loss1)
    dis2=np.sum(np.head_loss2)
    
    
    correction_factor1=-(dis1/(2*np.sum(np.ratio1)))
    correction_factor2=-(dis2/(2*np.sum(np.ratio2)))
    np.flow_rate_in_pipe1=np.flow_rate_in_pipe1+correction_factor1
    np.flow_rate_in_pipe2=np.flow_rate_in_pipe2+correction_factor2

    np.flow_rate_in_pipe1[1]=np.flow_rate_in_pipe1[0]+np.discharge_at_node[1]-np.flow_rate_in_pipe2[0]
    np.flow_rate_in_pipe2[2]=-np.flow_rate_in_pipe1[1]
    
    np.q=[np.flow_rate_in_pipe1[0],np.flow_rate_in_pipe2[0],np.flow_rate_in_pipe2[1],np.flow_rate_in_pipe1[2],np.flow_rate_in_pipe1[1]]
    np.q=np.around(np.q,decimals=3)
#    np.q=np.absolute(np.q)
    
    draw.draw_network([0,2,4,2,0],[2,0,2,4,2],[2,2],[0,4],np.q)
    
     
print(np.flow_rate_in_pipe1)
print(np.flow_rate_in_pipe2)    

