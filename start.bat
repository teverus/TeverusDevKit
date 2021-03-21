@echo off
rem color 0A - this will make console black and green
rem mode con: cols=68 lines=17 - this will set fixed size for the console
title=Type_your_title_here

rem This will work only if TeverusDevKit and venv are on the same level
rem Delete timeout -1 if you want the window to close right after your application quits

cmd /k "cd .. & cd venv\Scripts & activate & cd ..\.. & python main.py & timeout -1 & exit"