import copy
import itertools
import random
import time
from random import shuffle, randrange, choice

import numpy as np
from MakeData import *

lectures = ['Subject 1', 'Subject 1', 'Subject 1', 'Subject 1', 'Subject 1', 'Subject 1', 'Subject 1', 'Subject 2',
            'Subject 2', 'Subject 2', 'Subject 2', 'Subject 2', 'Subject 2', 'Subject 2', 'Subject 3', 'Subject 3',
            'Subject 3', 'Subject 3', 'Subject 3', 'Subject 3', 'Subject 3', 'Subject 4', 'Subject 4', 'Subject 4',
            'Subject 4', 'Subject 4', 'Subject 4', 'Subject 4', 'Subject 5', 'Subject 5', 'Subject 5', 'Subject 5',
            'Subject 5', 'Subject 5', 'Subject 5', 'Subject 6', 'Subject 6', 'Subject 6', 'Subject 6', 'Subject 6',
            'Subject 6', 'Subject 6', 'Subject 7', 'Subject 7', 'Subject 7', 'Subject 7', 'Subject 7', 'Subject 7',
            'Subject 7', 'Subject 8', 'Subject 8', 'Subject 8', 'Subject 8', 'Subject 8', 'Subject 8', 'Subject 8',
            'Subject 9', 'Subject 9', 'Subject 9', 'Subject 9', 'Subject 9', 'Subject 9', 'Subject 9', 'Subject 10',
            'Subject 10', 'Subject 10', 'Subject 10', 'Subject 10', 'Subject 10', 'Subject 10', 'Subject 11',
            'Subject 11', 'Subject 11', 'Subject 11', 'Subject 11', 'Subject 11', 'Subject 11', 'Subject 12',
            'Subject 12', 'Subject 12', 'Subject 12', 'Subject 12', 'Subject 12', 'Subject 12', 'Subject 13',
            'Subject 13', 'Subject 13', 'Subject 13', 'Subject 13', 'Subject 13', 'Subject 13', 'Subject 14',
            'Subject 14', 'Subject 14', 'Subject 14', 'Subject 14', 'Subject 14', 'Subject 14', 'Subject 15',
            'Subject 15', 'Subject 15', 'Subject 15', 'Subject 15', 'Subject 15', 'Subject 15', 'Subject 16',
            'Subject 16', 'Subject 16', 'Subject 16', 'Subject 16', 'Subject 16', 'Subject 16', 'Subject 17',
            'Subject 17', 'Subject 17', 'Subject 17', 'Subject 17', 'Subject 17', 'Subject 17', 'Subject 18',
            'Subject 18', 'Subject 18', 'Subject 18', 'Subject 18', 'Subject 18', 'Subject 18', 'Subject 19',
            'Subject 19', 'Subject 19', 'Subject 19', 'Subject 19', 'Subject 19', 'Subject 19', 'Subject 20',
            'Subject 20', 'Subject 20', 'Subject 20', 'Subject 20', 'Subject 20', 'Subject 20', 'Subject 21',
            'Subject 21', 'Subject 21', 'Subject 21', 'Subject 21', 'Subject 21', 'Subject 21', 'Subject 22',
            'Subject 22', 'Subject 22', 'Subject 22', 'Subject 22', 'Subject 22', 'Subject 22', 'Subject 23',
            'Subject 23', 'Subject 23', 'Subject 23', 'Subject 23', 'Subject 23', 'Subject 23', 'Subject 24',
            'Subject 24', 'Subject 24', 'Subject 24', 'Subject 24', 'Subject 24', 'Subject 24', 'Subject 25',
            'Subject 25', 'Subject 25', 'Subject 25', 'Subject 25', 'Subject 25', 'Subject 25', 'Subject 26',
            'Subject 26', 'Subject 26', 'Subject 26', 'Subject 26', 'Subject 26', 'Subject 26', 'Subject 27',
            'Subject 27', 'Subject 27', 'Subject 27', 'Subject 27', 'Subject 27', 'Subject 27', 'Subject 28',
            'Subject 28', 'Subject 28', 'Subject 28', 'Subject 28', 'Subject 28', 'Subject 28', 'Subject 29',
            'Subject 29', 'Subject 29', 'Subject 29', 'Subject 29', 'Subject 29', 'Subject 29', 'Subject 30',
            'Subject 30', 'Subject 30', 'Subject 30', 'Subject 30', 'Subject 30', 'Subject 30', 'Subject 31',
            'Subject 31', 'Subject 31', 'Subject 31', 'Subject 31', 'Subject 31', 'Subject 31', 'Subject 32',
            'Subject 32', 'Subject 32', 'Subject 32', 'Subject 32', 'Subject 32', 'Subject 32', 'Subject 33',
            'Subject 33', 'Subject 33', 'Subject 33', 'Subject 33', 'Subject 33', 'Subject 33', 'Subject 34',
            'Subject 34', 'Subject 34', 'Subject 34', 'Subject 34', 'Subject 34', 'Subject 34', 'Subject 1-Lab',
            'Subject 2-Lab', 'Subject 4-Lab', 'Subject 6-Lab', 'Subject 8-Lab', 'Subject 10-Lab', 'Subject 12-Lab',
            'Subject 13-Lab', 'Subject 15-Lab', 'Subject 17-Lab', 'Subject 21-Lab', 'Subject 23-Lab', 'Subject 30-Lab',
            'Subject 32-Lab']
