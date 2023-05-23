import pandas as pd

def add_to_map(word, map):
    if word in map:
        map[word] = map[word] + 1
    else:
        map[word] = 1
    return map


def count_words():
    with open('words.txt') as file:
        lines = file.readlines()
        word_map = {}
        
        for line in lines:
            words = line.split(' ')

            for word in words:
                word_map = add_to_map(word, word_map)
                
        max_key = max(word_map, key=word_map.get)
        print(f'Max repeated word is \'{max_key}\' with {word_map[max_key]} occurences')
    

def count_words_with_pandas():
    list = []
    data = pd.read_csv('words.txt', header=None)
    for line in data:
        for words in data[line].str.split(' '):
            for word in words:
                list.append(word)

    df = pd.DataFrame(list, columns=['word'])
    df2 = df.groupby('word')['word'].count().sort_values(ascending=False)
    print(f'Max repeated word is \'{df2.iloc[:1].index.values[0]}\' with {df2.iloc[:1].values[0]} occurences')

count_words()
count_words_with_pandas()