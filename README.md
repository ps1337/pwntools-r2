# pwntools-r2

Launch `radare2` from `pwntools`. This has been tested to work in combination with `tmux` - **other combinations may or may not work**. This *might* also work with other setups without `tmux` but that's not supported currently.

## Ok How To Use This?

- Create a new pipenv: `pipenv --python 2.7`
- Install this: `pipenv install pwntools-r2`
- Enter the virtual environment: `pipenv shell`
- Do stuff: `python2.7 ./exploit.py`


## Troubleshooting

- You can debug any errors with `context.log_level = 'DEBUG'` via your `pwntools` python script.
- If no terminal can be found, try setting `context.terminal` accordingly - e.g. to `urxvtc`


# Credits

This is based on [this](https://gist.github.com/bannsec/43cf0f1b05ec37eb7e92a2922967bc46) and [this](https://github.com/Enigmatrix/pwntools-dbg-r2/tree/master/r2dbg).