Lecturer_Subjects = {
    'Jane Courtney ': ['Subject 1', 'Subject 2', 'Subject 9', 'Subject 10', 'Subject 11', 'Subject 13', 'Subject 16',
                       'Subject 17', 'Subject 19', 'Subject 21', 'Subject 22', 'Subject 23', 'Subject 25', 'Subject 26',
                       'Subject 28', 'Subject 30', 'Subject 32', 'Subject 1-Lab', 'Subject 2-Lab', 'Subject 10-Lab',
                       'Subject 13-Lab', 'Subject 17-Lab', 'Subject 21-Lab', 'Subject 23-Lab', 'Subject 30-Lab',
                       'Subject 32-Lab'],
    'Nam Mckeller \xa0': ['Subject 4', 'Subject 7', 'Subject 12', 'Subject 18', 'Subject 19', 'Subject 20',
                          'Subject 24', 'Subject 25', 'Subject 28', 'Subject 30', 'Subject 33', 'Subject 4-Lab',
                          'Subject 12-Lab', 'Subject 30-Lab'],
    'Kristle Benshoof \xa0': ['Subject 5', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 11', 'Subject 12',
                              'Subject 13', 'Subject 16', 'Subject 18', 'Subject 20', 'Subject 23', 'Subject 28',
                              'Subject 30', 'Subject 31', 'Subject 33', 'Subject 8-Lab', 'Subject 12-Lab',
                              'Subject 13-Lab', 'Subject 23-Lab', 'Subject 30-Lab'],
    'Freddie Seabrook \xa0': ['Subject 1', 'Subject 2', 'Subject 4', 'Subject 7', 'Subject 8', 'Subject 9',
                              'Subject 10', 'Subject 14', 'Subject 16', 'Subject 18', 'Subject 19', 'Subject 23',
                              'Subject 24', 'Subject 26', 'Subject 27', 'Subject 34', 'Subject 1-Lab', 'Subject 2-Lab',
                              'Subject 4-Lab', 'Subject 8-Lab', 'Subject 10-Lab', 'Subject 23-Lab'],
    'Katherina Boutwell \xa0': ['Subject 3', 'Subject 4', 'Subject 5', 'Subject 8', 'Subject 10', 'Subject 11',
                                'Subject 13', 'Subject 14', 'Subject 15', 'Subject 16', 'Subject 17', 'Subject 18',
                                'Subject 19', 'Subject 20', 'Subject 26', 'Subject 28', 'Subject 31', 'Subject 33',
                                'Subject 4-Lab', 'Subject 8-Lab', 'Subject 10-Lab', 'Subject 13-Lab', 'Subject 15-Lab',
                                'Subject 17-Lab'],
    'Irina Foose \xa0': ['Subject 2', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 10', 'Subject 13', 'Subject 15',
                         'Subject 19', 'Subject 23', 'Subject 25', 'Subject 26', 'Subject 28', 'Subject 29',
                         'Subject 30', 'Subject 2-Lab', 'Subject 8-Lab', 'Subject 10-Lab', 'Subject 13-Lab',
                         'Subject 15-Lab', 'Subject 23-Lab', 'Subject 30-Lab'],
    'Nancy Riess \xa0': ['Subject 1', 'Subject 5', 'Subject 11', 'Subject 13', 'Subject 15', 'Subject 18', 'Subject 19',
                         'Subject 21', 'Subject 24', 'Subject 28', 'Subject 33', 'Subject 1-Lab', 'Subject 13-Lab',
                         'Subject 15-Lab', 'Subject 21-Lab'],
    'Tyesha Gong \xa0': ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 9',
                         'Subject 10', 'Subject 13', 'Subject 14', 'Subject 17', 'Subject 20', 'Subject 27',
                         'Subject 28', 'Subject 30', 'Subject 31', 'Subject 32', 'Subject 33', 'Subject 1-Lab',
                         'Subject 2-Lab', 'Subject 4-Lab', 'Subject 6-Lab', 'Subject 10-Lab', 'Subject 13-Lab',
                         'Subject 17-Lab', 'Subject 30-Lab', 'Subject 32-Lab'],
    'Cathryn Bendel \xa0': ['Subject 4', 'Subject 5', 'Subject 10', 'Subject 11', 'Subject 13', 'Subject 14',
                            'Subject 17', 'Subject 20', 'Subject 23', 'Subject 25', 'Subject 26', 'Subject 28',
                            'Subject 29', 'Subject 33', 'Subject 4-Lab', 'Subject 10-Lab', 'Subject 13-Lab',
                            'Subject 17-Lab', 'Subject 23-Lab'],
    'Paul Vandergrift \xa0': ['Subject 1', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 9', 'Subject 10',
                              'Subject 13', 'Subject 15', 'Subject 17', 'Subject 18', 'Subject 20', 'Subject 21',
                              'Subject 24', 'Subject 25', 'Subject 26', 'Subject 27', 'Subject 31', 'Subject 32',
                              'Subject 33', 'Subject 1-Lab', 'Subject 4-Lab', 'Subject 6-Lab', 'Subject 10-Lab',
                              'Subject 13-Lab', 'Subject 15-Lab', 'Subject 17-Lab', 'Subject 21-Lab', 'Subject 32-Lab'],
    'Nisha Pal \xa0': ['Subject 1', 'Subject 6', 'Subject 8', 'Subject 9', 'Subject 11', 'Subject 12', 'Subject 13',
                       'Subject 15', 'Subject 16', 'Subject 18', 'Subject 19', 'Subject 20', 'Subject 21', 'Subject 22',
                       'Subject 24', 'Subject 25', 'Subject 26', 'Subject 28', 'Subject 29', 'Subject 30', 'Subject 32',
                       'Subject 33', 'Subject 1-Lab', 'Subject 6-Lab', 'Subject 8-Lab', 'Subject 12-Lab',
                       'Subject 13-Lab', 'Subject 15-Lab', 'Subject 21-Lab', 'Subject 30-Lab', 'Subject 32-Lab'],
    'Ian Hooper \xa0': ['Subject 2', 'Subject 4', 'Subject 7', 'Subject 8', 'Subject 12', 'Subject 17', 'Subject 23',
                        'Subject 24', 'Subject 26', 'Subject 29', 'Subject 30', 'Subject 31', 'Subject 33',
                        'Subject 34', 'Subject 2-Lab', 'Subject 4-Lab', 'Subject 8-Lab', 'Subject 12-Lab',
                        'Subject 17-Lab', 'Subject 23-Lab', 'Subject 30-Lab'],
    'Lavenia Abdalla \xa0': ['Subject 1', 'Subject 7', 'Subject 10', 'Subject 11', 'Subject 12', 'Subject 13',
                             'Subject 14', 'Subject 15', 'Subject 17', 'Subject 18', 'Subject 19', 'Subject 20',
                             'Subject 22', 'Subject 23', 'Subject 26', 'Subject 29', 'Subject 32', 'Subject 33',
                             'Subject 1-Lab', 'Subject 10-Lab', 'Subject 12-Lab', 'Subject 13-Lab', 'Subject 15-Lab',
                             'Subject 17-Lab', 'Subject 23-Lab', 'Subject 32-Lab'],
    'Tiffani Iannotti \xa0': ['Subject 1', 'Subject 3', 'Subject 5', 'Subject 9', 'Subject 11', 'Subject 13',
                              'Subject 14', 'Subject 15', 'Subject 16', 'Subject 24', 'Subject 25', 'Subject 28',
                              'Subject 31', 'Subject 33', 'Subject 1-Lab', 'Subject 13-Lab', 'Subject 15-Lab'],
    'Hobert Pascarella \xa0': ['Subject 2', 'Subject 4', 'Subject 5', 'Subject 7', 'Subject 8', 'Subject 9',
                               'Subject 11', 'Subject 12', 'Subject 15', 'Subject 16', 'Subject 17', 'Subject 18',
                               'Subject 22', 'Subject 23', 'Subject 25', 'Subject 26', 'Subject 28', 'Subject 32',
                               'Subject 2-Lab', 'Subject 4-Lab', 'Subject 8-Lab', 'Subject 12-Lab', 'Subject 15-Lab',
                               'Subject 17-Lab', 'Subject 23-Lab', 'Subject 32-Lab'],
    'Kylee Giblin \xa0': ['Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 13', 'Subject 14', 'Subject 15',
                          'Subject 18', 'Subject 19', 'Subject 27', 'Subject 30', 'Subject 33', 'Subject 34',
                          'Subject 6-Lab', 'Subject 8-Lab', 'Subject 13-Lab', 'Subject 15-Lab', 'Subject 30-Lab'],
    'Eliza Biddle \xa0': ['Subject 1', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8',
                          'Subject 15', 'Subject 16', 'Subject 17', 'Subject 18', 'Subject 19', 'Subject 21',
                          'Subject 24', 'Subject 25', 'Subject 27', 'Subject 28', 'Subject 33', 'Subject 34',
                          'Subject 1-Lab', 'Subject 4-Lab', 'Subject 6-Lab', 'Subject 8-Lab', 'Subject 15-Lab',
                          'Subject 17-Lab', 'Subject 21-Lab'],
    'Waltraud Fill \xa0': ['Subject 3', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 10', 'Subject 11',
                           'Subject 12', 'Subject 13', 'Subject 14', 'Subject 20', 'Subject 21', 'Subject 22',
                           'Subject 23', 'Subject 24', 'Subject 28', 'Subject 29', 'Subject 31', 'Subject 6-Lab',
                           'Subject 8-Lab', 'Subject 10-Lab', 'Subject 12-Lab', 'Subject 13-Lab', 'Subject 21-Lab',
                           'Subject 23-Lab'],
    'Joi Shriver \xa0': ['Subject 1', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 8', 'Subject 10', 'Subject 12',
                         'Subject 20', 'Subject 21', 'Subject 23', 'Subject 24', 'Subject 27', 'Subject 28',
                         'Subject 32', 'Subject 1-Lab', 'Subject 4-Lab', 'Subject 6-Lab', 'Subject 8-Lab',
                         'Subject 10-Lab', 'Subject 12-Lab', 'Subject 21-Lab', 'Subject 23-Lab', 'Subject 32-Lab'],
    'Ruth Frew \xa0': ['Subject 1', 'Subject 4', 'Subject 5', 'Subject 9', 'Subject 11', 'Subject 12', 'Subject 13',
                       'Subject 14', 'Subject 21', 'Subject 24', 'Subject 25', 'Subject 26', 'Subject 27', 'Subject 30',
                       'Subject 31', 'Subject 32', 'Subject 34', 'Subject 1-Lab', 'Subject 4-Lab', 'Subject 12-Lab',
                       'Subject 13-Lab', 'Subject 21-Lab', 'Subject 30-Lab', 'Subject 32-Lab']}
