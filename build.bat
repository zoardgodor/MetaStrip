@echo off
REM MetaStrip PyInstaller Build Script
REM Creates a standalone executable with windowed mode, icon, and onedir distribution

echo Building MetaStrip...
echo.

.venv\Scripts\pyinstaller.exe ^
    --onedir ^
    --windowed ^
    --icon=logo.ico ^
    --name=MetaStripExe ^
    --add-data "open_metastrip:open_metastrip" ^
    main.py

echo.
echo Build complete! The executable is located in the 'dist\MetaStripExe' folder.
pause
