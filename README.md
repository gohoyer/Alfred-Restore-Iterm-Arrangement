# Alfred-Restore-Iterm-Arrangement
This alfred workflow will list avaliable [iTerm2](https://iterm2.com/index.html) arrangements and let you select one to restore.

## Requirements

[iterm2](https://iterm2.com/downloads/stable/iTerm2-3_4_15.zip): Build 3.4.15 (not tested on other versions but myght work)

And the following python libraries:
```
pip3 install iterm2
pip3 install pyobjc
```
> This workfllow will use the python from iterm2 on ~/Library/ApplicationSupport/iTerm2/Scripts/get_window_arrangements/iterm2env/versions/3.8.6/bin/python3

## Usage
Just type `iTermA` on alfred and it will:
 - Launch iterm2 if its closed
 - List the avaliable window arrangements
 - Restore the selected window arrangement

![RestoreItermArrangement.gif](images/RestoreItermArrangement.gif)

## Download
Check the [releases page](https://github.com/gohoyer/Alfred-Restore-Iterm-Arrangement/releases) to download it.