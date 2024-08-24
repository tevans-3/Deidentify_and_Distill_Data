# -*- coding: utf-8 -*-
import os 
import gooey
import PyInstaller
from PyInstaller.utils.hooks import collect_data_files

path_to_program = r'C:\\Users\\thoma\\Downloads\\TextSummarizing\\Deidentify_and_Distill_Data.py'
path_to_images = r'C:\\Users\\thoma\\Downloads\\TextSummarizing\\images'

image_overrides = Tree(path_to_images, prefix=path_to_images)

gooey_root = os.path.dirname(gooey.__file__)

gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
#gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

a = Analysis([path_to_program],
             pathex=[path_to_program],
             hiddenimports=[],
             hookspath=None,
             datas=collect_data_files("en_core_web_sm"),
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages,
          image_overrides,
          name='Deidentify_and_Distill_Data',
          debug=True,
          strip=None,
          upx=True,
          console=True,
          windowed=True,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))