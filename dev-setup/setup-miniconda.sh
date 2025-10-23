#! /bin/bash
echo "Setting miniconda"
# Get config variables
source config
echo "Downloading miniconda from $MINICONDA_LINK"

#wget -O /tmp/miniconda.sh $MINICONDA_LINK
chmod +x /tmp/miniconda.sh
bash /tmp/miniconda.sh -b

## Setup in bashrc
echo "" >> $HOME/.bashrc
echo "if [ \"\$CONDA\" = yes ]; then" >> $HOME/.bashrc
echo "  # >>> conda initialize >>>" >> $HOME/.bashrc
echo "  # !! Contents within this block are managed by 'conda init' !!" >> $HOME/.bashrc
echo "  __conda_setup=\"\$('$HOME/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)\"" >> $HOME/.bashrc
echo "  if [ \$? -eq 0 ]; then" >> $HOME/.bashrc
echo "      eval \"\$__conda_setup\"" >> $HOME/.bashrc
echo "  else" >> $HOME/.bashrc
echo "      if [ -f \"$HOME/miniconda3/etc/profile.d/conda.sh\" ]; then" >> $HOME/.bashrc
echo "          . \"$HOME/miniconda3/etc/profile.d/conda.sh\"" >> $HOME/.bashrc
echo "      else" >> $HOME/.bashrc
echo "          export PATH=\"$HOME/miniconda3/bin:\$PATH\"" >> $HOME/.bashrc
echo "      fi" >> $HOME/.bashrc
echo "  fi" >> $HOME/.bashrc
echo "  unset __conda_setup" >> $HOME/.bashrc
echo "# <<< conda initialize <<<" >> $HOME/.bashrc
echo "fi" >> $HOME/.bashrc

## Create desktop launcher
echo "[Desktop Entry]" >> /tmp/anaconda-shell.desktop
echo "Version=1.0" >> /tmp/anaconda-shell.desktop
echo "Type=Application" >> /tmp/anaconda-shell.desktop
echo "Name=Anaconda Terminal" >> /tmp/anaconda-shell.desktop
echo "Comment=Anaconda Terminal" >> /tmp/anaconda-shell.desktop
echo "Exec=env CONDA=yes  /bin/bash" >> /tmp/anaconda-shell.desktop
echo "Icon=utilities-terminal" >> /tmp/anaconda-shell.desktop
echo "Path=" >> /tmp/anaconda-shell.desktop
echo "Terminal=true" >> /tmp/anaconda-shell.desktop
echo "StartupNotify=false" >> /tmp/anaconda-shell.desktop
echo "Categories=Development;" >> /tmp/anaconda-shell.desktop

cp /tmp/anaconda-shell.desktop $HOME/Desktop/anaconda-shell.desktop
cp /tmp/anaconda-shell.desktop $HOME/.local/share/applications/anaconda-shell.desktop
