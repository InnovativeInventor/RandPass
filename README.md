# SafePass
A new python-based random password generator that uses only safe words. This is aimed for children/school audiences.

# One-line install and setup
`curl -L https://git.io/vbiCp | sudo bash`
Now, when you type in `password <options>`, passwords should be generated for you.

# Setting up
Just clone this repository (and all submoduels) by typing in:
```
git clone --recursive https://github.com/InnovativeInventor/SafePass
```
Finally, execute the script by typing in:
```
python3 SafePass/password.py <options>

Usage:
    python3 password.py <options>
    -h --help                   Show help
    -c --complex                Specifies complex dictionary
    -n --numbers                Specifies length of the random number used
    -a --amount                 Specifies the amount of passwords to be generated
    -w --words                  Specifies the amount of passwords to be generated
```
