#!/usr/bin/env python3
# See LICENSE for licensing information.
#
# Copyright (c) 2016-2019 Regents of the University of California and The Board
# of Regents for the Oklahoma Agricultural and Mechanical College
# (acting for and on behalf of Oklahoma State University)
# All rights reserved.
#
import unittest
from testutils import *
import sys, os
sys.path.append(os.getenv("OPENRAM_HOME"))
import globals
from globals import OPTS
from sram_factory import factory
import debug


@unittest.skip("Multibank is not working yet.")
class sram_2bank_test(openram_test):

    def runTest(self):
        config_file = "{}/tests/configs/config".format(os.getenv("OPENRAM_HOME"))
        globals.init_openram(config_file)
        from sram_config import sram_config
        c = sram_config(word_size=16,
                        num_words=32,
                        num_banks=2)

        c.words_per_row=1
        c.recompute_sizes()
        debug.info(1, "Layout test for {}rw,{}r,{}w sram "
                   "with {} bit words, {} words, {} words per "
                   "row, {} banks".format(OPTS.num_rw_ports,
                                          OPTS.num_r_ports,
                                          OPTS.num_w_ports,
                                          c.word_size,
                                          c.num_words,
                                          c.words_per_row,
                                          c.num_banks))
        factory.reset()
        a = factory.create(module_type="sram", sram_config=c)
        self.local_check(a, final_verification=True)

        c.num_words=64
        c.words_per_row=2
        c.recompute_sizes()
        debug.info(1, "Layout test for {}rw,{}r,{}w sram "
                   "with {} bit words, {} words, {} words per "
                   "row, {} banks".format(OPTS.num_rw_ports,
                                          OPTS.num_r_ports,
                                          OPTS.num_w_ports,
                                          c.word_size,
                                          c.num_words,
                                          c.words_per_row,
                                          c.num_banks))
        factory.reset()
        a = factory.create(module_type="sram", sram_config=c)
        self.local_check(a, final_verification=True)

        c.num_words=128
        c.words_per_row=4
        c.recompute_sizes()
        debug.info(1, "Layout test for {}rw,{}r,{}w sram "
                   "with {} bit words, {} words, {} words per "
                   "row, {} banks".format(OPTS.num_rw_ports,
                                          OPTS.num_r_ports,
                                          OPTS.num_w_ports,
                                          c.word_size,
                                          c.num_words,
                                          c.words_per_row,
                                          c.num_banks))
        factory.reset()
        a = factory.create(module_type="sram", sram_config=c)
        self.local_check(a, final_verification=True)

        c.word_size=2
        c.num_words=256
        c.words_per_row=8
        c.recompute_sizes()
        debug.info(1, "Layout test for {}rw,{}r,{}w sram "
                   "with {} bit words, {} words, {} words per "
                   "row, {} banks".format(OPTS.num_rw_ports,
                                          OPTS.num_r_ports,
                                          OPTS.num_w_ports,
                                          c.word_size,
                                          c.num_words,
                                          c.words_per_row,
                                          c.num_banks))
        factory.reset()
        a = factory.create(module_type="sram", sram_config=c)
        self.local_check(a, final_verification=True)

        globals.end_openram()

# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main(testRunner=debugTestRunner())
