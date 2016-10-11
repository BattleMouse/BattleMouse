echo on

SET InputPath=%1
SET UE4Version=4.12
SET Output="C:\Program Files\Epic Games\%UE4Version%\Engine\Plugins"

if "%SDKPath%" == "" SET SDKPath="none"

echo %Output%
call python %~dp0script/UE4PluginInstall.py %InputPath% %Output%

pause
