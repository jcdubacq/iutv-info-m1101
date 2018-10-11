#! /bin/sh
for i in *.ipynb; do
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace "$i"
done

strip-nondeterminism tikz/*.png

