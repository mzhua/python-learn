tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table():
    max_width = [0] * len(tableData)
    for i in range(len(tableData)):
        for name in tableData[i]:
            if len(name) > max_width[i]:
                max_width[i] = len(name)

    result = [[row[i] for row in tableData] for i in range(len(tableData[0]))]
    for i in range(len(result)):
        for name in result[i]:
            print(name.rjust(max_width[result[i].index(name)]), end=' ')
        print(end='\n')


print_table()
