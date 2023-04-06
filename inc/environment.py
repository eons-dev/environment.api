import os
import logging
import apie

class environment(apie.Endpoint):
    def __init__(this, name="environment"):
        super().__init__(name)

        this.supportedMethods = []

        this.allowedNext = [] # all

        this.requiredKWArgs.append('environment')

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return f'''\
Create a scoped environment by appending the environment name to the Endpoints requested.
For example, with 'environment=dev' the Endpoint 'whatever' would become 'whatever_dev'.
'''

    def Call(this):
        # Next should be nested, not flat (e.g. this.next.next...)
        # So, this should only ever affect 1 object.
        # However, it will also not fail if this.next is empty.
        this.next = [f"{n}_{this.environment}" for n in this.next]
