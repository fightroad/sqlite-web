# -*- mode: python ; coding: utf-8 -*-
# Build: pyinstaller sqlite_web.spec

block_cipher = None

a = Analysis(
    ['packaging_entry.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('sqlite_web/templates', 'sqlite_web/templates'),
        ('sqlite_web/static', 'sqlite_web/static'),
    ],
    hiddenimports=[
        'sqlite_web.executor',
        'playhouse.dataset',
        'playhouse.migrate',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Not required by sqlite-web; fragile on Python 3.15 beta.
        'numpy',
        'PIL',
        'Pillow',
        'psutil',
        'tkinter',
        'matplotlib',
        'scipy',
        'pandas',
        'IPython',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='sqlite-web',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
