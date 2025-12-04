# PowerShell script to start local HTTP server
Write-Host "Starting local server..." -ForegroundColor Green
Write-Host ""
Write-Host "Open your browser and go to: http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Try Python first, then Node.js, then PHP
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Using Python HTTP server..." -ForegroundColor Green
    python -m http.server 8000
}
elseif (Get-Command node -ErrorAction SilentlyContinue) {
    Write-Host "Using Node.js http-server..." -ForegroundColor Green
    if (-not (Get-Command http-server -ErrorAction SilentlyContinue)) {
        Write-Host "Installing http-server globally..." -ForegroundColor Yellow
        npm install -g http-server
    }
    http-server -p 8000
}
elseif (Get-Command php -ErrorAction SilentlyContinue) {
    Write-Host "Using PHP built-in server..." -ForegroundColor Green
    php -S localhost:8000
}
else {
    Write-Host "Error: No suitable server found!" -ForegroundColor Red
    Write-Host "Please install Python, Node.js, or PHP" -ForegroundColor Red
    pause
}


