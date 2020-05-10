Write-Host "<<<cobian_backup>>>"
Select-String -path "C:\Program Files (x86)\Cobian Backup 11\Logs\*.txt" -pattern "(Backing up the task)|(The Volume Shadow Copy snapshot set has been created successfully)|(The Volume Shadow Copy snapshot set has been successfully deleted)|(\*\* Backup done for the task)" -AllMatches | Foreach {$_.Line}
