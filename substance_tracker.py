from dataclasses import dataclass
from typing import List, Dict, Iterable, Collection

UNIT = 'slices'
SUBSTANCE = 'pizza'


@dataclass
class DayDoseMean:
    day: str
    time_dose: Dict[float, float]

    @property
    def doses(self) -> List[float]:
        return list(
          self.time_dose.values()
        )

    @property
    def times(self) -> List[float]:
        return list(
          self.time_dose.keys()
        )

    @property
    def daily_dose(self) -> Iterable[float]:
        return sum(i for i in self.doses)

    @property
    def mean(self) -> float:
        return self.daily_dose / len(self.doses)

    @property
    def diff(self) -> Iterable[float]:
        return (
          abs(
            self.times[i] - self.times[i+1]
          ) for i in enumerate(self.times) - 1
        )

    @property
    def time_mean(self) -> float:
        return sum(self.diff) / len(self.times)

    @property
    def format(self):
        return (
            f'{self.day}{":":4}'
            f'{self.daily_dose}{UNIT:4}'
            f'{self.mean}{self.time_mean:7}'
        )


@dataclass
class WeekDoseMean:
    week_dose_mean: Collection[DayDoseMean]

    @property
    def weekly_dose(self) -> float:
        return sum(
            i.daily_dose
            for i in self.week_dose_mean
        )

    @property
    def weekly_mean(self) -> float:
        return sum(
            i.mean
            for i in self.week_dose_mean
        ) / 7

    @property
    def weekly_time_mean(self) -> float:
        return sum(
             i.time_mean
             for i in self.week_dose_mean
         ) / 7

    @property
    def echo(self):
        print(
            f'\n--------------------------\n'
            f'{"Day":7}{SUBSTANCE:7}'
            f'{"dM":6}tM\n'
            f'--------------------------'
        )

        print(
          '\n'.join(
             i.format
             for i in self.week_dose_mean
          )
        )

        print(
            f'--------------------------\n'
            f'Weekly {"dM":4} -> mean: '
            f'{self.weekly_mean}\n'
            f'Weekly {"tM":4} -> mean: '
            f'{self.weekly_time_mean}\n'
            f'--------------------------\n'
            f'Weekly dose -> {SUBSTANCE}:'
            f'{self.weekly_dose}{UNIT}\n'
            f'--------------------------'
        )


def main():
    week_date = WeekDoseMean(
        week_dose_mean=(
            DayDoseMean(
                day='Mon',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Tue',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Wed',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Thu',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Fri',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Sat',
                time_dose={
                  12: 1,
                  13: 1
                }
            ),
            DayDoseMean(
                day='Sun',
                time_dose={
                  12: 2,
                  14: 2
                }
            )
        )
    )
#    week_date.echo


if __name__ == '__main__':
    main()
