#!/bin/bash

# Made by Innovative Inventor at https://github.com/innovativeinventor.
# If you like this code, star it on GitHub!
# Contributions are always welcome.

# MIT License
# Copyright (c) 2017 InnovativeInventor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

latest_version=2.1

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -u|--uninstall)
    uninstall=YES
    shift # past argument
    ;;
esac
done

detect_uninstall() {
    if ! [ -e "/etc/SafePass/uninstall.sh" ]; then
        mkdir -p /etc/SafePass
        touch /etc/SafePass/uninstall.sh
        echo "#!/bin/bash" >> /etc/SafePass/uninstall.sh
    fi
}

if ! [ -e /etc/dict4schools ]; then
    echo "rm -r /etc/dict4schools" >> /etc/SafePass/uninstall.sh
fi

if ! [ "$(type -t password)" ] || ! [ -e /etc/dict4schools ] || ! [ $(password --version) == "$latest_version" ]; then
    detect_uninstall
    if [ -e password.py ]; then
        cp password.py /usr/local/bin/password
        cp dict4schools /etc/dict4schools

    elif [ -e SafePass ]; then
        cp SafePass/password.py /usr/local/bin/password
        cp SafePass/dict4schools /etc/dict4schools

    else
        git clone --quiet --recursive https://github.com/InnovativeInventor/SafePass
        mv SafePass/password.py /usr/local/bin/password
        mv SafePass/dict4schools /etc/dict4schools
        rm -r SafePass
    fi
    chmod +x /usr/local/bin/password
    password
    echo "rm /usr/local/bin/password" >> /etc/SafePass/uninstall.sh
    exit
fi

if [ "$uninstall" = YES ]; then
    echo "Uninstalling"
    bash /etc/SafePass/uninstall.sh
fi
