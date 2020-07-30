import unittest
from systems import subproc


class TestRunCmd(unittest.TestCase):

    def test1(self):
        cmd = ["sh", "-c", "lart"]
        ret = subproc.runCmd(cmd)
        # print("Return code: ", ret)




if __name__ == '__main__':
    unittest.main()
