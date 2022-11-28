# Word Descrambler

A small script to descramble a word whose letters were reordered randomly.

Example: **bsmlecra** => **scramble**

## Get Started

This project requires [Python 3](https://www.python.org/downloads/) to be installed on your machine.

First the project has to be downloaded. Then the required libraries can be installed by executing the following command in the project folder:

```console
pip install -r requirements.txt
```

Then the script can be executed with the following command:

```console
python main.py -w bsmlecra
```

## Further Information

Currently only one input word is supported, so it is not possible to descramble whole sentences. There currently is also only support for the English language.

If you need more complex deciphers, check out [Ciphey](https://github.com/Ciphey/Ciphey). Their tool is really powerful.

## Inspiration

The creation of this script was inspired by a [riddle](https://twitter.com/TFT/status/1448680016045346821) that *Teamfight Tactics* posted on Twitter.
