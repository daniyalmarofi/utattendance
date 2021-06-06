'''
A simple python app for calculating
the sum of the presence of a user in
Adobe Connect Sessions.
Jun 6, 2021
Daniyal Marofi
'''

from UTAttendance import *


database = UTAttendance('data.csv').save_results()

