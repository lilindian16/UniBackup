def are_anagrams(word1, word2):
    """This function will check to see if two wordsin a parameter
    are anagrams ie they contain the same letters but are not the same words
    """
    list_word1 = list(word1)
    list_word1.sort()
    list_word2 = list(word2)
    list_word2.sort()
    
    if (word1) == (word2):
        return False
        
    elif list_word1 == list_word2:
        return True
    
    else:
        return False