import Runner_Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.first = Runner_Tournament.Runner('Усэйн', 10)
        self.second = Runner_Tournament.Runner('Андрей', 9)
        self.third = Runner_Tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        print(self.all_results)
        for result in self.all_results.values():
            show_result = {}
            for place, RT in result.items():
                show_result[place] = RT.name
            print(show_result)

    def test_run_1(self):
        dist = Runner_Tournament.Tournament(90, self.first, self.third)
        self.distance = dist.start()
        self.all_results['1'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_run_2(self):
        dist = Runner_Tournament.Tournament(90, self.second, self.third)
        self.distance = dist.start()
        self.all_results['2'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_run_3(self):
        dist = Runner_Tournament.Tournament(90, self.first, self.second, self.third)
        self.distance = dist.start()
        self.all_results['3'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')


if __name__ == '__main__':
    unittest.main()
