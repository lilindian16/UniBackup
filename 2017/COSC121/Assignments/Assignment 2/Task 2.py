def englishify_dog_word(word):
    """This will translate from doglatin back into English
    """
    
    
    if word[-4:-1] == ('woo'):
        translated_word = "(" + word[-4] + word[0:-4] + " or " + word[0:-4] + ")"
        return translated_word
    else:
        translated_word = word[-4] + word[ :-4]
        return translated_word
    

    
    
def englishify_dog_sentence(sentence):
    """This function will use the for loop for work out the english sentence
    for the doglatin
    """
    listed_string = sentence.split()
    result = []
    for word in listed_string:
        new_words = englishify_dog_word(word)
        result.append(new_words)
    stringed_result = ' '.join(result)
    return stringed_result

        
