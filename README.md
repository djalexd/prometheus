Code, configuration and usage of Raspberry-powered car Prometheus


Running the unit tests
----------------------
__Pythonic way__ (requires Python 2.7+):
  `python -m unittest discover test -v -p 'test*.py'`

Extract plot data from logs
---------------------------

  `cat example.log | grep angle | `cut -d ' ' -f5 > t.csv` `
  `cat t.csv | sed 's/[,]/ /' | sed 's/[(]/ /' | sed 's/[)]/ /' | sed 's/[\W]//' > t2.csv`
