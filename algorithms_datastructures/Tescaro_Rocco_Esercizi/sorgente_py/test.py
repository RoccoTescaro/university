from ordered_list import *
from binary_tree import *
from os_tree import *
import random
import numpy
import matplotlib.pyplot as plt

random.seed()
size = 1000
dd = 10
dims = [dd*(x+1) for x in range(size//dd)]
n_try = 500

actual_results = numpy.zeros([3, 2, 2, n_try])

avg = numpy.zeros([len(dims),3,2,2])
std = numpy.zeros([len(dims),3,2,2])

if input("Do you want to load the previous results? (y/n) ") == "n":
    for j, dim in enumerate(dims):

        for k in range(n_try):
            dss = []
            dss.append(ordered_list())
            dss.append(binary_tree())
            dss.append(os_tree())
            
            for _ in range(dim+1):
                value = random.randint(1,dim)
                dss[0].add(ol_node(value))
                dss[1].add(bt_node(value))
                dss[2].add(os_node(value))
        
            value = random.randint(1,dim)
            
            for i, ds in enumerate(dss):
                s_result = ds.test_os_select(value)
                r_result = ds.test_os_rank(ds.os_select(value))
                #avg[j][i][0] += s_result
                #avg[j][i][1] += r_result
                actual_results[i][0][0][k] = s_result[0]
                actual_results[i][0][1][k] = s_result[1]
                actual_results[i][1][0][k] = r_result[0]
                actual_results[i][1][1][k] = r_result[1]
                
        for i in range(3):
            for k in range(2):
                for l in range(2):
                    avg[j][i][k][l] = numpy.mean(actual_results[i][k][l])
                    std[j][i][k][l] = numpy.std(actual_results[i][k][l])

        print("Dimension: ", dim)

    numpy.save("avg.npy", avg)
    numpy.save("std.npy", std)
else:
    avg = numpy.load("avg.npy")
    std = numpy.load("std.npy")


p = 14
d = [p*dd*(x+1) for x in range((size//(p*dd))-1)]
dss = ['ordered_list', 'binary_tree', 'os_tree']

def draw_graph(style, color, algorithm, analysis):
    c = ['r', 'g', 'b', 'k']
    lw = 1.5
    fig, axes = plt.subplots(2, 2, figsize=(7.5, 6.5))
    for i, ds in enumerate(dss):
        data = [avg[dim][i][algorithm][analysis] for dim in range(0,len(dims))]
        axes[i//2][i%2].plot(dims, data, style, color = c[i] if color else c[3], linewidth=lw)
        axes[i//2][i%2].plot(d, [avg[p*x-1][i][algorithm][analysis] for x in range(1,(size//(p*dd)))], 'o', color = c[i] if color else c[3], linewidth=lw)
        axes[1][1].plot(dims, data, style, color = c[i] if color else c[3], label=ds, linewidth=lw)
        axes[i//2][i%2].title.set_text(ds)
        axes[i//2][i%2].grid(True, linestyle=':', alpha=0.5)
    
    axes[1][1].grid(True, linestyle=':', alpha=0.5)
    if color: 
        axes[1][1].legend()
    plt.tight_layout()
    plt.show()
  

draw_graph('-', True, 0, 1)
draw_graph('-', False, 0, 0)
draw_graph('-', True, 1, 1)
draw_graph('-', False, 1, 0)

for i in range(3):
    for x in range(1, (size//(p*dd))):
        print( p*x*dd, "&", 
              '%.2f' % avg[p*x-1][i][0][1], "&", 
              '%.2f' % avg[p*x-1][i][0][0], "&",
              '%.2f' % std[p*x-1][i][0][1], "&", 
              '%.2f' % avg[p*x-1][i][1][1], "&", 
              '%.2f' % avg[p*x-1][i][1][0], "&",
              '%.2f' % std[p*x-1][i][1][1], "\\\\")


"""
for x in range(87,100):t
    print(x)
    print(avg[x][2][0][1])
    print(avg[x][2][0][0])
    print()
    print(std[x][2][0][1])
    print(std[x][2][0][0])
    print()
"""