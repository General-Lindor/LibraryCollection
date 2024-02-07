@echo off

:loop

:: Get all arguments.
set input=%*

:: Get input path(s) if needed.
if not defined input set /p "input="

:: Exit if no input.
if not defined input exit /b

:: Display each argument (optional code).
::if defined input for %%A in (%input%) do echo input: %%A

:: Call each argument which can be a file or folder.
for %%A in (%input%) do call :step_1 "%%~A"

goto loop


:step_1

powershell start cmd -v runas -ArgumentList {/c \"%1\"}