Classroom_Size = {'Classroom A': [150], 'Classroom B': [200], 'Classroom C': [50], 'Classroom D': [50],
                  'Classroom E': [40], 'Classroom F': [90], 'Classroom G': [200], 'Classroom H': [220],
                  'Classroom I': [100], 'Classroom J': [40], 'Classroom K': [50]}
Classroom_Free = {
    'Time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
             57, 58, 59, 60, 61, 62, 63, 64, 65],
    'Classroom A': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom B': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom C': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom D': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom E': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom F': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom G': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom H': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom I': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom J': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Classroom K': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

Lecturer_Free = {
    'Time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
             57, 58, 59, 60, 61, 62, 63, 64, 65],
    'Jane Courtney ': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
                       1],
    'Nam Mckeller \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1],
    'Kristle Benshoof \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1],
    'Freddie Seabrook \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1],
    'Katherina Boutwell \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1],
    'Irina Foose \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1],
    'Nancy Riess \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1],
    'Tyesha Gong \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1],
    'Cathryn Bendel \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1],
    'Paul Vandergrift \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1],
    'Nisha Pal \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1],
    'Ian Hooper \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1],
    'Lavenia Abdalla \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1],
    'Tiffani Iannotti \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1],
    'Hobert Pascarella \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               1, 1, 1, 1, 1],
    'Kylee Giblin \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1],
    'Eliza Biddle \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1],
    'Waltraud Fill \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 1],
    'Joi Shriver \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1],
    'Ruth Frew \xa0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1]}
