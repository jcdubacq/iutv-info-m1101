#! /bin/sh

checkinstall() {    
    if which "$1" > /dev/null ; then
        echo "[$2]...ok"
    else
        echo "Il faut installer $2 pour Python3"
        echo "sudo apt-get install $2"
        exit
    fi
}

checkinstall pip3 python3-pip
checkinstall dot graphviz
checkinstall pdflatex texlive

pip3 install jupyter --user
pip3 install tutormagic --user
pip3 install jupyter_nbextensions_configurator --user
pip3 install nbtutor --user
pip3 install matplotlib --user
pip3 install graphviz --user
pip3 install hide_code --user
pip3 install git+git://github.com/mkrphys/ipython-tikzmagic.git --user
pip3 install jupyter_contrib_nbextensions --user
jupyter nbextensions_configurator enable --user
jupyter nbextension enable --py widgetsnbextension --user
jupyter nbextension install --py hide_code --user
jupyter nbextension enable --py hide_code --user
jupyter nbextension enable --py toc2 --user
jupyter contrib nbextension install --user
jupyter serverextension enable --py hide_code --user
jupyter-nbextensions_configurator enable
jupyter-nbextension enable toc2/main

OLDIFS="$IFS"
IFS=":"
FOUND=0
for p in $PATH ; do
    IFS="$OLDIFS"
    if [ "$p" = "$HOME/.local/bin" ]; then
        FOUND=1
    fi
    IFS=":"
done
IFS="$OLDIFS"
echo "$PATH"|cut -f
if [ "$FOUND" = 0 ]; then
    cat >> ~/.profile << EOF
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
EOF
fi


# nettoyage
# rm -rf ~/.local/bin ~/.local/share/jupyter ~/.jupyter/ ~/.local/lib  ~/.cache/pip/