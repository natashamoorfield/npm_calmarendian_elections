from config import conf
from npm_calmarendian_elections.electoral_cycle import ElectoralCycle


class Application(object):
    """
    An application to display details of seasonal elections in the Western Provinces.
    An application to illustrate the use of the npm_calmarendian_date package.
    """
    def __init__(self):
        self.election_cycle = ElectoralCycle(conf.start_cycle, cycles=conf.num_cycles)

    def run(self):
        """
        Print out the election schedule for the given period.
        """
        print(conf.title_string)
        print()
        print("Season               Date          Elections")
        for e in self.election_cycle.elections():
            print(f"{e.election_season():<20} {e.election_date}    {e.election_tiers()}")


if __name__ == '__main__':
    app = Application()
    app.run()
