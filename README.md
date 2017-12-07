# InstagramDownloader
[![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

Python tool to download media in full resolution from Instagram without an API access.

Since it doesn't use an API access, you can't download media from a private account.
### Compatible media
Right now InstagramDownloader is able to download single photo posts.

## Prerequisites
### Python version
Coded, build & tested in: `Python 3.6.3`
 
 I find really useful the tools [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage python versions in my computer.

### Aditional Packages

Required packages:

- `bs4`

You can install this packages using `pip`.

## Usage

For command line help: `python insta_down.py -h`

`python insta_down.py -l <photo_url>`

The photo url has the form *https://www.instagram.com/p/xxxxx* or *https://www.instagram.com/p/xxxxx/?taken-by=yyyyy*, you can copy it directly from your browser. 

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
