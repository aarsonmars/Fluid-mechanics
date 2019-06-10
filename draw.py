import matplotlib.pyplot as plt

def draw_network(x,y,x1,y1,q):
    
    
    fig=plt.figure(figsize=(11,7))
    ax = fig.add_subplot()
    plt.plot(x,y,label='single pipe')
    plt.plot(x1,y1,label='common pipe')
    ax.text(-0.2,2.2,'A',fontsize=17)
    ax.text(2,-0.4,'C',fontsize=17)
    ax.text(4.2,2,'D',fontsize=17)
    ax.text(1.9,4.2,'B',fontsize=17)
    
    plt.text(0.5,2.7, '$Q_1=$'+str(q[0]), fontsize=16,rotation=30, rotation_mode='anchor')
    plt.text(2.5,3.7, '$Q_2=$'+str(q[1]), fontsize=16,rotation=330, rotation_mode='anchor')
    plt.text(2.7,0.2, '$Q_3=$'+str(q[2]), fontsize=16,rotation=33, rotation_mode='anchor')
    plt.text(0.5,1.1, '$Q_4=$'+str(q[3]), fontsize=16,rotation=325, rotation_mode='anchor')
    plt.text(1.9,1.2, '$Q_5=$'+str(q[4]), fontsize=16,rotation=90, rotation_mode='anchor')
    plt.legend(loc='best')
    plt.arrow(2,4,0.15,0.15,head_width=0.05)
    plt.arrow(-0.2,2,0.15,0,head_width=0.05)
    plt.arrow(2,0,0.15,0,head_width=0.05)
    plt.arrow(4,2,0.1,0.15,head_width=0.05)
    ax.text(-0.8,2,'100$m^3/s$',fontsize=15)
    ax.text(2.2,4.2,'25$m^3/s$',fontsize=15)
    ax.text(4.2,2.2,'75$m^3/s$',fontsize=15)
    ax.text(2.2,0,'0$m^3/s$',fontsize=15)        
                    
    plt.axis('off')
    plt.show()
    


def draw_plain_network(x,y,x1,y1):
    fig=plt.figure(figsize=(11,7))
    ax = fig.add_subplot()
    plt.plot(x,y,label='single pipe')
    plt.plot(x1,y1,label='common pipe')
    ax.text(-0.2,2.2,'A',fontsize=17)
    ax.text(2,-0.4,'C',fontsize=17)
    ax.text(4.2,2,'D',fontsize=17)
    ax.text(1.9,4.2,'B',fontsize=17)
    plt.text(1,3.1, '$1$', fontsize=16,rotation=30, rotation_mode='anchor')
    plt.text(3,3.1, '$2$', fontsize=16,rotation=330, rotation_mode='anchor')
    plt.text(3,0.7, '$3$', fontsize=16,rotation=33, rotation_mode='anchor')
    plt.text(0.6,0.9, '$4$', fontsize=16,rotation=325, rotation_mode='anchor')
    plt.text(1.9,2, '$5$', fontsize=16,rotation=90, rotation_mode='anchor')
    plt.axis('off')
    plt.show()