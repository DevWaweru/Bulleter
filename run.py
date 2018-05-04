#!/usr/bin/env python3.6
import bulleter
my_file = "test.txt"

def read_file(this_file):
    bulleter.read_file(this_file)

def processor():
    bulleter.process_document()

def output():
    bulleter.give_output()

def main():
    print(read_file(my_file))
    print(processor())
    print(output())

if __name__ == '__main__':
    main()