#!/bin/bash

VERSION=2
words=2
numbers=2
amount=1
complex=""

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -c|--complex)
    complex="complex"
    shift # past argument
    shift # past value
    ;;
    -w|--words)
    words="$2"
    shift # past argument
    shift # past value
    ;;
    -n|--numbers)
    numbers="$2"
    shift # past argument
    shift # past value
    ;;
    -h|--help)
    help=YES
    shift # past argument
    shift # past value
    ;;
    -a|--amount)
    amount="$2"
    shift # past argument
    shift # past value
    ;;
    -f|--file)
    file="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

if [ ! $file ]; then
    echo "    python3 password.py $complex $words $numbers"
    while [[ $count -lt $amount ]]; do
        python3 password.py $complex $words $numbers
        count=$[$count+1]
    done
elif [ $file ]; then
    echo "    python3 password.py $complex $words $numbers"
    while [[ $count -lt $amount ]]; do
        python3 password.py $complex $words $numbers >> $file
        count=$[$count+1]
    done
fi
help() {
    echo
    echo "Script version $VERSION"
    echo 'A tool for generating random passwords.'
    echo 'Usage: genpass.sh <options> <complex>'
    echo 'Options:'
    echo '   -h --help                   Show help'
    echo '   -c --complex                Specifies complex dictionary'
    echo '   -n --numbers                Specifies length of the random number used'
    echo '   -a --amount                 Specifies the amount of passwords to be generated'
    echo '   -w --words                 Specifies the amount of passwords to be generated'
}
