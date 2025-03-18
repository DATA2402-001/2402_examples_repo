"""
Write all scoring logic classes by completing the class definitions in this file
"""

from abc import ABC, abstractmethod
import pandas as pd
import numpy as np


class ScoringLogic(ABC):

    @abstractmethod
    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        This method must accept a dataframe, add a new column of scores, and return the new dataframe
        """
        raise NotImplementedError('abstract method "score" must be implmented by child classes of ScoringLogic')


class LanguageScoringLogic(ScoringLogic):
    
    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        raise NotImplementedError('you must write this method!')


class EducationScoringLogic(ScoringLogic):
        
    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        ed_pts = {
            'Secondary school (high school diploma)': 5,
            'One-year degree, diploma or certificate': 15,
            'Two-year degree, diploma or certificate': 19,
            'Bachelor’s degree or other programs (three or more years)': 21,
            'Two or more certificates, diplomas, or degrees': 22,
            'Professional degree needed to practice in a licensed profession': 23,
            'University degree at the Master’s level': 23,
            'University degree at the Doctoral (PhD) level': 25,
        }

        # table['ed_score'] = table['education'].replace(ed_pts)

        # another way: use a loop
        for ed_level, pts in ed_pts.items():
            table.loc[table['education'] == ed_level, 'ed_score'] = pts

class WorkExpScoringLogic(ScoringLogic):

    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        raise NotImplementedError('you must write this method!')


class AgeScoringLogic(ScoringLogic):

    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        table = table.copy()

        # table['age_score'] = 12 - (table['age'] - 35)
        # table.loc[table['age'] < 35, 'age_score'] = 12
        # table.loc[table['age'] < 18, 'age_score'] = 0
        # table.loc[table['age'] > 47, 'age_score'] = 0
        
        # another way - construct a dict
        age_pts = dict()
        for age in range(18, 36):
            age_pts[age] = 12
        for age in range(36, 47):
            age_pts[age] = 12 - (age - 35)
        table['age_score'] = table['age'].replace(age_pts) # ages not in the dict will come out as NaN
        table.loc[table['age'] < 18, 'age_score'] = 0
        table.loc[table['age'] > 46, 'age_score'] = 0
        return table
        
        return table


class ArrangedEmployementScoringLogic(ScoringLogic):

    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        raise NotImplementedError('you must write this method!')


class AdaptabilityScoringLogic(ScoringLogic):

    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        each "yes" in the following columns is worth 5 pts:
        adaptability_spouse_language
        adaptability_spouse_education
        adaptability_spouse_work
        adaptability_you_education
        adaptability_you_employment
        adaptability_relatives
        A "yes" in adaptability_you_work is worth 10.
        Total pts capped at 10
        """

        table['adaptability_score'] = 0

        for column in [
            'adaptability_spouse_language',
            'adaptability_spouse_education',
            'adaptability_spouse_work',
            'adaptability_you_education',
            'adaptability_you_employment',
            'adaptability_relatives',
        ]:
            # one way:
            #  table.loc[table[column] == 'yes', 'adaptability_score'] += 5
            
            # another way:
            table['adaptability_score'] += table[column].replace({'yes': 5, 'no': 0})
            
        table.loc[table['adaptability_you_work'] == 'yes', 'adaptability_score'] += 10
        table['adaptability_score'] = np.minimum(10, table['adaptability_score'])
        return table


class FinalScoringLogic(ScoringLogic):

    def score(self, table: pd.DataFrame) -> pd.DataFrame:
        """
        Your method docstring here
        """
        raise NotImplementedError('you must write this method!')



# testing the age scoring
table = pd.DataFrame({'age': list(range(1, 51))})
age_scorer = AgeScoringLogic()
table = age_scorer.score(table)
print(table)