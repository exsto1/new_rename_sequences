#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", help='Input folder', required=True)
args = parser.parse_args()


def seq_rename(folder, file):
    text = open('/'.join([folder, file])).readlines()
    if '.' in file:
        output_filename = file.split('.')[0]
    else:
        output_filename = file
    output = open('/'.join([folder, output_filename]) + "_renamed", 'w')
    for i in text:
        if '>' in i:
            output.write('>' + output_filename + "_" + i.lstrip('>'))
        else:
            output.write(i)


def processing(folder):
    try:
        file_list = os.listdir(folder)
    except FileNotFoundError:
        print("Fatal Error: Folder doesn't exist. STOP.")
        exit()

    file_list = [i for i in file_list if "_renamed" not in i]
    for file in file_list:
        seq_rename(folder, file)


processing(args.i)
