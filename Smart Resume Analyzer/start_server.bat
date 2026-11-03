@echo off
title Smart Resume Analyzer - One-Click Launcher
color 0A

:: ============================================================
::  SMART RESUME ANALYZER - ONE-CLICK LAUNCHER
::  MongoDB -> Flask Backend -> Frontend Web -> Default Browser
:: ============================================================

:: Resolve project root directory
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

set "BACKEND_DIR=%ROOT%\backend"
set "FRONTEND_DIR=%ROOT%\frontend"
set "DB_DIR=%ROOT%\database"
set "BACKEND_PORT=5000"
set "FRONTEND_PORT=5500"
set "MONGO_PORT=27017"

:: Create required data and logs directories
if not exist "%ROOT%\mongo_data" mkdir "%ROOT%\mongo_data" >nul 2>&1
if not exist "%ROOT%\mongo_logs" mkdir "%ROOT%\mongo_logs" >nul 2>&1
if not exist "%ROOT%\uploads" mkdir "%ROOT%\uploads" >nul 2>&1

cls
echo.
echo ======================================================================
echo   SMART RESUME ANALYZER - SYSTEM INITIALIZATION
echo ======================================================================
echo   Project Directory : %ROOT%
echo   Backend API URL   : http://127.0.0.1:%BACKEND_PORT%/api
echo   Frontend Web URL  : http://127.0.0.1:%FRONTEND_PORT%
echo   MongoDB Port      : %MONGO_PORT%
echo ======================================================================
echo.

:: ------------------------------------------------------------
:: STEP 1: Check Python
:: ------------------------------------------------------------
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python was not found in PATH.
    echo Please install Python 3.9+ and check "Add Python to PATH".
    goto :die
)
for /f "tokens=*" %%v in ('python --version 2^>^&1') do echo   [OK] %%v
echo.

:: ------------------------------------------------------------
:: STEP 2: Check & Start MongoDB
:: ------------------------------------------------------------
echo [2/5] Checking MongoDB database...
netstat -ano | findstr /R /C:":%MONGO_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] MongoDB is already running on port %MONGO_PORT%.
    goto :seed_db
)

:: Locate mongod.exe
set "MONGOD="
where mongod >nul 2>&1 && set "MONGOD=mongod"
if not defined MONGOD (
    for /d %%d in ("C:\Program Files\MongoDB\Server\*") do (
        if exist "%%d\bin\mongod.exe" set "MONGOD=%%d\bin\mongod.exe"
    )
)
if not defined MONGOD (
    for /d %%d in ("C:\Program Files (x86)\MongoDB\Server\*") do (
        if exist "%%d\bin\mongod.exe" set "MONGOD=%%d\bin\mongod.exe"
    )
)
if not defined MONGOD (
    echo [ERROR] mongod.exe was not found.
    echo Please install MongoDB Community Server from:
    echo https://www.mongodb.com/try/download/community
    goto :die
)

echo   [INFO] Starting MongoDB process on port %MONGO_PORT%...
start "MongoDB Service" /min "%MONGOD%" --dbpath "%ROOT%\mongo_data" --port %MONGO_PORT% --logpath "%ROOT%\mongo_logs\mongod.log" --logappend

:: Wait for MongoDB port
set /a MONGO_WAIT=0
:wait_mongo
timeout /t 1 /nobreak >nul 2>&1
netstat -ano | findstr /R /C:":%MONGO_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] MongoDB is ready on port %MONGO_PORT%.
    goto :seed_db
)
set /a MONGO_WAIT+=1
if %MONGO_WAIT% lss 20 goto :wait_mongo

echo [ERROR] MongoDB failed to start within 20 seconds.
echo Check log file: %ROOT%\mongo_logs\mongod.log
goto :die

:seed_db
echo.

:: ------------------------------------------------------------
:: STEP 3: Seed Database (31 Job Roles + Admin)
:: ------------------------------------------------------------
echo [3/5] Syncing database sample data and 31 job roles...
python "%DB_DIR%\init_database.py"
echo   [OK] Database synchronization complete.
echo.

:: ------------------------------------------------------------
:: STEP 4: Start Flask Backend API
:: ------------------------------------------------------------
echo [4/5] Checking Flask Backend API on port %BACKEND_PORT%...
netstat -ano | findstr /R /C:":%BACKEND_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] Flask Backend is already active on port %BACKEND_PORT%.
    goto :start_frontend
)

