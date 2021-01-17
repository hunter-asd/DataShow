# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DataShow.py'],
             pathex=['C:\\Users\\liuyongag\\Desktop\\EXL50_Py\\DS'],
             binaries=[],
             datas=[],
             hiddenimports=['pyttsx3','pyttsx3.drivers','pyttsx3.drivers.sapi5','pkg_resources.py2_warn','MDSplus._mdsshr', 'MDSplus._version', 'MDSplus.apd', 'MDSplus.compound', 'MDSplus.connection', 'MDSplus.descriptor', 'MDSplus.event', 'MDSplus.magic', 'MDSplus.mdsExceptions', 'MDSplus.mdsarray', 'MDSplus.mdsdata', 'MDSplus.mdsdcl', 'MDSplus.mdsplus_wsgi', 'MDSplus.mdsscalar', 'MDSplus.modpython', 'MDSplus.scope', 'MDSplus.tests', 'MDSplus.tree', 'MDSplus.version', 'MDSplus.widgets', 'MDSplus.wsgi'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DataShow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='screen.ico')
