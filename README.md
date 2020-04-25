# Stock Code
A codebase for displaying and generating code for stock image and video purposes.

## Origin
This project was created for generating code to be used as textures () for screens in a 3D scene. 
It was difficult to find sufficiently good CC0 stock photography of the type of code, styled, as desired.

### Where did the code snippets come from?
To keep things CC0 and free from restrictions, all code snippets were taken from projects with Unlicense licenses.
All names and email addresses have been stripped for privacy and to keep the visuals as ambiguous as possible.

### Where did the generators come from?
The data generation scripts were written by me.

Because this repo relies on code licensed under the most unrescricted license available, it is being released under that same license.

If you would like to add your own scripts, please submit a pull request along with examples for use in the README!

## Requirements
Python 3+

## Usage
The files in this project are designed as scripts and thus intended to be run via a commandline interface.

## Examples

### code reader
single file, read out code at constant default speed

    python code_reader.py --ftr python_code/code_snippet1.py

two files, from different directories, read out at non-constant rate

    python code_reader.py --ftr python_code/code_snippet1.py c_code/code_snippet1.c --rsmax=.3 --rsmin=.0001 

multi-file, all from the same directory, read out at non-constant rate

    python code_reader.py --sd='c_code/' --ftr code_snippet1.c code_snippet2.c --rsmax=.3 --rsmin=.0001

### random hex dump
basic run, all defaults

    python random_hex_dump.py 
    
run with spaces, a smaller data chunk size, and set slower output speed

    python random_hex_dump.py --spaces=True --chars=5 --speed=.1
    
run with randomly sized data chunks

     python random_hex_dump.py --spaces=True --rchars_min=5 rchars_max=30