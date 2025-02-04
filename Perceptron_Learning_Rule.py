import numpy as np
import matplotlib.pyplot as plt

w=[w1, w2]=[0.5, 1]
w=np.array(w)
b=-1
Inputs=[(0,0),(0,1),(1,0),(1,1)]
Outputs=[0,0,0,1]
def train_perceptron(Inputs, Outputs, epochs, w, b):
    plt.figure(figsize=(8, 6))
    for epoch in range(epochs):
        flag=True
        for i in range(len(Inputs)):
            X,Y=Inputs[i]; w1,w2=w
            received_output=w1*X+w2*Y+b
            if received_output>=0:
               received_output=1
            else:
               received_output=0
            e=Outputs[i]-received_output
            print(Outputs[i], received_output)
            if not e==0:
                flag=False
                w1_new=w1+e*X
                w2_new=w2+e*Y
                b_new=b+e
                w=[w1_new, w2_new]
                b=b_new                 
        x_values = np.linspace(-3, 5, 100)
        y_values = (-b - w1_new * x_values) / (w2_new)
        if flag:
            break
        plt.plot(x_values, y_values, label=f'Decision Boundary {epoch+1}')
        #if w1==w1_new and w2==w2_new:
            #break 
    plt.scatter(*zip(*Inputs[:3]), marker='o', label='Class 1')
    plt.scatter(*Inputs[3], color='red', marker='*', label='Class 2')
    plt.title('Perceptron Decision Boundary')
    plt.xlabel('Input 1')
    plt.ylabel('Input 2')
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)
    plt.legend()
    plt.grid(True)
    plt.show()

epoch=100
train_perceptron(Inputs, Outputs, epoch, w, b)   

      
                  