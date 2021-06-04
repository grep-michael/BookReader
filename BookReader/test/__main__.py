import sys,unittest
import os
path = "\\".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-2])
sys.path.append(path)

from BookReader.test.ReadFromPDF import *
TestClass()
unittest.main()