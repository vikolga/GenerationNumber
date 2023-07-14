import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

opts = {'include_files': ['logo.gif'], 'includes': ['re']}

setup(name='Lotto',
      version='2.0',
      description='OlgaVik',
      options={'build_exe': opts},
      executables=[Executable('lotto_2.py', base=base)])
