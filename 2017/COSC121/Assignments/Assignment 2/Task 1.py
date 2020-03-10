def dog_latinify_word(word):
    """This function will take one word and return the dogified version
    """
    lower_case_word = word.lower()
    list_of_letters = list(lower_case_word)
    first_letter = list_of_letters[0]
    list_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                       "p", "q", "r", "s", "t", "v", "w", "x", "y"]
                                   
    if first_letter in list_consonants:
        dog_word = lower_case_word[1: ] + lower_case_word[0] + "oof"
        
    else:
        dog_word = lower_case_word + "woof"
            
    return dog_word  



def dog_latinify_sentence(sentence):
    """This function will convert a whole sentence from english to doglatin
    """
    listed_string = sentence.split()
    result = []
    for word in listed_string:
        new_words = dog_latinify_word(word)
        result.append(new_words)
    stringed_result = ' '.join(result)
    return stringed_result