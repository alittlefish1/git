import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth = 5)
#加标题设置字体
plt.title("square nember",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("suqare of value",fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 10)
plt.show()
