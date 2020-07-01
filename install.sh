#!/bin/bash
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit
fi
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found"
    exit
fi
if ! command -v git &> /dev/null
then
    echo "git could not be found"
    exit
fi
pip3 install requests
git clone https://git.code.sf.net/p/mingw/mingw-org-wsl mingw-mingw-org-wsl
echo "Done"
