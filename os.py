#!/usr/bin/env python

import os

print('Get current working directory')
print(os.getcwd)
print()

if os.path.exists('test/test.txt'):
    print('Remove file')
    os.remove('test.txt')
    print()

if os.path.exists('test'):
    print('Remove test dir')
    os.rmdir('test')
    print()

print('List contents of current directory')
print(os.listdir())
print()

print('Create test dir')
os.mkdir("test")
print()

print('List contents of current dir')
print(os.listdir())
print()

print('Change into test dir')
os.chdir('test')
print()

print('Get current working dir')
print(os.getcwd())
print()

print('List contents of test dir')
print(os.listdir())
print()

print('Create a file')
file = open('test.txt', 'w')
print(file)
file.write("This is a test!")
file.close()
file = None
file = open('test.txt', 'r')
print(file.read())
file.close()
print()

if os.path.exists('test.txt'):
    print('Remove file')
    os.remove('test.txt')
    print()

print('Move up on dir')
os.chdir('../')
print()

print('List contests of current dir')
print(os.listdir())
print()

if os.path.exists('test'):
    print('Remove test dir')
    os.rmdir('test')
    print()

print('Loop through dir names and file names of current working dir')
for dirpath, dirname, filenames in os.walk(os.getcwd(), topdown='true'):
    for filename in filenames:
        print(dirpath, filename)
print()
