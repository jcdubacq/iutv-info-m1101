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

bold=$(tput bold)
normal=$(tput sgr0)

pipinstall() {
    echo -n "[python:$@]"
    $PIPNAME -q install $@
    x=$?
    if [ "$x" = 0 ]; then
        echo "...ok"
    else
        echo "...ko"
        echo "$bold"$PIPNAME install $@ "$normal"
        $PIPNAME install $@
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
        echo "$bold"jupyter "$@" "$normal"
        jupyter "$@"
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
jupyterconfig enable:nbextensions_configurator nbextensions_configurator enable
jupyterconfig enable:widgetsnbextension nbextension enable --py widgetsnbextension
jupyterconfig install:hide_code nbextension install --sys-prefix --py hide_code
jupyterconfig enable:hide_code nbextension enable --sys-prefix --py hide_code
jupyterconfig contrib:install contrib nbextension install  --sys-prefix
jupyterconfig serverextension:hide_code serverextension enable --sys-prefix --py hide_code
jupyterconfig enable:nbextensions_configurator nbextensions_configurator enable
jupyterconfig enable:toc2 nbextension enable toc2/main

# BUGFIX : templates not found for hide_code
mkdir -p ~/.local/share/jupyter
for a in /home/jcdubacq/Documents/enseignement/new-m1101/m1101 /home/TP/TPINFO/M1101/venv_M1101; do
    where="$(pwd)"
    if [ -d "$a" ]; then
        for pat in $(find "$a" -name 'Templates'); do
            cd "$pat"; cp * ~/.local/share/jupyter/
        done
    fi
    cd "$where"
done

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

