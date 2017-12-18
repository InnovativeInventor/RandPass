# SafePass
A new python-based random password generator that uses only safe words. This is aimed for children/school audiences.

# One-line run/setup
If you only want to run this once, run this in Terminal.
`curl -L https://git.io/vb6av | python3`

If you want to save this, type in this command
`curl -L https://git.io/vb6av -o password.py | python3 password.py`

# Setting up
Just clone this repository (and all submoduels) by typing in:
```
git clone --recursive https://github.com/InnovativeInventor/SafePass
```
Then, change into the directory by typing in:
```
cd RandPass
```
Finally, execute the scrip by typing in:
```
python3 password.py <options>

Usage:
    python3 password.py <options>
    -h --help                   Show help
    -c --complex                Specifies complex dictionary
    -n --numbers                Specifies length of the random number used
    -a --amount                 Specifies the amount of passwords to be generated
    -w --words                  Specifies the amount of passwords to be generated
```
