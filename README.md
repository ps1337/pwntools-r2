# pwntools-r2

Launch `radare2` from `pwntools`. This has been tested to work in combination with `tmux` - **other combinations may or may not work**. This *might* also work with other setups without `tmux` but that's not supported currently.

![alt text](https://github.com/ps1337/r/blob/master/pwntools-r2/pwntools-r2-demo.gif?raw=true)

As of now, only the Python2 version of `pwntools` is being actively maintained.
A version for the currently unmaintained Python3 [fork](https://github.com/arthaud/python3-pwntools) of `pwntools` will be released as soon as it's being actively maintained and updated with `pwntools-gdb` environment variable support.

## Ok How To Use This?

- Create a new pipenv: `pipenv --python 2.7`
- Install this: `pipenv install pwntools-r2`
- Enter the virtual environment: `pipenv shell`
- Code your 1337 exploit:

```
#!/usr/bin/env python2

from pwntools_r2 import *

# You might want to change this
context.terminal = ['tmux', 'splitw', '-v']

r2script = """
#r2.cmd('db sym.main')
#r2.cmd('aaa')
#r2.cmd('V!')
"""

p = r2dbg('./a', r2script=r2script)
p.interactive()
```

Be sure to not forget `interactive()` at the end :)

Please note that the commands for `r2` have to be prefixed with a `#`. If you want to pass additional parameters, you can use the same in the function prototype of `gdb.debug` from `pwntools`.

- Do stuff: `python2.7 ./exploit.py`


## Troubleshooting

- You can debug any errors with `context.log_level = 'DEBUG'` via your `pwntools` python script.
- If no terminal can be found or any weird errors come up, try setting `context.terminal` accordingly - e.g. to `urxvtc` or  `['tmux', 'splitw', '-v']`


# Credits

This is based on [this](https://gist.github.com/bannsec/43cf0f1b05ec37eb7e92a2922967bc46) and [this](https://github.com/Enigmatrix/pwntools-dbg-r2/tree/master/r2dbg).
