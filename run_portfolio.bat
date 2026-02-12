@echo off
echo Starting Financial Chatbot Portfolio...

:: Start Backend
start "Chatbot Backend" cmd /k "python backend/server.py"

:: Start Frontend
cd portfolio-ui
start "Portfolio UI" cmd /k "npm run dev"

echo ===================================================
echo Backend running on http://localhost:5000
echo Frontend running on http://localhost:5173
echo ===================================================
