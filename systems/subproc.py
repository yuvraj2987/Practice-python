import subprocess as subproc


def runCmd(cmd):
    try:
        ret = subproc.check_output(cmd)
        return ret
    except subproc.CalledProcessError as ch:
        print(ch)
        return ch.returncode
# runCmd
