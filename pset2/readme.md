# Pset 2: Desktop GUI Application

### Due Friday March 10 11:59 PM NHT (New Haven Time)

## Table of Contents
- [Pset 2: Desktop GUI Application](#pset-2-desktop-gui-application)
    - [Due Friday March 10 11:59 PM NHT (New Haven Time)](#due-friday-march-10-1159-pm-nht-new-haven-time)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Rules](#rules)
  - [Getting Started](#getting-started)
  - [Your Task](#your-task)
  - [The Database](#the-database)
  - [The `lux.py` Program](#the-luxpy-program)
  - [The `luxserver.py` Program](#the-luxserverpy-program)
  - [Communication among tiers](#communication-among-tiers)
    - [The Justification](#the-justification)
  - [Communication with the Database](#communication-with-the-database)
    - [The Justification](#the-justification-1)
  - [Source Code Guide](#source-code-guide)
  - [Input Specification](#input-specification)
  - [Error Handling](#error-handling)
    - [Unavailable Port](#unavailable-port)
    - [Unavailble Server](#unavailble-server)
  - [Testing](#testing)
    - [Boundary Testing](#boundary-testing)
    - [Statement Testing](#statement-testing)
    - [Unit Testing](#unit-testing)
  - [Program Style](#program-style)
  - [Advice](#advice)
  - [Submission](#submission)
    - [Late Submissions](#late-submissions)
  - [Grading](#grading)

## Purpose

The purpose of this assignment is to help you learn or review graphical user interface programming and network programming in Python.

---

## Rules

You may work with one teammate on this assignment, and we prefer that you do so.

It must be the case that either you submit all of your team’s files or your teammate submits all of your team’s files.
(It must not be the case that you submit some of your team’s files and your teammate submits some of your team’s files.)
Your `README` file and your source code files must contain your name and your teammate’s name.

---

## Getting Started
> **Note**: this section contains exactly the text on the Canvas assignment, reproduced here only for completeness of this document.
> Since you made it here, you can safely ignore this section.

1. Accept [this GitHub classroom assignment](https://classroom.github.com/a/XUtBm54Q).
    * Select your team.
    * This step creates a GitHub repository for your team and links your team members' GitHub ids.
        * If you do not have a GitHub account, you are required to create one for this course
    * Use this git repository to track your assignment development.

1. Download the `lux.sqlite` database file from Canvas (or copy it over from your previous assignment) and place it in your new repository folder.
    > **Important**: Do not track `lux.sqlite` in your git repository.
    > It is too large to be hosted on GitHub and recovering from an error telling you that is challenging at best.
    > The included `.gitignore` file in the template repository will help with this, so *do not change or remove* that file.
    > You may keep the database file in the repository folder, but you must be careful not to *track* it.

---

## Your Task

As with Pset 1, assume you are working for the Yale University Art Galleries.
You are given a database containing data about objects and artwork stored in the gallery's collection.
Your task is to compose an application that allows museum visitors and other interested parties to query the database.

Your application must consist of two programs: a **client program** calld `lux.py` and a **server program** called `luxserver.py`.
Your `lux.py` program must have a **graphical user interface** and must communicate over a network with your `luxserver.py` program.
The `luxserver.py` program might be running on the same computer as `lux.py`, or it might be running on a different computer: the application must behave identically in either case.

---

## The Database

The database is identical to the one from Pset 1.
Refer to the Pset 1 specification for the list of tables and fields in the database.
As with Pset 1, the database is in a file named `lux.sqlite` that you should copy into your repository.

---

## The `lux.py` Program

When executed with `-h` as a command-line argument, your `lux.py` must display a help message that describes the program's behavior:

```
$ python lux.py -h
usage: lux.py [-h] host port

Client for the YUAG application

positional arguments:
  host        the host on which the server is running
  port        the port at which the server is listening

optional arguments:
  -h, --help  show this help message and exit
```

Your `lux.py` must accept exactly two command-line arguments. The first must be the **host**: the IP address or domain name of the computer on which your `luxserver.py` is running.
The second must be the number of the port at which your `luxserver.py` is listening.

As noted previously, your `lux.py` must have a graphical user interface.
Your graphical user interface must have these properties:
* It must be built using the `PyQt6` or `PySide6` GUI framework.
  > **Note**: The `PyQt6` framework is only intermittently compatible with Apple Silicon CPUs (M1, M2).
  > Use `PySide6` if you have such a machine, just to be safe.
  > Fortunately, all relevant class, type, and function names are identical between the two packages.
* When the application is launched, the main window should be no larger than $\frac{1}{4}$ of the total screen area (*i.e.*, no wider than $\frac{1}{2}$ of the screen's width and no taller than $\frac{1}{2}$ of the screen's height).
* Four `QLineEdit`s (text fields) labeled "Label", "Classifier", "Agent" and "Department" (in order) that allow the user to specify an object label, a classifier, an agent name, and a department.
* A `QPushButton` (button) that commands your `lux.py` to communicate with your `luxserver.py`.
Your `lux.py` must communicate with your `luxserver.py` to query the database each time the user clicks on the submit button or types the `Enter` key in any of the text fields.
* A `QListWidget` (list box) whose entries are the results of the query.
  The list box must have vertical and horizontal scroll bars (as needed), and so must be able to scroll vertically and/or horizontally.
* The fields displayed in the list must be&mdash;in order&mdash;the object's label, the object's date, a comma-separated list of all agents that produced the object and the part they produced, and a comma-separated list of the classifiers used for the object.
  * The list box entries must be sorted; the algorithm to sort is the same from pset 1 (except that since the department is not displayed, there is no need to sort by department).
  * The list box must have the appearance of a table, that is, the respective fields of each row must be aligned vertically.
    * There should be no header row of the table displayed. If you like, you may add `QLabel`s displaying the headers above the table, but it is not necessary.
  * There is no need to wrap text for the list box; since the box will be scrollable it is permissible to have each row of the table on one line

> **Note**: The required output for the table in this assignment differs somewhat from the required output for Pset 1.
> In particular, the tabular display in the window for your `lux.py` in this assignment should not display the department name, and all output should be on a single line 

> **Note**: To ensure the fields of your table are aligned, your list box ought to be displayed using a fixed-width font.
> However, we did not and will not discuss `PyQt6` font or typeface specifications in class, so the provided `dialog.py` file provides an instantiated fixed-width `QFont` that you can use, named `FW_FONT`.

Your `lux.py` must allow the user to select a particular list box entry.
If the list box contains any entries, then exactly one of them must be selected at any given time.
If the user clicks on an entry, then your `lux.py` must select that entry.
If the user *double-clicks* on an entry, then your `lux.py` must select that entry and display a dialog box containing detailed data about the class that the selected entry describes.
If the user clicks or double-clicks in the list widget when it contains no entries (or in an unfilled part of the list widget), then your `lux.py` must do nothing.
The detailed data in the dialog must contain the following pieces of information:
* A section with header "Object Information" containng the following pieces of information in a single-row table with the following headers and content:
  * "Accession No.", containing the object's accession number
  * "Label", containing the object's label
  * "Date", containing the object's date
  * "Place", containing the object's place
* A section with header "Produced By", containing a table with details of all agents that produced this object.
    The table must have the following column headers and content:
    * "Part", containing the part of the production carried out by each agent
    * "Name", containing the name of each agent
    * "Nationalities", containing all nationalities of each agent, each on its own line
    * "Timespan", containing the *year* of each agent's `begin_date` and the *year* of each agent's `end_date`, separated by dash or hyphen
        * Some agents are still alive/active; in those cases the Timespan column must contain text such as "1967&ndash;"
        * An agent that has no timespan should have that fact displayed in this column in some reasonable manner
  > **Note**: The table in the "Produced By" section must be sorted in ascending order of agent name, then part, then timespan and finally by nationality.
* A section with header "Classification", containing a comma-separated list of all classifiers for the object, sorted in ascending order of the classifier name
* A section with header "Information", containing a table of all `references` to the object, with two columns: "Type" and "Content" (with the obvious values), sorted first by type and then by content.

The data must be well formatted.
In fact, the requirements for this part are more or less the same as in your `luxdetails.py` program from Pset 1, with three changes:
1. You must display additional properties of the object in the "Object Information" section
2. Tables and lists must be sorted
3. **The maximum width is 150 characters, rather than 100**

It also must be displayed in a fixed-width font, so as to preserve the formatting generated by your table printing software.

> **Note**: There is no easy way to use built-in `Qt` classes to generate a dialog box that displays a message in a fixed-width font; feel free to use the provided `FixedWidthMessageDialog` class in `dialog.py` to accomplish it, or write your own `QDialog` subclass.

Your `lux.py` must be usable *without* a pointing device (mouse, touchpad, etc.). That is, your `lux.py` must be usable with only the keyboard. The user must be able to:
* Cycle the keyboard focus through the text fields and list box by pressing the `Tab` key.
* When the list widget has keyboard focus, indicate a current entry by pressing the `up-arrow` and `down-arrow` keys.
* When the list widget has keyboard focus, **activate** the selected list box entry by typing the `Enter` key, thereby displaying a detail dialog box (as described above).
* **Dismiss** the detail dialog box by typing the `Enter` key.

> **Note**: On Linux and Microsoft Windows systems, programs should be designed such that the user activates the selected list box entry by typing the `Enter` key.
> Remarkably, that's not true on Macs. 
> According to the Mac user interface standards, Mac programs should be designed such that the user activates the selected list box entry by typing `Command-o`.
> (Many popular Mac programs don't conform to that Mac standard.)
>
> Programs that use `PyQt6` and `PySide6` conform to the standards of each platform.
> That is, when running on Linux or Microsoft Windows, they require the user to type the `Enter` key; when running on Macs, they require the user to type `Command-o`.

It is possible to design a better interface than the one just described.
(In fact, you will do so later in the course!)
For now, the layout of your application must be as described.

---

## The `luxserver.py` Program

Your second program must be named `luxserver.py`.

When executed with `-h` as a command-line argument, your `luxserver.py` program must display the following help message that describes the program's behavior:

```
$ python luxserver.py -h
usage: luxserver.py [-h] port

Server for the YUAG application

positional arguments:
  port        the port at which the server should listen

optional arguments:
  -h, --help  show this help message and exit
```

Your `luxserver.py` must accept a single command-line argument.
That argument must be the number of the **port** on which the program will listen for connections.

Your `luxserver.py` must perform queries to the SQLite database.
Your `lux.py` program must **not** access the SQLite database.

Your `luxserver.py` must protect the database against SQL injection attacks.
That is, it must use SQL prepared statements.

> **Note**: Your `luxserver.py` must loop infinitely, as many servers do.
> The issue then becomes...how can you kill your server?
> That is, after creating a process by issuing a `python luxserver.py someport` command, how can you kill that process?
>
> On any Unix-like computer the answer is easy: type `Ctrl-c`. Doing that sends a `SIGINT` signal to the process, which (by default) kills it.
> (Don't type `Ctrl-z`.
> Doing that sends a `SIGTSTP` signal to the process, which does not kill it, but places it in the background.
> The process would continue to occupy the specified port.
> Subsequently issuing a `fg` command would bring the process back to the foreground.)
>
> On a Microsoft Windows computer the answer is harder.
> `Ctrl-c` might work. `Ctrl-Break` might work.
> If your keyboard doesn't have a `Break` key, then consulting the Wikipedia [Break Key](https://en.wikipedia.org/wiki/Break_key) article might help.
> In the worst case you can kill the process via the Windows Task Manager; but that's an awkward last resort.

---

## Communication among tiers

The network connection between your `lux.py` and your `luxserver.py` must not be persistent.
That is, it must *not* be the case that your `lux.py` and your `luxserver.py` create a socket upon startup of `luxserver.py`, transfer data using that one socket during the entire execution of your `lux.py`, and then close that socket upon exit of your `lux.py`.
Instead the network connection must be *transient*.
Each time the user initiates a communication between your `lux.py` and your `luxserver.py`, your `lux.py` and your `luxserver.py` must create a socket, transfer data using that socket, and then close that socket.

### The Justification

The transient approach, although slightly slower than the persistent approach, is more robust in the presence of server failures.
For example, using the transient approach your `luxserver.py` could crash and restart while your `lux.py` is running, with no negative effects upon your `lux.py`.
(The transient approach also mimics HTTP, which we will study soon in class.
In that sense using the transient approach provides a better basis for comparing/contrasting the code that you compose for this assignment with the code that you will compose for subsequent ones.)

## Communication with the Database
Similarly, the connection between your `luxserver.py` and the database must not be persistent.
That is, it must not be the case that your `luxserver.py` creates a database connection upon startup of your `luxserver.py`, uses that database connection during the entire execution of your `luxserver.py`, and then closes that connection upon exit of your `luxserver.py`.
Instead the database connection must be *transient*.
Each time the user initiates a communication between your reg.py and your `luxserver.py`, your `luxserver.py` must create a database connection, transfer data using that connection, and then close that connection.

### The Justification

The transient approach, although slightly slower than the persistent approach, is more robust in the presence of database failures.
For example, using the transient approach the `lux.sqlite` file could disappear, be changed, and reappear while your `luxserver.py` is running, with no negative effects upon your `luxserver.py` or your `lux.py`.

---

## Source Code Guide

Here are the **requirements** for the source code of your solution.

* The `luxserver.py` program must communicate with a SQLite database in a file named `lux.sqlite`, organized as described above.
* The `luxserver.py` program must use SQL prepared statements for every database query.
(This protects the database against SQL injection attacks.)
* Every module used by your program(s) must either be from the Python standard library or written by your team (and included in your submission).
The only exceptions to this are the `PySide6`/`PyQt6` packages for GUI programming and the scaffolding files we have provided you this semester (`dialog.py`, `table.py`).

Here are some **recommendations** for the source code of your solution.

* Reuse code from your solution to Pset 1 in this assignment.
    * The database queries executed by `luxserver.py` will be *almost identical* to the queries executed by your solution to Pset 1.
    * The requirements for the display of the results is exactly the same as Pset 1's `luxdetails.py` for the "object details" dialog box and only slightly modified from Pset 1's `lux.py` for the class list window.
* Modularize `luxserver.py` so that database communication code is cleanly separated from network code.
* Modularize `lux.py` so that GUI code is cleanly separated from network code.
    * Be able to, if needed, change the layout (or the language, or the color scheme...) of the user interface without needing to change anything except code that uses `PySide6` things.
    * Better yet, be able to swap out `PySide6` for *anything else* without needing to change anything except the `PySide6` code.
* Study the [**M**odel-**V**iew-**C**ontroller (MVC)](https://en.wikipedia.org/wiki/Model–view–controller) design pattern and implement it in your solution.

---

## Input Specification

You may assume the users of your `lux.py` and `luxserver.py` programs are generally acting "in good faith", that is, they will not intentionally provide input to your program that is corrupted, unusable, or otherwise incorrect.
In particular, you may assume...
* That the user will only ever provide arguments at the command line that conform to the allowed arguments:
    * The only provided arguments to `lux.py` will be `-h` or a `host`/`port` pair
    * The only provided argument to `luxserver.py` will be a single positional argument or the `-h` flag
* That the database exists in a file named `lux.sqlite` and is well-formed according to the database specification above

However, you may *not* assume...
* That there are any objects at all in the database
* That the `port` argument to either `lux.py` or `luxserver.py` is a numeric argument
* That `luxserver.py` is running on the specified `host`/`port` when you run `lux.py`
* That the user will interact with `reg.py` "slowly".
  That is, your program must handle arbitrarily quick interactions from the user.
  Precisely how you handle these repeated interactions is up to you; we recommend directing `reg.py` to ignore input while a request to the server is in process.
  Whatever you do, though, must prevent your app from crashing under the use of a very fast mouse-clicker (like a robot).

---

## Error Handling

Your `lux.py` and `luxserver.py` should be reasonably robust.
However, since we have only touched on error handling in this course, the kinds of things you are required to handle is limited in this assignment.
Keep in mind that as we progress through the course, error handling will become more important (and the specification of program input more relaxed!).

There are two classes of errors, however, that must be handled by any client-server application, including yours.

### Unavailable Port

Some port numbers are reserved by the operating system for certain processes and cannot be claimed by anyone other than the OS itself.
Other port numbers are in use sometimes, and can't be used by another process.
Still other numbers that allegedly refer to ports are simply too large to be a port number (on most modern systems there are 16 bits for port numbers; that is, valid ports are numbered 0&ndash;65,536).

If `luxserver.py` is given a port number that is not available (for whatever reason), then it must write a descriptive error message to `stderr` and exit with status 1.

### Unavailble Server

If `luxserver.py` is unavailable at the time `lux.py` sends a request, then `lux.py` must display a descriptive error message&mdash;specifically, the message contained in the thrown `Exception` object&mdash;in a `QErrorMessage` and continue executing.

---

## Testing

We’ll cover software testing techniques in lectures later in the semester.
In the meantime, to test your programs it will be sufficient to rely upon (1) your knowledge of testing from your previous experience, and (2) this [A Software Testing Taxonomy](https://yale.instructure.com/assignments/TestingTaxonomy.pdf) document, courtesy of Princeton University.

Test your `lux.py` and `luxserver.py` programs by (1) reviewing this assignment specification thoroughly, making sure that your programs conform to every aspect of it, and (2) comparing the behavior of your program with the example outputs given above.

### Boundary Testing

Focus on boundary (alias corner case) testing.
Of course, make sure that your programs handle normal data.
But also make sure that your programs handle unusual data: objects that have multiple agents, no agents, many classifications, *etc*.

### Statement Testing

Also focus on statement (alias coverage) testing.
Your tests should cause every statement of your `lux.py` and `luxserver.py` to be executed.

You're encouraged, but not required, to use the Python `coverage` tool to generate a coverage report showing which lines of your programs have and have not been executed by your tests. These are the steps:
1. Issue commands of the form `python -m coverage run -p luxserver.py argument` and `python -m coverage run -p lux.py arguments`&mdash;multiple times if necessary.
Interact with the programs to generate coverage reports in files named `.coverageX` (for some program name `X`).
2. Issue the command `python -m coverage combine` to combine the coverage reports generated by step 1 into one large coverage report in a file named `.coverage`.
3. Issue the command `python -m coverage html` to use the `.coverage` file to generate a human-readable report as a set of HTML documents in a directory named `htmlcov`.
4. Browse to `htmlcov/index.html` to check the report.

### Unit Testing

The kind of testing described above, in which the entire program is repeatedly run and the output compared to correct output, is called **system testing**.
You probably will notice that testing your `lux.py` program as a whole is quite tedious.
If you have sufficiently modularized your code, unit testing can help dramatically with all of the non-GUI parts of testing `lux.py` because it can test *individual functions*, including those that don't necessarily do anything to the GUI.
Testing the GUI parts of your program will remain tedious, but you can at least sleep a little more soundly knowing that your GUI is resting on a solid foundation.

> **Note**: Incidentally, if you're interested, the [pytestqt](https://pypi.org/project/pytest-qt/) package can help automate GUI testing.
> You are not required to automate any testing, much less GUI testing, but the tools exist and we encourage you to check them out.

Unit testing will be covered briefly later in the semester; for now, it is sufficient to read a blog post or two and study briefly the documentation for the Python `unittest` or `pytest` modules.

---

## Program Style

As with Pset 1, your solution to this assignment must be well-styled.
This includes not only good style as defined by the `pylint` static analysis tool, but also that your code conforms to "good" software project design principles such as modularity, abstraction, and an eye toward reusability.

As you self-evaluate program style, consider the following things:
* How much of your solution for Pset 1 was reusable in this assignment?
What changes could you make so that it is more reusable for the rest of the assignments, in which you will change the presentation tier and add sophistication to the application tier?
* If a specific protocol was required to be "spoken" by `luxserver.py`, how much effort would it take to modify your program to conform to that protocol?
  * For example, a common protocol for communication over the Internet is the [**H**yper**t**ext **T**ransfer **P**rotocol (HTTP)](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol).
  We'll talk about it in detail over the coming weeks, but you should aim to minimize the changes to `luxserver.py` that are needed to conform to it, for example, by encapsulating the creation of a server response inside of a function whose body can be swapped with an HTTP-conforming response creator.
* If the client of `luxserver.py` were not capable of unpickling your objects, how much effort would it take to change your server program to support that client?
* If a new Python GUI framework came into the picture that you liked better than `PySide6`, how much effort would it take to change your `lux.py` program to use the new framework?

---

## Advice

As noted above, your `lux.py` must handle communication with the human user, and your `luxserver.py` must handle communication with the database.
Beyond those obvious requirements, it's up to you to decide how to divide tasks between your `lux.py` and your `luxserver.py`.

It's also up to you to design the communication protocol between the two programs (other than that it must be over a network).
The protocol could be a "low-level" one involving transmitting lines of text.
Or it could be a "high-level" one involving transmitting `pickle`d Python objects.
Or it could be a "medium-level" one involving transmitting JSON or XML.
Any of those approaches is acceptable, but you probably will find the "high-level" approach easiest to implement.
That said, you should keep in mind that you will be writing non-Python clients in future assignments.

> **Note**: You *might* need to make some small modification to `table.py` if you intend to use object pickling (the "high-level" protocol).
> This is because objects of type `sqlite3.Row` are not `pickle`-able!
> You can handle this in one of two ways: convert your data to `pickle`-able objects *before* handing it to the `Table` class, or modify the `Table` class to convert the data to `pickle`-able objects such as `list`s upon initialization.
> Either is acceptable for this assignment, and you should decide which makes the most sense to you.

While it is not required that your progam(s) handle every possible error, if you would like to explore that aspect of software engineering, you could design your `luxserver.py` such that, after receiving a request from your `lux.py` client, it sends two things back to your `lux.py` client:
* The first is an indication of whether the processing of the request succeeded or failed (or, better, an indication of *why* it failed, if indeed it did).
* If the processing succeeded, then the second thing contains the requested data.
* If the processing failed, then the second thing is a string which is an error message, or a pickled `Exception` object containing a string which is an error message.

Design your `lux.py` such that if the user double clicks in the list box, or if the user types the `Enter` key (or, on a Mac, `command-o`) while the list box has keyboard focus, then the program:
* **Detects the event**. Then in the list box event handler...
* **Sends messages** to (*i.e.*, calls functions of) the list box to determine which list box entry was selected and the text that it contains.
* **Analyzes that text** to determine the object ID.
* **Sends a request** to the server to get the data for that object ID
* **Displays a dialog** box based upon that server response.

If you are having trouble wrapping your head around GUI programming, recognize that the most important part of this assignment is the communication between tiers.
Start with a command-line client that sends a request to the server and displays a table (perhaps this is done by refactoring `lux.py` from Pset 1 to communicate with a server rather than the database directly, or if you chose the "low-level" protocol it may be simply running `telnet`).
Only once you have a reliable communication mechanism should you start the GUI side of things.

---

## Submission

Replace the provided `README.md` file (which contains this assignment specification) with your own `README.md` file that conforms to the following requirements.

1. Leave the first line of the file alone (it is the assignment title).

2. Thereafter your `README.md` file must contain:
    * Your name and Yale netid and your teammate’s name and Yale netid (if you worked with a partner)
    * A paragraph describing your contribution, and another paragraph describing your teammate’s contribution.
    Please be thorough; we are looking for two substantial paragraphs, not a sentence or two.
    * A description of whatever help (if any) you received from other people while doing the assignment.
    * A description of the sources of information that you used while doing the assignment, that are not direct help from other people.
    * An indication of how much time you spent doing the assignment, rounded to the nearest hour.
    * Your assessment of the assignment:
        * Did it help you to learn?
        * What did it help you to learn?
        * Do you have any suggestions for improvement? *Etc.*
    * (Optionally) Any information that will help us to grade your work in the most favorable light.
    In particular, describe all known bugs and explain why any `pylint` style warnings you received are unavoidable or why you know better than `pylint` (a convincing argument might negate some `pylint` style penalties you may accrue).

Your `README.md` file must be a plain text file.
**Do not** create your `README.md` file using Microsoft Word or any other word processor, although it may be formatted using [markdown](https://www.markdownguide.org/), like this provided `README.md` file.

Package your assignment files by [creating a release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) on GitHub in your assignment repository. There must be at least three files with the following (exact) names in that repository when you submit it:
* `README.md`
* `lux.py`
* `luxserver.py`

Ensure that any additional files needed by your program (such as other Python modules) are in the repository snapshot (i.e., commit) captured by the release.

> **Note**: If you have installed external packages, you must also include a file named `requirements.txt` containing the dependencies of your project.
> It can be created from your virtual environment by running the following command:
> ```
> $ pip freeze -r requirements.txt
> ```
> 
> Failure to include a `requirements.txt` file if you use third-party packages will result in an automatic 5% penalty and a request that you submit an appropriate `requirements.txt` file to the graders.

Submit your solution to Canvas (in the assignment named "Desktop Version A") as [a link to that release](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases).

As noted above in the [Rules](#rules) section, it must be the case that either you submit all of your team’s files or your teammate submits all of your team’s files.
(It must not be the case that you submit some of your team’s files and your teammate submits some of your team’s files.)
You and your team may submit multiple times; we will grade the latest files that you submit before the deadline unless a particular version is requested as the canonical version.

**Please follow the directions on what to submit and how.**
It will be a big help to us if you get the filenames right and submit exactly what’s asked for.
Thanks.

### Late Submissions

The deadline for this assignment is **11:59 PM NHT (New Haven Time) on Friday March 10, 2022**.
There is a strict 30 minute grace period beyond the deadline, to be used in case of technical or administrative difficulties, and not for putting final touches on your solution.

Late submissions will receive a 5% deduction for every 12-hour period (or part thereof) after the deadline.
After 72 hours, the Canvas assignment will close and submissions after that time will not receive any credit.

---

## Grading

Your grade will be based upon:
* **Correctness**, that is, the correctness of your programs as specified by this document.
* **Style**, that is, the quality of your program style.
This includes not only style as qualitatively assessed by the graders (including modularity, cleanliness, and algorithmic efficiency) but also style as reported by the `pylint` tool, using the default settings, and when executed via the command `python -m pylint **/*.py`.

Ten percent of your grade will be based upon the quality of your program style as reported by `pylint`.
Your grader will start with the 10-point score reported by pylint.
Your *pylint style grade* is your pylint score rounded to the nearest integer (minimum 0).
For example, if your pylint score is 9.8, then your *pylint style grade* will be 10; if your pylint score is 7.4, then your *pylint style grade* will be 7.

If your code fails the tests on some particular functionality, your grader will inspect your code manually to try to assign partial credit for that functionality.
Partial credit will be given only if there is an *obvious* "quick fix" (*e.g.*, you have accidentally changed the name of the database file and your solution points to a file with a name that does not match the grader's copy of the database); if no such quick fix exists then no partial credit for that feature will be given.

---

Original copyright &copy;2021 by Robert M. Dondero, Jr.

Modified &copy;2023 by Alan Weide

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
