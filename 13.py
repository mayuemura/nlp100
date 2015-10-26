import fileinput
import sys

fo = open("output.txt","w")

for l in fileinput.input(["col1.txt","col2.txt"]):


