<h1 align="center">stay-awake</h1>
<p align="center">
  <a href="https://pypi.org/project/stay-awake/">
    <img src="https://raw.githubusercontent.com/singhsidhukuldeep/stay-awake/main/images/sample.PNG" width="1080" alt="Go to https://pypi.org/project/stay-awake/">
  </a>
</p>
<p align="center">
<a href="https://pypi.org/project/stay-awake/"><img src="https://img.shields.io/pypi/pyversions/stay-awake" alt="Go to https://pypi.org/project/stay-awake/"/></a>
<a href="https://pypi.org/project/stay-awake/"><img src="https://img.shields.io/pypi/v/stay-awake" alt="Go to https://pypi.org/project/stay-awake/"/></a>
<a href="https://pypi.org/project/stay-awake/"><img src="https://img.shields.io/pypi/status/stay-awake" alt="Go to https://pypi.org/project/stay-awake/"/></a>
<a href="https://pypi.org/project/stay-awake/"><img src="https://img.shields.io/pypi/format/stay-awake" alt="Go to https://pypi.org/project/stay-awake/"/></a>
<a href="https://pypistats.org/packages/stay-awake"><img src="https://img.shields.io/pypi/dm/stay-awake"/></a>
<!--<img src="https://visitor-badge.glitch.me/badge?page_id=stay_awake" alt="Go to https://pypi.org/project/stay-awake/"/>-->
<img src="https://static.pepy.tech/personalized-badge/stay-awake?period=total&units=none&left_color=black&right_color=brightgreen&left_text=Total%20Downloads" alt="Go to https://pypi.org/project/stay-awake/"/>
</p>

Stay-Awake is a Simple Platform Independent Python package to keep your system awake without affecting workflow!

* Does this affect workflow? 
> No, this only get's triggered when you don't do any mouse movements!

* Is there a GUI?
> This was intended to be a light weight solution, so as of now it only has a CLI!

* How does it work?
> If in a span of 60 seconds you don't move your mouse, this script will automatically move your mouse for about 1 to 4 pixels randomly. There won't be any mouse displacement! If you are working, this will do absolutely nothing!



## Setup

### Installing Package
 
 ```shell
pip3 install stay-awake
 ```

### Running

```shell
python3 -m stay-awake
```

> You can also give custom timeouts
> Eg: for 5 minutes (default is 1 min) `python3 -m stay-awake 5`

**Important:** *Virtual Environment is recommended*


If getting issue in installing virtualenv on `windows`, use administrator privileges
    
  
<h2 align="center">🌟⭐✨STAR ME✨⭐🌟</h2>

<p align="center">
  <b>You can give me a small 🤓 dopmaine 🤝 support by ⭐STARRING⭐ this project</b>
  
<img src="https://api.star-history.com/svg?repos=singhsidhukuldeep/stay-awake&type=Date" width="70%" alt="🌟⭐✨STAR ME✨⭐🌟">
</p>


## Credits

### Maintained by

***Kuldeep Singh Sidhu*** 

Github: [github/singhsidhukuldeep](https://github.com/singhsidhukuldeep)
`https://github.com/singhsidhukuldeep`

Website: [Kuldeep Singh Sidhu (Website)](http://kuldeepsinghsidhu.com)
`http://kuldeepsinghsidhu.com`

LinkedIn: [Kuldeep Singh Sidhu (LinkedIn)](https://www.linkedin.com/in/singhsidhukuldeep/)
`https://www.linkedin.com/in/singhsidhukuldeep/`

### Contributors

The full list of all the contributors is available [here](https://github.com/singhsidhukuldeep/stay-awake/graphs/contributors)


[![website](https://forthebadge.com/images/badges/built-with-love.svg)](http://kuldeepsinghsidhu.com)

## Say Thanks

If this helped you in any way, it would be great if you could share it with others.

## Current Status

[![Issues](https://img.shields.io/github/issues/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/issues)
[![Total Commits](https://badgen.net/github/commits/singhsidhukuldeep/stay-awake/main)](https://github.com/singhsidhukuldeep/stay-awake/commits/main)
[![Contributors](https://badgen.net/github/contributors/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/graphs/contributors)
[![Forks](https://badgen.net/github/forks/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/network/members)
[![Stars](https://badgen.net/github/stars/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/stargazers)
[![Watchers](https://badgen.net/github/watchers/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/watchers)
[![Branches](https://badgen.net/github/branches/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake/branches)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python3.5+-1f425f.svg)](https://www.python.org/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![repo- size](https://img.shields.io/github/repo-size/singhsidhukuldeep/stay-awake)](https://github.com/singhsidhukuldeep/stay-awake)
[![Followers](https://img.shields.io/github/followers/singhsidhukuldeep?style=plastic&logo=github)](https://github.com/singhsidhukuldeep?tab=followers)


## Steps for publishing to `pypi` [This is just for me, Maybe!]

- `pip3 install setuptools twine`
- Go to project folder
- `python3 setup.py sdist`
- `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`

OR

Go to your project folder and:
```shell
pip3 install setuptools twine

python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
