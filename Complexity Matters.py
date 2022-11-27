import matplotlib.pyplot as plt
import numpy as np

# Assignment: Complexity Matters (Optional Project)
# Name: Julius Broomfield
# Class: CSc 2510 

class LineChart():
    def __init__(self, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel("n")
        plt.ylabel("Time in Seconds")
    
    def plot(self, label, xdata, ydata, size, degree = 1, annotate = False):
        self.xdata, self.ydata = xdata, ydata

        #Finding Line of Best Fit
        if isinstance(degree, int):
            model = np.poly1d(np.polyfit(xdata, ydata, degree))
        #Adjusting for Exponential Model
        else:
            m, b = np.polyfit(xdata, np.log(ydata), 1)

        #Plotting Scatter Points
        plt.scatter(xdata, ydata, alpha = 0.5)

        #Plotting Best Fit Line
        if isinstance(degree, int):
            plt.plot(xdata, model(xdata), label = label)
        else:
            ydata = list(map(lambda x: np.exp(b) * np.exp(x * m), xdata))
            plt.plot(xdata, ydata, label = label)

        #Will print y-value of each point
        if annotate:
            for i, x in enumerate(self.xdata):
                plt.annotate(self.ydata[i], (x, self.ydata[i]))
        

    def display(self):
        #Adds Legend
        plt.legend()

        #Displays Points
        plt.show()

        #Clears Plot
        plt.clf()

'''
Task 1:
Using Bridges LineChart object, plot the runtime of an algorithm for problem size 
ranging from 1 to 10^5.(Don't use all values of n, take some values in the middle.)

1. 10^4 n instructions on a machine at 1 MHz
2. 5.10^4 n instructions on a machine at 1MHz
3. 10^2 n^2 instructions on a machine at 100MHz
'''

t1 = LineChart("Task 1", "n", "Time in Seconds")
size = 10 ** 5

x1 = [x for x in range(0, (size), (size) // 20)]
y1 = list(map(lambda x: (10 ** 4 * x) / 1_000_000, x1))
t1.plot("10^4 n at 1 MHz", x1, y1, size)

x2 = [x for x in range(0, (size), (size) // 20)]
y2 = list(map(lambda x: (5.10 ** 4 * x) / 1_000_000, x2))
t1.plot("5.10^4 n at 1MHz", x2, y2, size)


x3 = [x for x in range(0, (size), (size) // 20)]
y3 = list(map(lambda x: ((10 ** 2) * (x ** 2) / 1_000_000), x3))
t1.plot("10^2 n^2 at 100MHz", x3, y3, size, 2)

t1.display()


'''
Task 2:

Using Bridges LineChart object, plot the runtime of an algorithm for problem size ranging 
from 1 to 10^4. (Don't use all values of n, take some values in the middle.)

1. 10^4 n instructions on a machine at 1 MHz
2. 10^2 n^2 instructions on a machine at 100MHz
3. n^4 instructions on a machine at 10GHz
'''

t2 = LineChart("Task 2", "n", "Time in Seconds")
size = 10 ** 4

x1 = [x for x in range(0, (size), (size) // 20)]
y1 = list(map(lambda x: (10 ** 4 * x) / 1_000_000, x1))
t2.plot("10^4 n at 1 MHz",x1, y1, size)

x2 = [x for x in range(0, (size), (size) // 20)]
y2 = list(map(lambda x: (10 ** 2) * (x ** 2) / 100_000_000, x2))
t2.plot("10^2 n^2 at 100MHz",x2, y2, size, 2)


x3 = [x for x in range(0, (size), (size) // 20)]
y3 = list(map(lambda x: (x ** 4 / 100_000_000), x3))
t2.plot("n^4 at 10GHz",x3, y3, size, 4)

t2.display()


'''
Task 3:

Using Bridges LineChart object, plot the runtime of an algorithm for problem size ranging 
from 1 to 10^2. (Don't use all values of n, take some values in the middle.)

1. 10^4 n instructions on a machine at 1 MHz
2. 10^2 n^2 instructions on a machine at 100MHz
3. n^4 instructions on a machine at 10GHz
4. 2^n instruction on a machine at 1PHz
'''

t3 = LineChart("Task 3", "n", "Time in Seconds")
size = 10 ** 2

x1 = [x for x in range(0, (size), (size) // 50)]
y1 = list(map(lambda x: (10 ** 4 * x) / 1_000_000, x1))
t3.plot("10^4 n at 1 MHz", x1, y1, size)

x2 = [x for x in range(0, (size), (size) // 50)]
y2 = list(map(lambda x: (10 ** 2) * (x ** 2) / 100_000_000, x2))
t3.plot("10^2 n^2 at 100MHz", x2, y2, size, 2)


x3 = [x for x in range(0, (size), (size) // 50)]
y3 = list(map(lambda x: (x ** 4 / 100_000_000), x3))
t3.plot("n^4 at 10GHz", x3, y3, size, 4)

x4 = [x for x in range(0, (size), (size) // 50)]
y4 = list(map(lambda x: (2 ** x) / (10 ** 18), x4))
t3.plot("2^n at 1PHz", x4, y4, size, "exp")

t3.display()