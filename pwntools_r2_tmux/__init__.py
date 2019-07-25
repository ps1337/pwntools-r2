from pwn import gdb

def r2dbg(args, exe=None, ssh=None, env=None, sysroot=None, **kwargs):
    gdbscript = ""
    # this calls pwntools-gdb internally
    return gdb.debug(args, gdbscript, exe, ssh, env, sysroot, **kwargs)
