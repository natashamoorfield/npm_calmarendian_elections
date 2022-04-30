from npm_calmarendian_date import CalmarendianDate


class Election(object):
    """
    Class that will generate information about an election for a given cycle/season.
    """
    def __init__(self, cycle: int, season: int):
        self.election_date = CalmarendianDate.from_date_string(f"{cycle:>03}-{season}-25-1")

    def election_season(self):
        """
        Return a string with the season name and cycle number.
        """
        return f"{self.election_date.season.name()} {self.election_date.absolute_cycle_ref()[0]}"

    def election_tiers(self) -> str:
        """
        Calculate which tiers of government will have elections in the given season and
        return a string listing those tiers.
        """
        tiers = []
        asr = self.election_date.absolute_season_ref()
        if asr % 4 == 1:
            tiers.append("Provincial")
        if asr % 3 == 1:
            tiers.append("County")
        if asr % 2 == 1:
            tiers.append("District")
        item_count = len(tiers)
        if item_count == 0:
            return "-- none --"
        out_string = ""
        for i, item in enumerate(tiers):
            if i + 1 == item_count:
                out_string += item
            elif i + 2 == item_count:
                out_string += item + " and "
            else:
                out_string += item + ", "
        return out_string
