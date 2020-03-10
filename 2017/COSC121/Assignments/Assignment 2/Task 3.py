"""This program will convert any given sentence input by the user into Dog Latin  
"""

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
    return (stringed_result)

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

        


def main():
    """This main function will keep asking for the user to enter in a sentence
    and will return the Dog Latin equivalent sentence
    """
    is_quitting = False
    prompt = ("Enter English sentence: ")
    while not is_quitting:
        command = input(prompt)
    
        if command == 'q':
            is_quitting = True
            
            
        else:
            answer = dog_latinify_sentence(command)
            print(("Dog Latin ="), (answer))
    print("oodbyegoof")
    
#Runs the program
main()
                
        