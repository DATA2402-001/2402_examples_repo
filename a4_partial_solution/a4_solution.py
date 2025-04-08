import pandas as pd
import numpy as np


class UFCAnalysis:

    def __init__(self):
        self.events_table = pd.read_csv('./a4_partial_solution/data/events.csv')
        self.fighters_table = pd.read_csv('./a4_partial_solution/data/fighters.csv')
        self.fights_table = pd.read_csv('./a4_partial_solution/data/fights.csv')
        self.stats_table = pd.read_csv('./a4_partial_solution/data/stats.csv')

        # convert to datetime series
        self.events_table['date'] = pd.to_datetime(self.events_table['date'])
        self.fighters_table['dob'] = pd.to_datetime(self.fighters_table['dob'])

        # drop rows missing winners and results
        missing_winners = pd.isna(self.fights_table['winner'])
        self.fights_table = self.fights_table[~missing_winners]

        missing_results = pd.isna(self.stats_table['result'])
        self.stats_table = self.stats_table[~missing_results]


    def question_1(self) -> None:
        # which fighters have the most wins and losses?
        pass


    def question_2(self) -> None:
        # What percentage of fights “go the distance”?
        pass


    def question_3(self) -> None:
        # are younger fighters more likely to win?

        # join both fighters' DOB to the fights table
        joined = pd.merge(
            self.fights_table[['event', 'fighter1', 'fighter2', 'winner']],
            self.fighters_table[['name', 'dob']],
            left_on='fighter1',
            right_on='name'
        )
        joined = pd.merge(
            joined,
            self.fighters_table[['name', 'dob']],
            left_on='fighter2',
            right_on='name',
            suffixes=['_1', '_2']
        )
        
        # age difference between fighter 1 and fighter 2
        # here positive difference means fighter 1 is older (earlier DOB)
        joined['age_diff'] = joined['dob_2'] - joined['dob_1']

        # drop missing dates  
        joined = joined.loc[~pd.isna(joined['age_diff'])]
        
        # correlation between age diff and fighter 1 winning
        r = joined['age_diff'].corr(joined['winner'] == joined['fighter1'])

        print('\n____Q3______')
        print('correlation between age diff and winning:', r)
        print('(negative correlation means advantage for younger fighter)')
        

    def question_4(self) -> None:
        # is there a stance advantage?
        joined = pd.merge(
            self.stats_table[['fighter', 'result']],
            self.fighters_table[['name', 'stance']],
            left_on='fighter',
            right_on='name'
        )

        southpaw = joined['stance'].isin(['Southpaw', 'Switch'])
        orthodox = joined['stance'] == 'Orthodox'

        sp_win_rate = (joined.loc[southpaw, 'result'] == 'win').mean()
        orth_win_rate = (joined.loc[orthodox, 'result'] == 'win').mean()

        print('\n____Q4______')
        print('southpaw win-rate', sp_win_rate)
        print('orthodox win-rate', orth_win_rate)


    def question_5(self) -> None:
        # which event was most exciting?
        pass


    def question_6(self) -> None:
        # Which fighter has dealt the most strikes to an opponent
        strikes = self.stats_table.groupby(['fighter', 'opponent'])\
            ['sig. str.'].agg(['sum', 'count'])
        
        most_strikes_matchup = strikes['sum'].idxmax()        

        print('\n____Q6______')
        print((f"{most_strikes_matchup[0]} hit {most_strikes_matchup[1]} "
               f"{strikes.loc[most_strikes_matchup, 'sum']:.0f} times "
               f"over {strikes.loc[most_strikes_matchup, 'count']} fights"))


    def question_7(self) -> None:
        # which fighter has the longest career?
        joined = pd.merge(
            self.events_table[['event', 'date']],
            self.fights_table[['event', 'fight']],
            on='event'
        )
        joined = pd.merge(
            joined,
            self.stats_table[['fight', 'fighter']]
        )
        
        dates = joined.groupby('fighter')['date'].agg(['min', 'max'])
        dates['span'] = dates['max'] - dates['min']

        longest_career = dates['span'].idxmax()

        print('\n____Q7______')
        print(dates.loc[longest_career])

analysis = UFCAnalysis()
analysis.question_1()
analysis.question_2()
analysis.question_3()
analysis.question_4()
analysis.question_5()
analysis.question_6()
analysis.question_7()
