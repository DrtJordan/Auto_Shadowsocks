@echo off

rem ѡ��ѡ��
echo "1.��һ�η�ǽ"
echo "2.�����ڷ�ǽ(�Ժ�������0,6,12,18,24��������)"
echo "3.ֹͣ�����ڷ�ǽ"
rem ps:��ν�������ڷ�ǽָ���������ƻ�����ʹshadowsocksÿ��Сʱ�Զ��ػ�����

CHOICE /C 123 /M ""

if %errorlevel%==1 goto First
if %errorlevel%==2 goto Second
if %errorlevel%==3 goto Third

:First
rem ֱ�����г���

rem ------------------
rem ע��·��!!!<(���䣭)>
rem ------------------
cd ..
shadowsocks.py

goto Quit

:Second
rem ��0�㿪ʼ��ÿ��Сʱ��һ��qq�������,��ֱ������һ�μƻ�����
cd ..
schtasks /create /sc hourly /mo 6 /tn "Auto" /tr shadowsocks.py /st 00:00:02 /f

rem ------------------
rem ע��·��!!!<(���䣭)>
rem ------------------

schtasks /run /tn "Auto"
goto Quit

:Third
rem ɾ���ƻ����� "Auto"
schtasks /delete /tn "Auto"
goto Quit


:Quit
pause
