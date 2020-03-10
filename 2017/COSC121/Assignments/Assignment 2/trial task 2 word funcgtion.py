def dog_latinify_sentence(sentence):
    """This function will convert a whole sentence from english to doglatin
    """
    sentence = input("Enter English Sentence: ")
    listed_string = sentence.split()
    result = []
    for word in listed_string:
        new_words = dog_latinify_word(word)
        result.append(new_words)
    stringed_result = ' '.join(result)
    return (stringed_result)


