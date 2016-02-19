import os, sys

class openAppClass:
    def init(x):
        useProgram = ""
        path = "/usr/share/applications"
        for file in os.listdir(path):
            splitFile = os.path.splitext(file)[0].lower()
            if splitFile in x:
                useProgram = splitFile
                os.system("open -a " + useProgram)