Lab_Free = {
    'Time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
             57, 58, 59, 60, 61, 62, 63, 64, 65],
    'Lab A': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Lab B': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Lab C': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Lab D': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Lab E': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Lab F': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}


def getInitialPopulation(lectures, classrooms, labs, Lecturer_Subjects, population):
    timetables = []
    fitness_list = []
    for pop in range(population):
        classes = []
        for lecture in lectures:
            if lecture[-4:] == "-Lab":
                typ = "Lab"
                classroom = choice(labs)
            else:
                typ = "Lecture"
                classroom = choice(classrooms)
            classes.append([randrange(0, 64), classroom, choice(get_keys(Lecturer_Subjects, lecture)), lecture, typ])
        timetables.append(classes)
        fitness = calc_fitness(classes, 0, 1, 2)
        fitness_list.append(fitness)
    return timetables, fitness_list


import copy
import random
import time
import numpy as np


def mutate(chromosome, MUTATION_PROBABILITY):
    for i in range(len(chromosome)):
        if np.random.uniform(0.0, 1.0) < MUTATION_PROBABILITY:
            if np.random.random() < 0.5:
                randomRoom = choice(rooms)
                chromosome[i][1] = randomRoom
            else:
                randomTimeSlot = random.randint(0, 64)
                chromosome[i][2] = randomTimeSlot
    return chromosome


