from die import Die
import pygal

#c创建一个骰子的实例
die = Die()
#掷骰子的数目，并将结果保存在列表里
results = []
for roll_num in range(100000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_side):
    frequency = results.count(value)
    frequencies.append(frequency)
#对结果进行可视化
hist = pygal.Bar
print(frequencies)