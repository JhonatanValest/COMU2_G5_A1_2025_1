"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Embedded Python Block example - a simple accumulate block"""

    def __init__(self):
        """Constructor for the accumulate block."""
        gr.sync_block.__init__(
            self,
            name='e_Acum',   # Name of the block in GRC
            in_sig=[np.float32],  # Input signature: single stream of float32
            out_sig=[np.float32]  # Output signature: single stream of float32
        )
        # Initialize an internal state variable to keep track of the cumulative sum
        self.accumulator = np.float32(0.0)

    def work(self, input_items, output_items):
        """Accumulate the input items and produce the output."""
        x = input_items[0]  # Input items
        y0 = output_items[0]  # Output items

        # Calculate the cumulative sum for the current input items
        y0[:] = np.cumsum(x) + self.accumulator

        # Update the internal accumulator with the last value of the cumulative sum
        self.accumulator = y0[-1]

        return len(y0)  # Return the number of output items processed
