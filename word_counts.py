import collections

def word_count(file_path, word):
    file_content = open(file_path, 'r')
    lines_list = file_content.read()
    words_list = lines_list.split()
    trimmed_words_list = list(map(lambda x: x.lower().replace(',','').replace('.','').replace('\'',''), words_list))
    words_count_list = collections.Counter(trimmed_words_list)
    print(type(words_count_list))
    print(words_count_list)
    file_name = file_path.split("/")[-1]
    print(f"word {word} is found {words_count_list[word]} times in the file {file_name}")

if __name__=='__main__':
    file_path = input("Enter the file path to do word count: ")
    word = input("Enter the word to search on the file: ")
    word_count(file_path, word)


# filtered_words_list = list(filter(lambda x: x=='rakuten', trimmed_words_list ))
#
# print(f"Number of words in the file is: {len(trimmed_words_list)}")
#
# count = 0
# for line in lines_list:
#     for words in line.split():
#         if (words.lower().replace('.','')=='rakuten'):
#             count = count + 1
