from npm_calmarendian_date import CalmarendianDate
from npm_calmarendian_date.c_date_config import CDateConfig


class MyConfig(object):
    today: CalmarendianDate = CalmarendianDate(CDateConfig.APOCALYPSE_EPOCH_ADR - 1)
    start_cycle: int = today.absolute_cycle_ref()[0]
    num_cycles: int = 2

    def __init__(self):
        print("INIT MyConfig")
        period = str(self.start_cycle)
        if self.num_cycles > 1:
            period = f"{period} - {self.start_cycle + self.num_cycles - 1}"
        self.title_string = f"Calmarendian General Elections: {period}"


conf: MyConfig = MyConfig()
