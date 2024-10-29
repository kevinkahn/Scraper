# ref:  https://stackoverflow.com/questions/38225874/mouse-click-automation-with-powershell-or-other-non-external-software
# get position:
#$X = [System.Windows.Forms.Cursor]::Position.X
#$Y = [System.Windows.Forms.Cursor]::Position.Y
#Write-Output "X: $X | Y: $Y"

[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") 
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 

$signature=@'
[DllImport("user32.dll",CharSet=CharSet.Auto,CallingConvention=CallingConvention.StdCall)]
public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
'@

$SendMouseClick = Add-Type -memberDefinition $signature -name "Win32MouseEventNew" -namespace Win32Functions -passThru

Start-Process chrome.exe -WindowStyle Maximized -ArgumentList "https://ix.bdreporting.com/Home","--start-fullscreen","--new-window"
sleep -Seconds 5

# click to net worth
$x = 1192
$y = 160
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);
$x = 1200
$y = 200
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 05
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);
sleep -Milliseconds 500

# right click  to print
$x = 1200
$y = 250
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Milliseconds 500
$SendMouseClick::mouse_event(0x00000008, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000010, 0, 0, 0, 0) # sends a right-click up

# click print
$x = 1271
$y = 409
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Milliseconds 500
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)

# request options
$x = 2125
$y = 299
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)

# set scale
$x = 1981
$y = 574
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)
sleep -Seconds 01
#Write-Host "`b`b`b70" -NoNewline
#$host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates 1981, 574 # Set cursor to top-left corner
[System.Windows.Forms.SendKeys]::SendWait("`b`b`b70")

# select save
$x = 2028
$y = 1194
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)

# do save to file name box
$x = 1739
$y = 1065
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)

# ok the overwrite
$x = 1333
$y = 705
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)

# close the browser
$x = 2539
$y = 18
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
sleep -Seconds 01
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0)
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0)
