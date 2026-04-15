block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('exp/*', 'exp')],  # imágenes y recursos
    hiddenimports=[
        'cv2',
        'numpy',
        'PIL',
        'onnxruntime'
    ],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='remove-background',
    debug=False,
    console=False,  # sin consola (GUI)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='remove-background'
)
