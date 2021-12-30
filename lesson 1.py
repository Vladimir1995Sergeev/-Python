my_list = [(5+6j),4.4, 8, [7, 9],'Hello', (4, 3, 9.2),'string', None, False,
           frozenset(),range(13), zip(*[(11, 12), (13, 14), ('a', 'b')]), TypeError, {4, 11}]
for i, item in enumerate(my_list, 1):
    print (f"{i}) {item} - {type(item)}")