![Code Quality Score](https://www.code-inspector.com/project/24631/score/svg)
[![Code Grade](https://www.code-inspector.com/project/24631/status/svg)](https://frontend.code-inspector.com/project/24631/preferences)

# whatsapp-message-scheduler-cli
 This is the final project in the completion of the Skaehub Bootcamp
 
# 1.problem 
Build a CLI app to schedule whatsapp messages and send them automatically once the scheduled time has passed. For example, your app should prompt the user to write a message, their whatsapp number, the recipient’s number and the time they intend to have it sent out. You can save this data on an SQLite Database.

# 2.general purpose
The general purpose of the application is to enable the user to be able to schedule meessages at ease incase they are not able to do it at that specific time.The application allows the user to enter recepient number and message to be sent at that specific scheduled time

# 3.How it works
The program utilises Twilio API for Whatsaapp to only send messages and Python 's in-built libraries like datetime and time to schedule the messages.

# 4.Installation and setup
1.Clone this repository into your local machine

2.Create a virtualenv into your machine and activate it.

3.cd into the folder of the clone of the repository.

4.install the packages and dependancies using pip: pip install -r requirements.txt

5.run the app using python3 App/inputs/main.py

# 5.Testing
This application was tested by unittest.and done a coverage done on the tests.<br>
1.To install unittest:pip install unittest2<br>

2.To install coverage:pip install coverage<br>

1.To run the test:using unittest-python -m unittest whatsapp_schedule_test.py<br>

2.o run the test:using coverage-coverage run -m unittest whatsap_schedule_test.py<br>

# Credits
1.Namsi Lydia.<br>
2.Skaehub Community.<br>
