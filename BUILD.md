# PyInstaller Build Guide for MetaStrip

## Prerequisites

Make sure you have installed all dependencies:

```bash
pip install -r requirements.txt
```

## Building the Executable

### Option 1: Using Batch Script (Windows CMD)

Simply run the batch file:

```bash
build.bat
```

### Option 2: Using PowerShell Script

Run the PowerShell script:

```powershell
.\build.ps1
```

### Option 3: Manual Command (Windows PowerShell/CMD)

Run this command directly:

```powershell
pyinstaller --onedir --windowed --icon=logo.ico --name=MetaStripExe --add-data "open_metastrip:open_metastrip" main.py
```

## Build Options Explained

- `--onedir`: Creates a folder with the executable and all dependencies inside
- `--windowed` (or `-w`): Runs without a console window (GUI only)
- `--icon=logo.ico`: Adds the logo.ico file as the application icon
- `--name=MetaStripExe`: Names the executable and output folder "MetaStripExe"
- `--add-data "open_metastrip:open_metastrip"`: Includes the open_metastrip module

## Output

After building, the executable will be located in:

```
dist/MetaStripExe/MetaStripExe.exe
```

You can run it directly:

```powershell
.\dist\MetaStripExe\MetaStripExe.exe
```

## Distribution

To distribute MetaStrip:

1. Copy the entire `dist/MetaStripExe` folder
2. Users can run `MetaStripExe.exe` without needing Python installed
3. No external dependencies required

## Clean Build

To create a clean build (remove old builds first):

```powershell
Remove-Item -Recurse -Force dist
Remove-Item -Recurse -Force build
Remove-Item MetaStrip.spec
```

Then run the build command again.

## Troubleshooting

**Error: `logo.ico` not found**
- Ensure `logo.ico` is in the project root directory

**Error: Module not found**
- Make sure all imports in the code are correct
- Check that `open_metastrip` folder contains `__init__.py`

**Large executable size**
- This is normal for PySide6. The executable includes the entire Qt framework.
- You can reduce it using `--onefile` instead of `--onedir`, but startup will be slower.
