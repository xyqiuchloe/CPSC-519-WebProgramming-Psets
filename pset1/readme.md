# pset1
### team 27, Xinyue Qiu xq44, Jie Zhu jz788

## Contribution

Jie 's contribution on writing the luxdetails.py, including all the modulized helper functions from  filter_details.py. Jie have also contributed to finding edge cases, writing boundary tests and test automation. 

Xinyue's contribution is mostly focused on lux.py and filters_obj.py, writing tests like unit tests, test automation, programming style correction.

Both of us have contributed evenly on composing documentations required for this problem set and debugging the command-line programs. 

## Help Received (people and resources)

Throughout the project, we have referred to demo codes of sql queries from class, and have taken use of the table.py to format our output. When writing the lux.py and luxdetails.py files, we have consulted with instructor for advice regarding sql queries. We have also taken use of online resources to write docstrings, unit tests, following the standard format. For all the online resources we have taken use of, a citation list is as follows:

### Citations for the online resources:
1. https://www.datacamp.com/tutorial/docstrings-python
2. https://docs.python.org/3/library/unittest.html
3. https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/

## Time Spent

We estimated each of us has spent about 6 hours on this assignment.

## Self-assessment on this assignment

Yes, we believe this assignment has enables us to explore: sql queries, command line programs, writing modules. We also learned how to handle user input, and ways to structure a command line program. We learned to use a range of packages like 'argparse' library, to parse command line arguemnts, and learned to use main() for testing the entire program.

One suggestion for improvement would be to add more robust error handling to the program. For example, if the user enters an invalid option or a search term that does not match any artwork in the gallery, the program currently does not provide any helpful feedback. Adding more descriptive error messages could help to improve the user experience. Additionally, adding more advanced search options, such as the ability to search by artist or date, could help to make the program more powerful.

## Additional Information

### Descriptions of all submitted documents and requirements

'lux.py' and 'luxdetails.py' composed two programs required for submission. The parameters required for these two command-line programs follows the input specification requirements of this assignment. Inside the file, we have included Error Handling that would capture the errors specified in pset requirements. We also submitted two modules that will help execute these two programs: 'filters_obj.py' and 'filters_detail.py'.

'test_lux.py' is a automated testing file which includes a list of command line/test cases we would like to run. To run this file, type 'python test_lux.py' in terminal and it will run automatically. The command lines executed upon call contains all the test cases we wanted to test. The output will be a coverage. file and htmlcov folder from coverage package. The test cases we put inside the test file included: objects that have no references, lots of references, agents with several nationalities, which also fits into purpose of boundary testing. Following these command line, we generated a test coverage report, which is named: 'coverage_index.html'. We consider these two files a combination of boundary tests and test automation. 

'out1' contains all the output we have generated from test_lux.py. To check if this matches the record from sql, we manually searched all of the test cases using sqlite studio, and have found out1 to be matching the sql queries output.

'unit_test_lux.py' and 'unit_test_luxdetails.py' contains unit testing for 'lux.py' and 'luxdetails.py' separately. We have included tests of modulized functions imported in the unit tests. We consider these two files a submission of unit testing requirement for this test. 

### Pylint suggested bugs

pylint has suggested that our 'lux.py', 'luxdetails.py' files are all near perfect(10/10). 
'filters_obj' suggested an error related to use of enumerate, and we think that leaving it as it is does not impede the functionality. In 'filters_obj.py' and 'filters_detail.py', pylint suggested that we a problem of catching too general excception. We think that using 'Exception' to handle all the exception situations is able to help us handle the errors, thus we believe that this problem is unavoidable. 

### Missing lines in Coverage report 

After statement tests, we have found that coverage of these files are: 100% for lux.py, 100% for luxdetails.py, 96% for filters_detail.py, and 93% for filters_obj.py. After careful review, we think all of the missing lines are due to exception handling using try-except block, and due to the 'return None' code we have put under helper function. We think this missing is unavoidable, because we are taking consideration of situations not commonly happening when we are running the program, e.g. missing database. Thus we think the coverage report not reaching 100% is reasonable. 
