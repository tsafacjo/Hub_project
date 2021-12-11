import sys
import argparse
from lexer import Lexer
from parser import Parser


if __name__ == '__main__':

    # adding test file name as command line argument


    argParser = argparse.ArgumentParser()
    argParser.add_argument('testFileName')
    args = argParser.parse_args()

    testFileName = args.testFileName

    try:
        with open(testFileName, 'r') as testFile:
            testFileData = testFile.readlines()
    except FileNotFoundError:
        print('Error: test file {} does not exist'.format(testFileName))
        sys.exit()

    lexer = Lexer()
    tokens = lexer.lex(testFileData)

    verbose = True
    parser = Parser(verbose)
    parser.parse(tokens)

