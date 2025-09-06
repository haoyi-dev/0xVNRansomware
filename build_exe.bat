@echo off
echo ========================================
echo            Haoyi Developer
echo ========================================
echo.

where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo PyInstaller chua duoc cai dat. Dang tien hanh cai dat...
    pip install pyinstaller
) else (
    echo PyInstaller da duoc cai dat.
)

echo.
echo Chon file python de dong goi thanh exe:
echo 1. ransomware.py (Basic)
echo 2. ultimate.py (Ultimate)
set /p choice="Nhap lua chon (1 hoac 2): "

if "%choice%"=="1" (
    set "pyfile=ransomware.py"
    set "exename=0xVN_Prank"
) else if "%choice%"=="2" (
    set "pyfile=ultimate.py"
    set "exename=0xVN_Ultimate"
) else (
    echo Lua chon khong hop le. Mac dinh dong goi ransomware.py
    set "pyfile=ransomware.py"
    set "exename=0xVN_Prank"
)

echo.
echo Dang dong goi %pyfile% thanh file exe...
pyinstaller --onefile --windowed --name "%exename%" %pyfile%

echo.
echo Tao file exe thanh cong!
echo Ban co the tim thay %exename%.exe trong thu muc dist
pause
