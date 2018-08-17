# Nouvelle version du cours M1101

Pour installer:

Disposer d'une version de python et de pip3

    pip3 install jupyter --user
    pip3 install tutormagic --user
    pip3 install nbtutor --user
    pip3 install matplotlib --user
    pip3 install git+git://github.com/mkrphys/ipython-tikzmagic.git --user
    jupyter nbextension enable --py widgetsnbextension --user
    jupyter nbextension install --py hide_code --user
    jupyter nbextension enable --py hide_code --user
    jupyter serverextension enable --py hide_code --user

S'assurer que `~/.local/bin` est dans le chemin d'exécution :

    cat >> ~/.profile << EOF
    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi
    EOF

Actuellement, les lignes suivantes ne sont plus utiles :

    jupyter nbextension install --overwrite --symlink --user --py nbtutor
    jupyter nbextension enable nbtutor --user --py
