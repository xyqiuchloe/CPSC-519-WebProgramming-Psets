# Pset 2: Desktop GUI Application
### team 27, Jie Zhu jz788,  Xinyue Qiu xq44

## Contribution

Jie 's contribution on writing the dialog.py, lux.py, the client side of this web application, including the modularized helper functions from filter_details.py, filters_obj.py, and list_widget.py. Jie has also contributed to finding edge cases, writing boundary tests and programming style correction. 

Xinyue's contribution is mostly focused on modifying table.py, dialog.py, and luxserver.py, the server side of this web application, writing tests like unit tests, test automation, statement test, and programming style correction.

Both of us have contributed evenly on composing documentation required for this assignment and debugging the server side and client side of this web program. 

## Help Received (people and resources)

Throughout the project, we have referred to demo codes code1 and code2 folders from class, and have taken use of the table.py and dialog.py that we have used in pset1 to format our output and GUI. We have also taken use of online resources to write unit tests, use PySide6, and write the callback function. 

## Time Spent

We estimated each of us has spent about 6 hours on this assignment.

## Self-assessment on this assignment

Yes, we believe this assignment has enabled us to explore: Graphical User Interface and networking, pickling, based on QtSide6 and pickle package. We learned how to handle client input based on callback functions and how to build funnels for two-way communications. We have also learned how to do the error handling of unavailable ports and unavailable servers using ‘stderr’ and ‘QErrorMessage’.

One suggestion for improvement would be to change the view of information details. For example, if the user has clicked on the line in our output table, there will be a popup window displaying the information. However, for different laptops we are seeing a different view of this window, and we think we can improve further on this. 

## Additional Information

### Descriptions of all submitted documents and requirements

'lux.py' and 'luxserver.py' composed two programs required for submission. The parameters required for these two command-line programs follow the input specification requirements of this assignment. The lux.py file is responsible for the client side, and the luxserver.py file is responsible for the server side of our application. Inside the file, we have included Error Handling that would capture the errors specified in pset requirements. We also submitted two modules that will help execute the lux.py program: 'filters_obj.py' and 'filters_detail.py'.

For the purpose of both boundary test and statement tests, we have taken use of the coverage function in python and generated the coverage report as 'coverage_index.html'. After using the coverage function, we have run all of the edge cases and other common cases that we have identified in the previous assignment to generate the coverage report. The test cases we put inside the test file included: objects that have no references, lots of references, agents with several nationalities, which also fits into the purpose of boundary testing. 


### Pylint suggested bugs

pylint has suggested that our 'luxserver.py' file is near perfect(9.62/10). The errors not handled are: 
1) too general exception, which we think the broad-exception-caught is legit to use because it handles the errors we have foreseen in this pset.
2)The other error is ‘Unnecessarily calls dunder method \___str___.\, while we think it is necessary to use \__str__.\ because it is from the table.py function.  

Pylint has suggested the score of our ‘lux.py’ file is low (5.54/10). The errors not handled are: 
1) One major error suggested is an error like ‘No name 'QApplication' in module 'PySide6.QtWidgets' (no-name-in-module)’ . As suggested based on ed threads, we have decided to ignore this. 

### Missing lines in Coverage report 

After statement tests, we have found that coverage of our file ‘luxserver.py’ is 92%, with about 6 lines missing. We have accounted for these missing lines as our lines for exception/errors. 
