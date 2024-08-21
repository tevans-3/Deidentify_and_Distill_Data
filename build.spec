# -*- coding: utf-8 -*-
import os 
import gooey

path_to_images = r'C:\\Users\\thoma\\Downloads\\TextSummarizing\\images'

image_overrides = Tree(path_to_images, prefix=path_to_images)

gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
#gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

a = Analysis(['Deidentify_and_Distill_Data.py'],
             pathex=[r'C:\\Users\\thoma\Downloads\\TextSummarizing'],
             hiddenimports=[],
             hookspath=None,
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
          gooey_languages, # Add them in to collected files
          image_overrides,
          name='Deidentify_and_Distill_Data',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))