@echo off
color 0a
MODE CON COLS=80 LINES=36
title ！！！！！！！！！！！！！！！！！注意！！！！！！！！！！！！！！！！！
echo.
echo.
echo.
echo                 ┏─────────────────────┓
echo                 │!!!!!!!!!!!!!!!!!!!注意!!!!!!!!!!!!!!!!!!!│
echo                 │─────────────────────│
echo                 │如果原本是2.0.0或2.5.0固件，只需选择2即可 │
echo                 │如果原本是8XX固件，需要选择1烧写全部      │
echo                 │一般从8XX固件烧写，需要强刷。按住按钮不放 │
echo                 │重新连接USB，直至烧写完毕再松手即可！     │
echo                 │                                          │
echo                 │   1、烧写Bootrom  + fullimage            │
echo                 │                                          │
echo                 │   2、只烧写fullimage.elf                 │
echo                 │                                          │
echo                 │                    By:tssmcu 2016-11-08  │
echo                 ┗─────────────────────┛
echo
echo.
echo.
set num=
set /p num= 请输入【设备管理器—端口—Proxmark3】的串口号(例如"5"):

echo.
echo.

set ok=
set /p ok= 请查看【警告】，并选择一个数字(1,2):
if "%ok%"=="1" goto :all
if "%ok%"=="2" goto :next

:all
cls
title 正在烧写Proxmark3固件至[2.0.0],请等候片刻……
echo.
echo                 ┏────────────────────┓
echo                 │你选择了刷新所有固件，包含Bootrom！     │
echo                 │正在刷新 bootrom.elf,请等候片刻……     │
echo                 ┗────────────────────┛
echo.
flasher.exe com%num% -b ..\firmware_win\bootrom.elf
ping 127.0.0.1 -n 8 >nul
taskkill /f /im flasher.exe


:next
cls
echo.
echo                 ┏────────────────────┓
echo                 │正在刷新 fullimage.elf,请等候片刻……   │
echo                 ┗────────────────────┛
echo.
flasher.exe com%num% ..\firmware_win\fullimage.elf
ping 127.0.0.1 -n 3 >nul
taskkill /f /im flasher.exe
cls
title 恭喜Proxmark3-2.0.0固件成功升级！
echo.
echo.
echo                ┏──────────────────────┓
echo                │     恭喜，固件全部更新完成！Enjoy it !     │
echo                │                                            │
echo                │日行一善，善如春园之草，不见其长，日有所增; │
echo                │                                            │
echo                │日行一恶，恶如磨刀之石，不见其亏，日有所减! │
echo                │                                            │
echo                │    Proxmark3-2.0.0固件成功升级！  BinAry   │
echo                ┗──────────────────────┛
echo.
pause.
cls
MODE CON COLS=130 LINES=36
cmd.exe
