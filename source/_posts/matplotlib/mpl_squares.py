from matplotlib import pyplot


squates = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
pyplot.plot(input_values, squates, linewidth=3)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', labelsize=13)

pyplot.show()
