# MetaStrip PyInstaller Build Script (PowerShell)
# Creates a standalone executable with windowed mode, icon, and onedir distribution

Write-Host "Building MetaStrip..." -ForegroundColor Green
Write-Host ""

& .\.venv\Scripts\pyinstaller.exe `
    --onedir `
    --windowed `
    --icon=icon.ico `
    --name=MetaStrip `
    --add-data "open_metastrip:open_metastrip" `
    main.py

Write-Host ""
Write-Host "Build complete! The executable is located in the 'dist\MetaStrip' folder." -ForegroundColor Green
Write-Host "Run it with: .\dist\MetaStrip\MetaStrip.exe" -ForegroundColor Cyan
