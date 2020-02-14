The Behave testing tool can be organised into 3 parts -
1. The native code to be tested
2. Features: written tests to run. These are written in natural gerkhin language
3. Steps: The code which executes these features in tandem with the native code to be tested.

Running behave:

We have 2 modules available , base and network having test cases related to gene/tissue mapping and network features respectively
Navigate to the parent directory and run the command "behave features/<module>.features " to run all scenarios for a given module
run the command "behave features/<module>.features -n <name of scenario>" to run a particular scenario of a given module.
As required by the behave principles, the scenarios are fairly self explanatory

The result of the output is present in output folder. The results.txt file. A more in detailed explanation in a xml format is also available in the file TESTS-ds_test_<module>.xml where <module> is the module being tested.


Directory Structure:

1.The features folder contains the modules being tested. Currently the modules pertaining to gene/tissue mapping (base) and network functionalities(network) are present.
2. the gerkhin based scenarios are written in the feature file under the respective feature directory
3. The steps are implemented in the <module>.feature/steps directory
4. dataFiles directory contains files used commonly accross the program
5. testFiles directory contains testing files we can use to simulate large scenarios.
6. DS.py is the pilot code which implements the underlying diseascope module
7. behave.ini acts as the config file for predefining the behave runtime flags


