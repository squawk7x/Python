from matplotlib import pyplot as plt

#print(plt.style.available)
#plt.style.use('bmh')

ages_x = [25, 26, 27, 28, 29, 30]
dev_y = [10000, 25000, 32000, 33000, 40000, 43000]
plt.plot(ages_x, dev_y, 'k--o', label='All Devs')
plt.bar(ages_x, dev_y, label='All Devs')

py_dev_y = [11000, 29000, 34000, 36000, 42000, 45000]
plt.plot(ages_x, py_dev_y, color='#5a7d9a', marker='.', label='Python')
plt.bar(ages_x, py_dev_y, color='#5a7d9a', label='Python')

plt.title('Median Salary (USD)')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()  # according order inserted # according labels

# plt.legend(['All Devs', 'Python']) # according order inserted

#plt.grid()
#plt.tight_layout()
#plt.savefig('plot.png')
plt.show()

