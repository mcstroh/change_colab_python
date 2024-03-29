import os #for restart routine
import subprocess # for bash run
import sys #for version checker

if 'X.XX' in sys.version:
    print('You already have X.XX')
else:
    
    command = """
    #install python X.XX and dev utils
    #you may not need all the dev libraries, but I haven't tested which aren't necessary.
    sudo apt-get update -y
    sudo apt-get install pythonX.XX pythonX.XX-dev pythonX.XX-distutils libpythonX.XX-dev 
    sudo apt-get install pythonX.XX-venv binfmt-support #recommended in install logs of the command above

    #change alternatives
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/pythonX.XX 2

    # install pip
    curl -sS https://bootstrap.pypa.io/get-pip.py | pythonX.XX
    python3 get-pip.py --force-reinstall

    #install colab's dependencies
    python3 -m pip install setuptools ipython traitlets==5.7.1 ipython_genutils ipykernel jupyter_console prompt_toolkit httplib2 astor numpy pandas

    #minor cleanup
    sudo apt autoremove

    #link to the old google package
    ln -s /usr/local/lib/python3.10/dist-packages/google /usr/local/lib/pythonX.XX/dist-packages/google
    #this is just to verify if X.XX folder was indeed created
    ls /usr/local/lib/pythonX.XX/
    """
    with open('install_python.sh','w') as file:
        file.write(command)
    subprocess.run(['bash','install_python.sh'])

    print("\n" + "="*50 + "\n")
    print("Manually restart the runtime and the new version should load.")
    print(" - Click on the RunTime menu at the top of the screen.")
    print(" - Choose 'Restart runtime'")
    print(" - Click 'Yes' to accept.")
    print(" - Next time you run a code cell, Colab will connect to the new version of Python.")
