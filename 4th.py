'''Use lambda functions to define custom sorting criteria.
 Use the Build in Sort Method to do this Example:'''
data = [(89, 'Bob'), (95, 'Alice'), (92, 'Charlie')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
