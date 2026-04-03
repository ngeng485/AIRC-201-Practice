import unittest
from problems import run_experiments

class TestHW6(unittest.TestCase):
    def test_run_experiments(self):
        results = run_experiments()
        
        expected_strat1 = [126.0, 126.0, 126.0, 123.0, 128.0, 123.0, 123.0, 127.0, 124.0, 128.0]
        expected_strat2 = [102.0, 102.0, 102.0, 102.0, 102.0, 102.0, 102.0, 102.0, 101.0, 102.0]
        expected_strat3 = [101.0, 101.0, 101.0, 101.0, 101.0, 102.0, 101.0, 101.0, 101.0, 101.0]
        
        actual_strat1 = results[1][:, -1].tolist()
        actual_strat2 = results[2][:, -1].tolist()
        actual_strat3 = results[3][:, -1].tolist()
        
        self.assertEqual(actual_strat1, expected_strat1, f'Strategy 1 failed! Expected {expected_strat1}, got {actual_strat1}')
        self.assertEqual(actual_strat2, expected_strat2, f'Strategy 2 failed! Expected {expected_strat2}, got {actual_strat2}')
        self.assertEqual(actual_strat3, expected_strat3, f'Strategy 3 failed! Expected {expected_strat3}, got {actual_strat3}')

if __name__ == '__main__':
    # Define ANSI color codes
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Mapping of test method prefixes to Problem Names
    problem_map = {
        "run_experiments": "1. Run Experiments"
    }

    print(f"\n{BOLD}Running HW6 Tests...{RESET}\n")
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHW6)
    
    total_passed_overall = 0
    total_tests_overall = 0
    
    problem_summaries = []

    for problem_key, problem_display_name in problem_map.items():
        relevant_tests = []
        for test in suite:
            method_name = test._testMethodName
            if method_name.startswith("test_" + problem_key):
                 relevant_tests.append(test)
                 
        if not relevant_tests:
            continue
            
        passed = 0
        total = len(relevant_tests)
        problem_failures = []
        
        for test in relevant_tests:
            result = unittest.TestResult()
            test.run(result)
            if result.wasSuccessful():
                passed += 1
            else:
                failures = result.failures + result.errors
                for test_case, trace in failures:
                    problem_failures.append((test_case, trace))
        
        if problem_failures:
            print(f"{BOLD}{problem_display_name} Failures:{RESET}")
            for test_case, trace in problem_failures:
                 print(f"  {RED}FAIL: {test_case.id()}{RESET}")
                 indented_trace = "\n".join("    " + line for line in trace.splitlines())
                 print(indented_trace)
                 print()
        
        problem_summaries.append((problem_display_name, passed, total))

        total_passed_overall += passed
        total_tests_overall += total

    print("-" * 40)
    print(f"{BOLD}Summary:{RESET}")
    for name, passed, total in problem_summaries:
        if passed == total:
            color = GREEN
        elif passed == 0:
            color = RED
        else:
            color = RED 
            
        print(f"{name:<35} {color}[{passed}/{total}]{RESET}")

    print("-" * 40)
    final_color = GREEN if total_passed_overall == total_tests_overall else RED
    print(f"{BOLD}Total Progress:{RESET} {final_color}[{total_passed_overall}/{total_tests_overall}]{RESET}")
