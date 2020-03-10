"""Demo of keyword arguments. """

def describe(name='Unknown name', species='unknown creature', age='unknown'):
    """This function will be used before the main function to describe a person
    or animal
    """
    print(str(name) + " is a " + str(species) + ", age: " + str(age) + ".")



def main():
    """Test the describe function """
    describe(name='Angus', species='chipmunk')
    print(30 * '=')
    describe(species='human', name='Marina')
    print(30 * '=')
    describe(age='17')
    print(30 * '=')
    describe('Peter', 'penguin', 10)

main()