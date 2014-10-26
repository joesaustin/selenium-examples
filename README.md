selenium-examples
=================

These are basic selenium examples done in python.
The NYT folder contains a simple test that clicks on all the sections of the site and asserts that the subscribe now button appears on each page.
The birth-day-test folder contains a script that is a little more advance and test that the birthday calculator on calculator.net actually displays the correct age is given based on the date of birth entered.

Dependencies
------------

1) Install selenium
    $ pip install selenium

2) Download [selenium rc](http://docs.seleniumhq.org/download/) 

3) Download [chromedriver](http://chromedriver.storage.googleapis.com/index.html)

4) Start the selenium hub
    $ java -jar selenium-server-standalone-verson.jar -role hub