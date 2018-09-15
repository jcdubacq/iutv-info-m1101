#! /bin/sh

# Pour IUTV: /iutv/Mes_Montages/TP/TPINFO/M1101/install.sh

PIPNAME=pip3
pip3 --version > /dev/null 2>/dev/null
if [ "$?" != "0" ]; then
	PIPNAME=pip
fi

maybeinstall() {    
    if which "$1" > /dev/null ; then
        echo "[$2]...ok"
    else
        echo "Il faudrait installer $2"
        echo "sudo apt-get install $2"
    fi
}
checkinstall() {    
    if which "$1" > /dev/null ; then
        echo "[$2]...ok"
    else
        echo "Il faut installer $2"
        echo "sudo apt-get install $2"
        exit
    fi
}

pipinstall() {
    echo -n "[python:$@]"
    $PIPNAME -q install $@ --user
    x=$?
    if [ "$x" = 0 ]; then
        echo "...ok"
    else
        echo "...ko"
        exit
    fi
}

jupyterconfig() {
    x=$1
    shift
    echo -n "[configuration:$x]"
    jupyter "$@" > /dev/null 2>/dev/null
    x=$?
    if [ "$x" = 0 ]; then
        echo "...ok"
    else
        echo "...ko"
        exit
    fi
}

checkinstall $PIPNAME python3-pip
checkinstall dot graphviz
maybeinstall pdflatex texlive
maybeinstall wkhtmltopdf wkhtmltopdf

PATH="$HOME/.local/bin:$PATH"

pipinstall jupyter

if which jupyter > /dev/null ; then echo "ok, jupyter accessible."; else echo "Mais où est jupyter ?"; exit; fi

pipinstall tutormagic
pipinstall jupyter_nbextensions_configurator
pipinstall nbtutor
pipinstall matplotlib
pipinstall graphviz
pipinstall hide_code
pipinstall git+git://github.com/mkrphys/ipython-tikzmagic.git
pipinstall jupyter_contrib_nbextensions

echo "[configuration]"
jupyterconfig enable:nbextensions_configurator nbextensions_configurator enable --user
jupyterconfig enable:widgetsnbextension nbextension enable --py widgetsnbextension --user
jupyterconfig install:hide_code nbextension install --py hide_code --user
jupyterconfig enable:hide_code nbextension enable --py hide_code --user
jupyterconfig contrib:install contrib nbextension install --user
jupyterconfig serverextension:hide_code serverextension enable --py hide_code --user
jupyterconfig enable:nbextensions_configurator nbextensions_configurator enable
jupyterconfig enable:toc2 nbextension enable toc2/main

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

if [ "$FOUND" = 0 ]; then
    cat >> ~/.profile << EOF
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
EOF
fi


echo "Avant de lancer jupyter, ouvrez un nouveau shell ou tapez :"
echo 'PATH="$HOME/.local/bin:$PATH"'

if [ -f Plan.ipynb ]; then
    exec jupyter notebook
fi
# nettoyage
# rm -rf ~/.local/bin ~/.local/share/jupyter ~/.jupyter/ ~/.local/lib  ~/.cache/pip/

