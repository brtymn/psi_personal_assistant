import matplotlib.pyplot as plt


def plot_single_file(path_to_file):

    f=open(path_to_file, "r")

    lines=f.readlines()

    l1=[]
    l2=[]

    for x in lines:
        l1.append(x.split(' ')[0])
        l2.append(x.split(' ')[1])

        f.close()

    x_axis_str = [i.replace('\n','') for i in l1]
    y_axis_str = [i.replace('\n','') for i in l2]

    x_axis = [float(number1) for number1 in x_axis_str]
    y_axis = [float(number2) for number2 in y_axis_str]

    plt.plot(x_axis, y_axis)

    plt.xlabel('First Cloumn')
    plt.ylabel('Second Cloumn')

    plt.show()
