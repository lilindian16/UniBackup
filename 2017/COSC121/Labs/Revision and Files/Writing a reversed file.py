def write_reversed_file(input_filename, output_filename):
    """This function will use an input file and reverse the contents and then
    write it to a new output file
    """
    infile = open(input_filename, 'r')
    lines = infile.readlines()
    outfile = open(output_filename, 'w')
    for line in lines[::-1]:
        outfile.write(str(line))