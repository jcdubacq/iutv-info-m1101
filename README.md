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


## Pour démarrer à l'IUT

Une fois tout installé avec le script de /iutv/Mes_Montages/TP/TPINFO/M1101/install.sh en cas de problème, on peut relancer le tout:

    # Ouvrir un nouveau terminal, puis :
    source activate m1101
    cd ~/Documents/iutv-info-m1101
    jupyter notebook list
    jupyter notebook stop 8888
    # Recommencer avec les autres numéros s'il y en a plusieurs
    jupyter notebook # <== démarre le nouveau jupyter

Quand un notebook est ouvert, commencer tout de suite par l'exécuter en redémarrage avec le bouton ⏩
Lorsque vous êtes dans un notebook (M1101-XXX) il faut aller dans `View > Cell toolbar > Hide code` pour faire apparaître sur chaque cellule le contrôle de la visibilité du code (souvent caché).

Certaines cellules qui contiennent des exercices (*activités*) peuvent être relancées pour obtenir un exercice différent.
Certaines cellules qui suivent une activité sont là pour vérifier si l'exercice précédent est correct ou non.

Après la première exécution par le bouton ⏩, le notebook a été fait en mode "non-interactif". À la fin, le notebook bascule en mode "interactif". Si vous refaites un exercice en le relançant il va proposer d'attendre les solutions et (parfois) dire si elles sont correctes ou pas.

**IMPORTANT :** Si vous êtes en mode interactif et qu'un exercice attend une réponse, le notebook n'affichera plus rien tant que le noyau attendra une réponse pour l'exercice. Soit vous répondez (si vous vous souvenez où c'est), soit vous stoppez et relancez le noyau (avec exécution de toutes les cellules de préférence).


## Pour nettoyer

Sous Linux avec juste le script `install.sh`:

    rm -rf ~/.local/bin ~/.local/share/jupyter ~/.jupyter/ ~/.local/lib  ~/.cache/pip/
    
À l'IUT, c'est plus compliqué à cause de l'environnement conda qui est utilisé pour avoir une version suffisante de python3/pip3.