from npm_calmarendian_elections.election import Election


class ElectoralCycle(object):
    """
    Class for generating a sequence of Election objects for the required time period.
    By default, it will generate election objects for all seven seasons in the specified Cycle.
    Optionally it can be extended to an arbitrary number of Cycles.
    """
    def __init__(self, first_cycle: int, *, cycles: int = 1):
        self.start = first_cycle
        self.cycles = cycles

    def elections(self):
        """
        Generator yielding sequential Election objects.
        """
        count = 0
        while count < self.cycles:
            season = 1
            while season < 8:
                yield Election(self.start + count, season)
                season += 1
            count += 1
