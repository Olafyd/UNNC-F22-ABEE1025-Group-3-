# EnergyPlus, Copyright (c) 1996-2021, The Board of Trustees of the University
# of Illinois, The Regents of the University of California, through Lawrence
# Berkeley National Laboratory (subject to receipt of any required approvals
# from the U.S. Dept. of Energy), Oak Ridge National Laboratory, managed by UT-
# Battelle, Alliance for Sustainable Energy, LLC, and other contributors. All
# rights reserved.
#
# NOTICE: This Software was developed under funding from the U.S. Department of
# Energy and the U.S. Government consequently retains certain rights. As such,
# the U.S. Government has been granted for itself and others acting on its
# behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
# Software to reproduce, distribute copies to the public, prepare derivative
# works, and perform publicly and display publicly, and to permit others to do
# so.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# (1) Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
# (2) Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
# (3) Neither the name of the University of California, Lawrence Berkeley
#     National Laboratory, the University of Illinois, U.S. Dept. of Energy nor
#     the names of its contributors may be used to endorse or promote products
#     derived from this software without specific prior written permission.
#
# (4) Use of EnergyPlus(TM) Name. If Licensee (i) distributes the software in
#     stand-alone form without changes from the version obtained under this
#     License, or (ii) Licensee makes a reference solely to the software
#     portion of its product, Licensee must refer to the software as
#     "EnergyPlus version X" software, where "X" is the version number Licensee
#     obtained under this License and may not use a different name for the
#     software. Except as specifically required in this Section (4), Licensee
#     shall not use in a company name, a product name, in advertising,
#     publicity, or other promotional activities any name, trade name,
#     trademark, logo, or other designation of "EnergyPlus", "E+", "e+" or
#     confusingly similar designation, without the U.S. Department of Energy's
#     prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from ctypes import cdll, c_void_p


class StateManager:
    """
    This API class enables a client to create and manage state instances for using EnergyPlus API methods.
    Nearly all EnergyPlus API methods require a state object to be passed in, and when callbacks are made, the current
    state is passed as the only argument.  This allows client code to close the loop and pass the current state when
    making API calls inside callbacks.

    The state object is at the heart of accessing EnergyPlus via API, however, the client code should simply be a
    courier of this object, and never attempt to manipulate the object.  State manipulation occurs inside EnergyPlus,
    and attempting to modify it manually will likely not end well for the workflow.

    This class allows a client to create a new state, reset it, and free the object when finished with it.
    """

    def __init__(self, api: cdll):
        self.api = api
        self.api.stateNew.argtypes = []
        self.api.stateNew.restype = c_void_p
        self.api.stateReset.argtypes = [c_void_p]
        self.api.stateReset.restype = c_void_p
        self.api.stateDelete.argtypes = [c_void_p]
        self.api.stateDelete.restype = c_void_p

    def new_state(self) -> c_void_p:
        """
        This function creates a new state object that is required to pass into EnergyPlus Runtime API function calls

        :return: A pointer to a new state object in memory
        """
        return self.api.stateNew()

    def reset_state(self, state: c_void_p) -> None:
        """
        This function resets an existing state instance, thus resetting the simulation, including any registered
        callback functions.

        :return: Nothing
        """
        self.api.stateReset(state)

    def delete_state(self, state: c_void_p) -> None:
        """
        This function deletes an existing state instance, freeing the memory.

        :return: Nothing
        """
        self.api.stateDelete(state)
