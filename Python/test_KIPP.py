import os
try:
    KIPP_DIR = os.environ['KIPP_DIR']
except KeyError:
    os.environ['KIPP_DIR']=os.environ['PWD']
    KIPP_DIR=os.environ['PWD']
from ESSENTIAL_PACKAGES import *
def test_requirements():
    import Commands
    from Command import commands
