# 创造自己的语言 我们将在英语的基础上创建自己的语言：在单词的最后加上-，然后将单词的第一个字母拿出来放到单词的最后，
# 然后在单词的最后加上y，例如，Python，就变成了ython-Py
Word = 'Python'
New_Word = (Word[0:] + '-')[1:] + Word[:2]
print(New_Word)
