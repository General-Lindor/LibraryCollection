import webbrowser
import os
import re

def getPath(filename):
    base = "file:///" + os.path.abspath(__file__)
    base = re.split("\\\\", base)
    base.pop(len(base) - 1)
    result = ""
    for partialString in base:
        if partialString != "":
            result += partialString + "/"
    result += filename
    return result

def previewPDF(filename):
    url = getPath(filename)
    webbrowser.open(url, new = 2)

#previewPDF("testPDF.pdf")