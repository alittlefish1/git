import matplotlib.pyplot as plt

from random_walk import RandomWalk

biaozhi = True
#只要处于活跃就不断地模拟随机漫步
while biaozhi:
    #创建randomwalk的实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    #设置窗口尺寸
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Blues,
                edgecolor='none',s = 1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=10)
    plt.savefig('randomwalk.png',bbox_inches = 'tight')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    while True:
        if keep_running == 'n':
            biaozhi = False
            break
        elif keep_running == 'y':
            break
        else:
            keep_running = input("invalid please input y or n : ")
