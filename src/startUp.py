import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# import module.utils

from NetTool.Server import *
server = Server("127.0.0.1")