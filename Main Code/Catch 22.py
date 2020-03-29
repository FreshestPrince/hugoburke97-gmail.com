import datetime
import random
import unittest
import Test_GA

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


def get_fitness(guess, target):
    if target == guess.Fitness:
        return (guess)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        candidate.Genes, candidate.Fitness, timeDiff))


class TT(unittest.TestCase):
    def test(self):
        target = 0
        self.find_tt(target)

    def find_tt(self, target):
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        optimalFitness = 0
        best = Test_GA.get_best(fnGetFitness, optimalFitness, fnDisplay)
        self.assertEqual(best.Genes, target)


if __name__ == '__main__':
    unittest.main()
