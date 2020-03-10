import re


def print_common_words(filename_1, filename_2):
    """THIS WILL PRINT THE WORDS THAT OCCUR BOTH IN FILE ONE AND IN FILE TWO
    """
    try: 
        word_set_from_file(filename_1)
        word_set_from_file(filename_2)
    except FileNotFoundError:
        print('A file could not be found.')
    else:
        results = []
        set_one = word_set_from_file(filename_1)
        set_two = word_set_from_file(filename_2)
        similar_words = set_one & set_two
        for word in similar_words:
            results += [word]
        results.sort()
        for word in results:
            print(word)
            
        
def word_set_from_file(filename):
    """THIS WILL OBTAIN A SET OF WORDS THAT OCCUR IN THE FILE
    """
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    return(set(words))        
    
        
set1 = {0, 2, 4}
set2 = {1, 3, 5}

inter = set1.intersection(set2)
print(inter)