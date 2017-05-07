# Auth Topic - DOM XSS #

## What is this? ##
This repository contains some test code for an Authentication Topic for a class. There are examples of both successful DOM XSS and failures (for modern web browsers) contained in the folders of the repo. The primary point with these examples is that DOM XSS is still very relevant in modern browsers due to developer error (not sanitizing input as well as decoding the URL encoding). There is also the possibility of attackers exploiting weaknesses in URL encoding, which is not discussed in these examples but would be an interesting topic to pursue.

## How to Run ##
- To run any of these examples, pip3 must be installed as well as Flask.
- To install pip on Linux, follow this [guide.](https://packaging.python.org/install_requirements_linux/)
To install Flask after pip, run:
```
pip3 install flask
```

- Once these dependencies have been addressed, run any example with:
```
python3 app.py
```
