# -*- mode: python -*-

block_cipher = None


a = Analysis(['package.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\oceanofcodes\\exploration\\package'],
             binaries=[],
             datas=[('img//maizi.png', 'img')],
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
          name='package',
          debug=False,
          strip=False,
          upx=True,
          console=False )
