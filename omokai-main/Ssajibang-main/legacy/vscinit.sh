#!/bin/bash


# 사용 방법
#
# 1. vscinit.sh 파일을 최상위 폴더(guest-어쩌구저쩌구)에 놓는다.
# 2. Ctrl+` 를 눌러 터미널을 열고, 터미널에 bash vscinit.sh 을 친다.
# 3. 새로운 창이 뜨면 기존 VSCode 창은 닫는다.

echo -e "{
    \"editor.fontFamily\": \"'Monospace 10', 'Droid Sans Mono', monospace, 'Droid Sans Fallback'\",
    \"editor.fontSize\": 14,
    \"editor.fontLigatures\": true,
    \"terminal.integrated.fontSize\": 14,
    \"terminal.integrated.fontFamily\": \"'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'\",
    \"terminal.integrated.cursorBlinking\": true,
    \"terminal.integrated.cursorStyle\": \"underline\"
}" > ~/.config/Code/User/settings.json

echo -e "[
    {
        \"key\": \"ctrl+enter\",
        \"command\": \"python.execInTerminal\"
    }
]" > ~/.config/Code/User/keybindings.json


#code --install-extension ms-dotnettools.csharp
#code --install-extension ms-python.python
code --install-extension ms-vscode.cpptools
code --install-extension ms-ceintl.vscode-language-pack-ko
code
exit 0
