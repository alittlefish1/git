import matplotlib.pyplot as plt

x_value =list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value,y_value,edgecolor='none',c=y_value,s=40)
#设置图表坐标并给坐标加标签
plt.title("squares number",fontsize = 24)
plt.xlabel("value",fontsize = 12)
plt.ylabel("square of value",fontsize = 12)
#设置刻度
plt.tick_params (axis = 'both',which= 'major',labelsize =12)

#设置坐标轴的取值范围
plt.axis([0,1100,0,1100000])


plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()