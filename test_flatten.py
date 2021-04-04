import unittest
from flatten import flattener


class FlattenTests(unittest.TestCase):
    def test_output(self):

        # test with given GitHub input
        github_input = {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
            }
        }

        github_output = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
        }
                
        self.assertEqual(flattener(github_input), github_output)
        
        # test with input with no nesting
        no_nesting_input = {
            "a": 2,
            "b": True,
            "c": 7,
        }

        self.assertEqual(flattener(no_nesting_input), no_nesting_input)
       
        # test with input with multiple nesting
        multiple_nesting_input = {
            "a": 1,
            "b": True,
            "c": {
                "d": {
                    "e": 5,
                    "f": "test"
                },
                "g": 20
            }
        }

        multiple_nesting_output = {
            "a": 1,
            "b": True,
            "c.d.e": 5,
            "c.d.f": "test",
            "c.g": 20
        }

        self.assertEqual(flattener(multiple_nesting_input), multiple_nesting_output)


if __name__ == '__main__':
    unittest.main()