def calc_fitness(lst, index1, index2, index3):
    fitness = len(lst)  # When parsing through list, items count themselves in fitness,
    # to combat this, set fitness to the length of the list.
    for items in lst:
        for pieces in lst:
            if [items[index1], items[index2]] == [pieces[index1], pieces[index2]] \
                    or [items[index1], items[index3]] == [pieces[index1], pieces[index3]]:
                fitness -= 1
    return int(fitness/2)


def rouletteWheelFitnessSelection(choices):
    choices = [abs(k) for k in choices]
    max = sum(choices)
    pick = random.uniform(0, max)
    current = 0
    parent1 = random.choice(choices)
    parent2 = random.choice(choices)
    for key, value in enumerate(choices):
        current += value
        if current > pick:
            parent1 = key
            parent2 = key
            break
    while (parent1 == parent2):
        pick = random.uniform(0, max)
        current = 0
        for key, value in enumerate(choices):
            current += value
            if current > pick:
                parent2 = key
                break
    return parent1, parent2


def uniformCrossover(parent1, parent2):
    child = [[] for _ in range(len(parent1))]
    for i in range(len(parent1)):
        if np.random.uniform(0.0, 1.0) < 0.5:
            child[i] = copy.copy(parent1[i])
        else:
            child[i] = copy.copy(parent2[i])
    return child


