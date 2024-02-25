import builtins
import lab8q2
from io import StringIO
from sys import stderr 
import sys
import os.path

import importlib

oriOpen = builtins.open
def openfile(a, b):
    if b.upper() == "W":
        return oriOpen("testSubject.txt", "w")
    elif b.upper() == "R":
        return oriOpen("testSubject.txt", "r")
    elif b.upper() == "A":
        return oriOpen("testSubject.txt", "a")
    else:
        return oriOpen("testSubject.txt", "r")   

def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("builtins.open", openfile)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab8q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert os.path.exists("testSubject.txt")
    if os.path.exists("testSubject.txt"):
        with oriOpen(f"testSubject.txt") as tf:
            s = tf.read()
            assert(s.find("12 x  4 =  48") != -1 )
            assert(s.find("1  x  4 =   4") != -1 )
    assert captured_stdout.strip().find(f'12 x  4 =  48') != -1
    assert captured_stdout.strip().find(f'1  x  4 =   4') != -1

