"""
I've got a new cowl; cold energy.
Each moment, valuable.
"""

# First thing is to outline the model of a moment.
# Yet, each moment has a context.

import datetime


class Moment:
    """
    General representation of a particular moment.

    Context ::
    Time :: 
    """

    # Constructor
    def __init__(
        self, baseline: float = 1, time: datetime.date = datetime.date.today()
    ):
        """
        # Set up time + date variables
        """
        self.baseline = baseline
        self.time = time

        return None

    # # Baseline
    # def rest(self, context: str = ""):
    #     self.context = context
    #     self.time = time
    #     return None
