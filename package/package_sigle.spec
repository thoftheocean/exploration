# -*- mode: python -*-

block_cipher = None


a = Analysis(['package_sigle.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\oceanofcodes\\exploration\\package'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='package_sigle',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Administrator\\Desktop\\undercover.ico')
