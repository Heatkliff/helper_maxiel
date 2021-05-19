queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
words = ['сериалы', 'курс']

queries_list = queries.split()
new_list = []
for query in queries_list:
    for words[0] in query or words[1] in query:
        new_list.append(queries_list)
result = ','.join(new_list)
print(result)
