mitchbarry.com
==============

Personal Website & Blog built with [Pelican](http://getpelican.com)!

##Required Software
1. [Python](https://www.python.org/download/releases/2.7.8/) (2.4+, 3.0+)
1. pip Python Package Manager ([pip Installation Guide](https://pip.pypa.io/en/latest/installing.html)) - **already bundled with Python >= 3.4 release**

##Getting Started

```bash
$> git clone https://github.com/mitch-b/web
$> cd web
```

The [Pure CSS theme](https://github.com/mitch-b/pelican-purecss) lives in another repo. To pull it into your local workspace, initialize the submodule.

```bash
$> git submodule update --init --recursive
```

##Create new VirtualEnv (Optional)
```bash
$> virtualenv ~/venv/web && source ~/venv/web/bin/activate
```

##Dependencies & Setup

```bash
$> pip install -r requirements.txt
```

##Generating Static Site

```bash
$> pelican content/ -s pelicanconf.py
$> cd output && python -m SimpleHTTPServer
```

Now, view your site at [http://localhost:8000/](http://localhost:8000)

##Deploying

Run the `init_makefile.py` module to generate the Makefile you'll want for deployment. Answer the questions at each prompt, and the file will be created. Then you can run the following command to use rsync to deploy your source.

```bash
$> python init_makefile.py # answer prompts
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
