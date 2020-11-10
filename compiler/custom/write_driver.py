# See LICENSE for licensing information.
#
# Copyright (c) 2016-2019 Regents of the University of California and The Board
# of Regents for the Oklahoma Agricultural and Mechanical College
# (acting for and on behalf of Oklahoma State University)
# All rights reserved.
#
import debug
import design
import utils
from tech import GDS, layer
from tech import cell_properties as props


class write_driver(design.design):
    """
    Tristate write driver to be active during write operations only.
    This module implements the write driver cell used in the design. It
    is a hand-made cell, so the layout and netlist should be available in
    the technology library.
    """

    pin_names = [props.write_driver.pin.din,
                 props.write_driver.pin.bl,
                 props.write_driver.pin.br,
                 props.write_driver.pin.en,
                 props.write_driver.pin.vdd,
                 props.write_driver.pin.gnd]

    type_list = ["INPUT", "OUTPUT", "OUTPUT", "INPUT", "POWER", "GROUND"]
    cell_size_layer = "boundary"

    def __init__(self, name):
        super().__init__(name)
        debug.info(2, "Create write_driver")

        (width, height) = utils.get_libcell_size(self.cell_name,
                                                 GDS["unit"],
                                                 layer[self.cell_size_layer])

        pin_map = utils.get_libcell_pins(self.pin_names,
                                         self.cell_name,
                                         GDS["unit"])

        self.width = width
        self.height = height
        self.pin_map = pin_map
        self.add_pin_types(self.type_list)

    def get_bl_names(self):
        return props.write_driver.pin.bl

    def get_br_names(self):
        return props.write_driver.pin.br

    @property
    def din_name(self):
        return props.write_driver.pin.din

    @property
    def en_name(self):
        return props.write_driver.pin.en

    def get_w_en_cin(self):
        """Get the relative capacitance of a single input"""
        # This is approximated from SCMOS. It has roughly 5 3x transistor gates.
        return 5*3

    def build_graph(self, graph, inst_name, port_nets):
        """Adds edges based on inputs/outputs. Overrides base class function."""
        self.add_graph_edges(graph, port_nets)
