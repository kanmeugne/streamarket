# Analyzing commentators transfer between twitch streamers channels

This repository is about building visuals to understand how commentators flow between streamers channels on twitch.

**data**

The data are extracted from some of the chats that happen during the *pixel war* within selected french streamers channels.

# How to play

1. clone the repository somewhere on your computer

```shell
somewhere$ git clone https://github.com/kanmeugne/streamarket.git
somewhere$ cd streamarket
somewhere/streamarket$ ls
data  dataviz.ipynb  prepare.py   requirements.txt
```

2. build the dependencies before going further (it is preferable to use a virtual environment -- see [here](https://kanmeugne.github.io/posts/setting-up-virtual-environments-in-python/ "Kanmeugne's Blog: Setting up your virtual environment in python") for more details)

```shell
somewhere/streamarket$ pip install -r requirements.txt
```

3. launch the jupyter notebook and start playing with the data

```shell
somewhere/streamarket$ jupyter lab dataviz.ipynb
```

