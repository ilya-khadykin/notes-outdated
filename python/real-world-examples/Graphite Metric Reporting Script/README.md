# Graphite Metric Reporting Script
This is a monitoring script I used at work, I changed it a bit to make it more universal

[Graphite] is a powerful set of tools for collecting, storing and graphing operations data (or any kind of time-series data). It has a very good [URL API] which makes it even more handy to use. It's heavily used in the industry nowadays for monitoring.

The script uses [Graphite Render API] to get metrics for the last minute, compares it with the value winch was captured an hour ago, computes the change rate and sends email reports every hour using specified Gmail credentials. It's pretty basic, but it was useful when we closely monitored one of our key metrics

The script utilizes the code of the following modules:
* `urllib` to send HTTP requests to Graphite
* `json` to work with JSON
* `time.sleep(seconds)` to delay execution for a number of seconds
* `datetime` to work with date and time
* `pytz` to be able to change timezones
* `smtplib` to send emails via SMTP
* `email.mime` to be able to use MIME types 

[graphite]: <http://graphite.wikidot.com/start>
[URL API]: <http://graphite.wikidot.com/url-api-reference>
[Graphite Render API]: <http://graphite.readthedocs.org/en/latest/render_api.html>