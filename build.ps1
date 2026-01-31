# MetaStrip PyInstaller Build Script (PowerShell)
# Creates a standalone executable with windowed mode, icon, and onedir distribution

Write-Host "Building MetaStrip..." -ForegroundColor Green
Write-Host ""

& .\.venv\Scripts\pyinstaller.exe `
    --onedir `
    --windowed `
    --icon=logo.ico `
    --name=MetaStripExe `
    --add-data "open_metastrip:open_metastrip" `
    main.py

Write-Host ""
Write-Host "Build complete! The executable is located in the 'dist\MetaStripExe' folder." -ForegroundColor Green
Write-Host "Run it with: .\dist\MetaStripExe\MetaStripExe.exe" -ForegroundColor Cyan