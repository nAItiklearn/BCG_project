Write-Host "Starting Financial Chatbot Portfolio..." -ForegroundColor Cyan

# Start Backend
Start-Process cmd -ArgumentList "/k python backend/server.py" -WorkingDirectory $PSScriptRoot -WindowStyle Normal
Write-Host "Started Backend Server" -ForegroundColor Green

# Start Frontend
Start-Process cmd -ArgumentList "/k cd portfolio-ui && npm run dev" -WorkingDirectory $PSScriptRoot -WindowStyle Normal
Write-Host "Started Frontend Server" -ForegroundColor Green

Write-Host "`nBackend running on http://localhost:5000"
Write-Host "Frontend running on http://localhost:5173"
Write-Host "Opening browser..."

Start-Sleep -Seconds 3
Start-Process "http://localhost:5173"
