spam = ['apple', 'pear', 'pineapple']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
what = ['asda', 'dasdas', 'daaa', 'akakakak', 'abc', 1132, 'awaart']


def comma(lst):
    sentence = ''
    for item in range(len(lst)-1):
        sentence += str(lst[item]) + ', '
    sentence = sentence[:len(sentence)-2] + ' and ' + str(lst[-1]) + '.'
    print(sentence)


comma(spam)
comma(numbers)
comma(what)
