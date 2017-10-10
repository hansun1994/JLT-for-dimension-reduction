import random
import math
import numpy
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams

def generate_date():
    data_set = numpy.zeros([20, 100])
    for i in range(20):
        data_set[i, 0] = math.cos(random.uniform(0, 2)*math.pi)
        data_set[i, 1] = 1

    return data_set

def randomSubspace(subspaceDimension, ambientDimension):
    return numpy.random.normal(0,1,size=(subspaceDimension, ambientDimension))

def theoreticalBound(n, epsilon):
    bound = math.ceil(4 * math.log(n) / (epsilon**2 / 2 - epsilon**3 /3))
    return bound

def jlt(data_set, subspaceDimension):
    ambientDimension = len(data_set[0])
    a = randomSubspace(subspaceDimension, ambientDimension)
    reduct_data = (1 / math.sqrt(subspaceDimension)) * a.dot(data_set.T).T
    return reduct_data

def generate_test(data_set, reduct_data, subspaceDimension):
    c = range(20)
    l = random.sample(c, 10)
    l.sort()
    ind = []
    ind_reduct = []
    for i in l:
        ind.append(data_set[i])
        ind_reduct.append(reduct_data[i])
    test_data = numpy.array(ind)
    test_reduct = numpy.array(ind_reduct)

    return [test_data, test_reduct, l]

def get_error(v, v_d, result):
    test_data = result[0]
    test_reduct = result[1]
    l = result[2]
    x = []
    y = []
    e = []
    for i in range(10):
        a1 = v.dot(test_data[i].T)
        a2 = v_d.dot(test_reduct[i].T)
        x.append(a1)
        y.append(a2)
        e.append(abs(a1 - a2) / abs(a1))
    error = float(sum(e) / len(e))

    return error

#print([((1/x),theoreticalBound(n=100, epsilon=1/x)) for x in [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]])
#print([((1/x),theoreticalBound(n=100, epsilon=1/x)) for x in [1.05,1.04,1.03,1.02,1.01,1,0.95,0.9,0.85,0.8]])
def plot_1(d, v, total_error):
    for i in range(5, 96, 5):
        d_d = jlt(d, i)
        v_d = jlt(v, i)

        result = generate_test(d, d_d, i)
        total_error.append(get_error(v, v_d, result))

    print(total_error)
    N = len(total_error)
    y = range(5, 96, 5)
    width = 3
    total_error.reverse()
    fig1 = plt.figure('no repeat')
    plt.bar(y, total_error, width, color='c')
    plt.xlabel('Reduced Dimension')
    plt.ylabel('Error')
    plt.grid(True)
    fig1.show()

def plot_100(d, v, n=1000):
    total_error = []
    for i in range(5, 96, 5):
        a = 0
        for j in range(n):
            d_d = jlt(d, i)
            v_d = jlt(v, i)

            result = generate_test(d, d_d, i)
            a += get_error(v, v_d, result)

        total_error.append(a/1000)

    print(total_error)
    N = len(total_error)
    y = range(5, 96, 5)
    width = 3
    total_error.reverse()
    fig2 = plt.figure('repeat 1000 times')
    plt.bar(y, total_error, width, color='c')
    plt.xlabel('Reduced Dimension')
    plt.ylabel('Error')
    plt.grid(True)
    fig2 = plt.show()

d = generate_date()
total_error = []
v = numpy.zeros([1,100])
v[0, 0] = 1

plot_1(d, v, total_error)
plot_100(d, v)