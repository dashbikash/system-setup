#! /bin/bash
echo "Setting vscode"
# Get config variables
source config
echo "Downloading vs code from $VSCODE_LINK"
wget -O /tmp/vscode.tar.gz $VSCODE_LINK
tar -xvfz /tmp/vscode.tar.gz --directory $TARGET_DIR



# [Desktop Entry]
# Name=Visual Studio Code
# Comment=Code Editing. Redefined.
# GenericName=Text Editor
# Exec=/usr/share/code/code --unity-launch %F
# Icon=com.visualstudio.code
# Type=Application
# StartupNotify=false
# StartupWMClass=Code
# Categories=TextEditor;Development;IDE;
# MimeType=text/plain;inode/directory;application/x-code-workspace;
# Actions=new-empty-window;
# Keywords=vscode;

# [Desktop Action new-empty-window]
# Name=New Empty Window
# Exec=/usr/share/code/code --new-window %F
# Icon=com.visualstudio.code