"""
Tests for A New Cowl ::
"""

# === Imports === #
import datetime
import pytest
import os

# Local imports
from moment import Moment


class TestMoment:
    """
    Basic unit tests for anewcowl.py.
    """

    def test_moment_time_datetime(self):
        """Test that Moment.time datatype is correct."""
        moment = Moment()
        assert isinstance(moment.time, datetime.date)
