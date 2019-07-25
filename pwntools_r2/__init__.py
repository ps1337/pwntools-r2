from pwn import gdb


def r2dbg(args,
          r2script=None,
          exe=None,
          ssh=None,
          env=None,
          sysroot=None,
          **kwargs):
    gdbscript = ""
    if r2script:
        gdbscript += '\n'.join(cmd for cmd in r2script.split('\n'))
    # this calls pwntools-gdb internally
    return gdb.debug(args, gdbscript, exe, ssh, env, sysroot, **kwargs)
