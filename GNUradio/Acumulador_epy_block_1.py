"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_Diff',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]

    
        )
        self.acum_anterior = 0
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        x= input_items[0]
        y0= output_items[0]

        N= len(x)
        diff= np.cumsum(x) - self.acum_anterior
        self.acum_anterior = diff[N-1]
        y0[:] = diff
        return len(y0)
