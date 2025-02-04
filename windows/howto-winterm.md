---
dates: 2022-07-28
---
## Install
Install from the Microsoft Store
> __TODO__ Update?

## Customize

Settings can be edited directly from WT; it is also possible to open ```settings.json```. For this, the system must have an editor (e.g. VScode). Working with the file is more flexible but requires knowing what settings are available and what values are afforded.

The ```settings.json``` for WT is located in 
```
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState
```
and edited by the system, e.g. when new wsl intances appear.

> __TODO__  add link to my ```settings.json``` file

### Generic
Tabs, position, shortcuts, ...
```
"alwaysShowTabs": true,
"confirmCloseAllTabs": false,
"copyFormatting": "none",
"copyOnSelect": true,
"defaultProfile": "{2ece5bfe-50ed-5f3a-ab87-5cd4baafed2b}",
"disableAnimations": true,
"initialCols": 109,
"initialRows": 53,
"initialPosition": "817,3",
```

### Themes
Themes can be copied from different sources, good one is
```
https://windowsterminalthemes.dev/
```

### Fonts
I did not go into tweaking the fonts, just saved pointers
```
https://www.thushanfernando.com/posts/2020/windows-terminal-setup/#pixel-perfect-fonts
```

### Profiles
Each profile must have a guid. To generate guid
```
\\ Windows powershell
  [guid]::NewGuid()
  
\\ Linux
  uuidgen
```

To create a profile with elevated capabilities, use `gsudo`
```
\\ install gsudo on Windows
winget install gsudo

\\ add the profile with gsudo in command line
{
    "guid": "{62c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    "name": "PowerShell ⚡",
    "commandline": "gsudo powershell.exe",
    "icon" : "ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png",
    "fontFace":  "Delugia Nerd Font",
    "hidden": false,
}
```

### Startup Panes
I did not go there.

## Links

https://www.thushanfernando.com/posts/2020/windows-terminal-setup

2022-07-28
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState

generate guid
	Windows powershell
		[guid]::NewGuid()
	Linux
		uuidgen
		
https://windowsterminalthemes.dev/

winget install gsudo