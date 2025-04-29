from PyInstaller.utils.hooks import collect_submodules, collect_data_files
import os

# Set the path to your virtual environment's site-packages
venv_site_packages = os.path.join(os.getcwd(), '.venv', 'lib', 'python3.10', 'site-packages')

robot_data_files = collect_data_files('robot')

# Collect submodules from the robot library (and other libraries you need)
hiddenimports = collect_submodules('robot')
hiddenimports += collect_submodules('robot.libraries')
hiddenimports += collect_submodules('Camunda')
hiddenimports += collect_submodules('Camunda.Browser')
hiddenimports += collect_submodules('Camunda.Excel')

hiddenimports += [
        "Camunda.Archive",
        "Camunda.Browser.Selenium",
        "Camunda.Calendar",
        "Camunda.Desktop",
        "Camunda.Desktop.OperatingSystem",
        "Camunda.Excel.Application",
        "Camunda.Excel.Files",
        "Camunda.FileSystem",
        "Camunda.FTP",
        "Camunda.HTTP",
        "Camunda.Images",
        "Camunda.JavaAccessBridge",
        "Camunda.JSON",
        "Camunda.MFA",
        "Camunda.MSGraph",
        "Camunda.Outlook.Application",
        "Camunda.PDF",
        "Camunda.SAP",
        "Camunda.Tables",
        "Camunda.Tasks",
        "Camunda.Windows",
        "Camunda.Word.Application",
    ]

# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['src/robot_runner.py'],
    pathex=[],
    binaries=[],
    datas=robot_data_files,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='robot',
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