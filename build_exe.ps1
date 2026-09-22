# Build a single-file Windows executable for sqlite-web.
# Usage: powershell -ExecutionPolicy Bypass -File .\build_exe.ps1

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

python -m pip install -U pip
python -m pip install -e .
python -m pip install pyinstaller

if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }

python -m PyInstaller --noconfirm --clean sqlite_web.spec

Write-Host ""
Write-Host "Built: $(Join-Path $PSScriptRoot 'dist\sqlite-web.exe')"