:: Write backend runner
set "RUN_BACKEND=%ROOT%\mongo_logs\_start_backend.bat"
echo @echo off > "%RUN_BACKEND%"
echo title Flask Backend API - Port %BACKEND_PORT% >> "%RUN_BACKEND%"
echo cd /d "%ROOT%" >> "%RUN_BACKEND%"
echo set "PYTHONPATH=%ROOT%" >> "%RUN_BACKEND%"
echo python -u backend\app.py >> "%RUN_BACKEND%"
echo pause >> "%RUN_BACKEND%"

echo   [INFO] Starting Flask backend in background...
start "Flask Backend [Smart Resume]" cmd /c "%RUN_BACKEND%"

:: Wait for Flask port
set /a FLASK_WAIT=0
:wait_flask
timeout /t 1 /nobreak >nul 2>&1
netstat -ano | findstr /R /C:":%BACKEND_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] Flask Backend is ready on http://127.0.0.1:%BACKEND_PORT%/api
    goto :start_frontend
)
set /a FLASK_WAIT+=1
if %FLASK_WAIT% lss 30 goto :wait_flask

echo [ERROR] Flask Backend failed to respond on port %BACKEND_PORT% within 30 seconds.
echo Please run: python backend\app.py to inspect any Python error.
goto :die

:start_frontend
echo.

:: ------------------------------------------------------------
:: STEP 5: Start Frontend Server
:: ------------------------------------------------------------
echo [5/5] Checking Frontend Web Server on port %FRONTEND_PORT%...
netstat -ano | findstr /R /C:":%FRONTEND_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] Frontend Web Server is already active on port %FRONTEND_PORT%.
    goto :launch_browser
)

:: Write frontend runner
set "RUN_FRONTEND=%ROOT%\mongo_logs\_start_frontend.bat"
echo @echo off > "%RUN_FRONTEND%"
echo title Frontend Web Server - Port %FRONTEND_PORT% >> "%RUN_FRONTEND%"
echo cd /d "%FRONTEND_DIR%" >> "%RUN_FRONTEND%"
echo python -m http.server %FRONTEND_PORT% --bind 127.0.0.1 >> "%RUN_FRONTEND%"
echo pause >> "%RUN_FRONTEND%"

echo   [INFO] Starting Frontend web server...
start "Frontend Web Server [Smart Resume]" cmd /c "%RUN_FRONTEND%"

:: Wait for Frontend port
set /a FRONT_WAIT=0
:wait_frontend
timeout /t 1 /nobreak >nul 2>&1
netstat -ano | findstr /R /C:":%FRONTEND_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo   [OK] Frontend Web Server is ready on http://127.0.0.1:%FRONTEND_PORT%
    goto :launch_browser
)
set /a FRONT_WAIT+=1
if %FRONT_WAIT% lss 20 goto :wait_frontend

echo [ERROR] Frontend Web Server failed to start on port %FRONTEND_PORT%.
goto :die

:launch_browser
echo.
echo ======================================================================
echo   SMART RESUME ANALYZER IS RUNNING SUCCESSFULLY!
echo ======================================================================
echo.
echo   WEBSITE URL (Click or Copy to your browser):
echo   ------------------------------------------------------------------
echo     FRONTEND WEBSITE : http://127.0.0.1:%FRONTEND_PORT%
echo     BACKEND API      : http://127.0.0.1:%BACKEND_PORT%/api
echo     DATABASE         : mongodb://127.0.0.1:%MONGO_PORT%/smart_resume_analyzer
echo   ------------------------------------------------------------------
echo     ADMIN LOGIN      : admin@smartresume.com  /  Admin@123
echo ======================================================================
echo.
echo Launching your default browser to: http://127.0.0.1:%FRONTEND_PORT% ...
timeout /t 2 /nobreak >nul 2>&1

start "" "http://127.0.0.1:%FRONTEND_PORT%"

echo.
echo [STATUS] All services are online and active.
echo [INFO] This Command Prompt window will remain permanently open.
echo [INFO] When you are finished, you can simply close this window [X].
echo.

:: Keep window open indefinitely
:permanent_loop
timeout /t 3600 /nobreak >nul 2>&1
goto :permanent_loop

:die
echo.
echo ======================================================================
echo   [FATAL] Startup encountered an issue. Review the log above.
echo   This window will stay open for troubleshooting.
echo ======================================================================
echo.
:error_hold
pause >nul
goto :error_hold
