# InstagramDownloader
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

`python insta_down.py -l <photo_url>`

The photo url has the form *https://www.instagram.com/p/xxxxx* or *https://www.instagram.com/p/xxxxx/?taken-by=yyyyy*, you can copy it directly from your browser. 

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
