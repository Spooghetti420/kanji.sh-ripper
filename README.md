# kanji.sh Ripper
This is a set of 5 programs, each downloading a different set of PDF worksheets for practicing Japanese kanji from the site [kanji.sh](kanji.sh).
I haven't included the final PDFs in this repository, but after discussions with the maintainer, that might be a nicer idea to stop us script-users
from wasting his bandwidth on these downloads. However, for now you can use these scripts to download all the sheets in a matter of 1 minute or so.
I've featured in a 1-second pause between sheet downloads: I know some sites have a blacklist that bans people who spam the site with requests.
If you want the download to go faster, comment out that line for the relevant script.

## Usage
There is one dependency, `requests`.
To install: `pip install requests`.
Then, to download a given sheetset, choose a program to run, e.g. `python frequency.py`, and it'll get downloading.
Good studies to you.

## Credit
Thanks to aruke, the maintainer of the kanji.sh site. Please check out aruke's ["Buy-me-a-coffee"](https://www.buymeacoffee.com/aruke) platform to buy him a sushi :)