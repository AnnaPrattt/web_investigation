# Web Technology Practice
A practice web app to help junior security professionals use web tools. <br> <br>
This tool was designed to provide a simple web application that junior security professionals can investigate. Their investigation will help these professionals learn basic web functionals and tools, such as:
* HTTP methods
* Curl
* Dirb/GoBuster
* Browser Inspector

This site contains **SIX** flags.

## Requirements
* The application requires the `flask` library. <br>
* The infrastructure runs on port `8888`

## Usage
```python
pip3 install requirements.txt
python3 ./server.py
```

## Answers
See the `waklkthrough.md` file for instrucitons on how to get each flag.

## Future Work
* Add flag 7 that requires specific content in a POST body
* Add flag 8 that is hosted on an endpoint not listed in the common.txt DIRB wordlist
