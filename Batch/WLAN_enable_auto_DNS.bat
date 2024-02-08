powershell start cmd -v runas -ArgumentList {/c \"@echo on & powershell \"\\\"0x{0:x}\\\" -f ^(Get-ScheduledTask -TaskName \\\"DHCP auto DNS\\\"^|Enable-ScheduledTask^)\" & powershell \"\\\"0x{0:x}\\\" -f ^(Get-ScheduledTask -TaskName \\\"Google Public DNS autoconnect\\\"^|Enable-ScheduledTask^)\" & @echo off\"}

::ACTUAL COMMANDS
::powershell "\"0x{0:x}\" -f (Get-ScheduledTask -TaskName \"DHCP auto DNS\"|Enable-ScheduledTask)"
::powershell "\"0x{0:x}\" -f (Get-ScheduledTask -TaskName \"Google Public DNS autoconnect\"|Enable-ScheduledTask)"

::ESCAPED
::powershell \"\\\"0x{0:x}\\\" -f ^(Get-ScheduledTask -TaskName \\\"DHCP auto DNS\\\"^|Enable-ScheduledTask^)\"
::powershell \"\\\"0x{0:x}\\\" -f ^(Get-ScheduledTask -TaskName \\\"Google Public DNS autoconnect\\\"^|Enable-ScheduledTask^)\"