#! /bin/bash
source ../env/bin/activate
python manage.py graph_models -a > output.dot
dot -Tpng output.dot -o er_diagram.png
rm output.dot