def getNewGeneration(population, populationFitness):
    newGeneration = [copy.copy(population[-1])]
    newGenerationFitness = [copy.copy(populationFitness[-1])]
    while (len(newGeneration) < POPULATION_SIZE):
        parent1, parent2 = rouletteWheelFitnessSelection(populationFitness)
        if (np.random.uniform(0.0, 1.0) < CROSSOVER_PROBABILITY):
            child = uniformCrossover(population[parent1], population[parent2])
        else:
            child = population[parent1]
        child = mutate(child, MUTATION_PROBABILITY)
        isDuplicated = False
        for j in range(len(newGeneration)):
            if (child == newGeneration[j]):
                isDuplicated = True
                break
        if (not isDuplicated):
            index1 = 0
            index2 = 1
            index3 = 2
            childFitness = calc_fitness(child, index1, index2, index3)
            newGeneration.append(copy.copy(child))
            newGenerationFitness.append(copy.copy(childFitness))
    return newGeneration, newGenerationFitness


POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.025
CROSSOVER_PROBABILITY = 1.0
MAX_NUMBER_OF_GENERATIONS = 1000
MAX_NO_PROGRESS_GENERATIONS = 150

rooms = classrooms = (list(Classroom_Size.keys()))[1:]
labs = (list(Lab_Free.keys()))
shuffle(classrooms)
shuffle(lectures)
shuffle(labs)
maxFit = []
stopCondition = False
noProgressGenerations = 0
numberOfGenerations = 0
maximumAtGen = 0
t0 = time.time()
population, populationFitness = getInitialPopulation(lectures, classrooms, labs, Lecturer_Subjects, POPULATION_SIZE)
while (not stopCondition):
    newGeneration, newGenerationFitness = getNewGeneration(population, populationFitness)
    if (populationFitness[-1] == newGenerationFitness[-1]):
        noProgressGenerations += 1
    else:
        noProgressGenerations = 0
    population = copy.copy(newGeneration)
    populationFitness = copy.copy(newGenerationFitness)
    numberOfGenerations += 1
    print("Generation number", numberOfGenerations)
    if (numberOfGenerations >= MAX_NUMBER_OF_GENERATIONS or populationFitness[
        -1] == 1.0 or noProgressGenerations > MAX_NO_PROGRESS_GENERATIONS):
        stopCondition = True
    maxFit.append(populationFitness[-1])
    if (populationFitness[-1] < 0.01):
        maximumAtGen += 1
    print(populationFitness[-1])
print(populationFitness[-1])
print(maximumAtGen)
print("---------")
t1 = time.time()
total = t1 - t0
print(total, "seconds.")
