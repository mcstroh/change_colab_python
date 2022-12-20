echo "Attempting to install Python $1"
sed "s/X\.XX/$1/g" change_colab_python/default.py > change_colab_python/run_me.py
chmod u+x change_colab_python/run_me.py
python change_colab_python/run_me.py
PY_VERSION=`python --version`
echo "Installed Python version: $PY_VERSION"
