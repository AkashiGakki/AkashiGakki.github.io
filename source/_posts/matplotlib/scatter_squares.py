from matplotlib import pyplot


# pyplot.scatter(2, 4, s=30)
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# pyplot.scatter(x_values, y_values, s=7)
# pyplot.scatter(x_values, y_values, c=(0.8, 0.2, 0.2, 0.4), edgecolors='none', s=7)
pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Reds, edgecolors='none', s=7)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', which='major', labelsize=13)

# 设置每个坐标轴的取值范围
pyplot.axis([0, 1100, 0, 1100000])

# pyplot.show()
pyplot.savefig('squares_plot.png', bbox_inches='tight')
