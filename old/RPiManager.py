import logging
from p2p2 import P2P2 as Net
from old.HardwareManager import HardwareManager

class RPiManager(HardwareManager):

    def __init__(self, cfg, net: Net):
        super().__init__(self, cfg, net=net)
        self.logger = logging.getLogger("RPiManager")

    async def Control(self):
        while 1:
            r = super().net.recv()
            if r != None:
                super().cmd(r["cmd"])

    async def Report(self):
        while 1:
            super().net.send(
                {
                    "Type": "States",
                    "States": super().report_states()
                }
            )
            super().net.send(
                {
                    "Type": "Data",
                    "Data": super().report_data()
                }
            )
