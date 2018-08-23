# Nouvelle version du cours M1101

## Pour installer

Disposer d'une version de python et de pip3

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

S'assurer que `~/.local/bin` est dans le chemin d'exécution :

    cat >> ~/.profile << EOF
    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi
    EOF

Pour installer pip et python3 sur un système Debian/Ubuntu

    sudo apt-get install python3-pip
    
Pour installer les autres programmes utiles:

    sudo apt-get install texlive-full graphviz


## Pour démarrer

    cd .../iutv-info-M1101
    jupyter-notebook # ouvre un navigateur

Lorsque vous êtes dans un notebook (M1101-XXX) il faut aller dans `View > Cell toolbar > Hide code` pour faire apparaître sur chaque cellule le contrôle de la visibilité du code (souvent caché).

Certaines cellules qui contiennent des exercices (*activités*) peuvent être relancées pour obtenir un exercice différent.
Certaines cellules qui suivent une activité sont là pour vérifier si l'exercice précédent est correct ou non.

## Pour mémoire

Actuellement, les lignes suivantes ne sont plus utiles :

    jupyter nbextension install --overwrite --symlink --user --py nbtutor
    jupyter nbextension enable nbtutor --user --py

## Pour nettoyer

Sous Linux :

    rm -rf ~/.local/bin ~/.local/share/jupyter ~/.jupyter/ ~/.local/lib  ~/.cache/pip/