# UTAttendance

A simple python app for calculating the sum of the presence of a user in Adobe Connect Sessions.

## Input File

The input is a CSV file with three columns that are student number, start date, and end date.

Example:

```csv
 login, date-created, date-end
810199001,30/05/2021 0:34:53,30/05/2021 0:35:00
810199002,30/05/2021 0:30:15,30/05/2021 0:35:00
810199003,30/05/2021 0:27:28,30/05/2021 0:28:32
810199004,30/05/2021 0:23:41,30/05/2021 0:34:44
810199005,30/05/2021 0:22:40,30/05/2021 0:22:58
```

## Usage

Run these commands in terminal:

```bash
git clone https://github.com/daniyalmarofi/utattendance.git
pip3 install pandas
cd utattendance
python3
```

And then in python shell:

```python
from UTAttendance import *
database = UTAttendance('input_data.csv').save_results('output.csv')
```

Or simply edit and run `main.py` file.

## Issues

In case of any issues, [Create an issue](https://github.com/daniyalmarofi/utattendance/issues/new/choose)

## About

Code by [Daniyal Marofi](https://github.com/daniyalmarofi)
