# Get all running processes on the local computer.

$processes = Get-Process
# Output the process list to the console.
Write-Host "Process Name" -ForegroundColor Green
foreach ($process in $processes) {
    Write-Host $process.Name
}