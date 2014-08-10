mitchbarry.com
==============

Personal Website & Blog

Built with [Pelican](http://getpelican.com)!

##Required Software
1. Python (>2.4)
1. pip

##Getting Started

```bash
$> git clone https://github.com/mitch-b/web
$> cd web
```

##Dependency & Setup

###Windows
You'll want to ensure Fabric [can be installed](http://docs.fabfile.org/en/1.4.3/installation.html). Might be easiest to [install precompiled libraries](http://www.voidspace.org.uk/python/modules.shtml#pycrypto) as found here (according to your Python installation). Real easy to setup.

```bash
C:\\web\\> pip install -r requirements-win.txt
C:\\web\\> git update-index --assume-unchanged fabfile.py
```

###Non-Windows
```bash
$> pip install -r requirements.txt
$> git update-index --assume-unchanged Makefile
```

##Generating Static Site

```bash
$> pelican content/ -s pelicanconf.py
$> cd output && python -m SimpleHTTPServer
```

Now, view your site at [http://localhost:8000/](http://localhost:8000)

##Deploying

###Windows

Edit `fabfile.py` to include proper release details.

```bash
C:\\web\\> fab publish
```

###Non-Windows

Edit `Makefile` to include proper release details.

```bash
$> make rsync_upload
```

##Tips

If you want to keep Pelican updating your output directory, you can open a new window and run the following command:

```bash
$> pelican content/ -s pelicanconf.py --autoreload
```

###Licenses
This source is provided under MIT License.
This site uses material from:
1. [Pelican - GNUv3](https://github.com/getpelican/pelican/blob/master/LICENSE)
1. [PurePelicanTheme - GPLv3](https://github.com/PurePelicanTheme/pure/blob/master/LICENSE)
1. Some Pelican Plugins (under Pelican License)
1. [Tipue Search - MIT](http://www.tipue.com/search/docs/#license)
