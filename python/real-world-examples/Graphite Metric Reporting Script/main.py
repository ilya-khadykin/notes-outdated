import urllib.request
import json
from time import sleep
from datetime import datetime
from pytz import timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

######################################
# Graphite Metric Reporting Script
#
# The script uses Graphite Render API to get metrics for the last minute, compares it with the value
# which was captured an hour ago, computes the change rate and sends email reports every hour
# using specified Gmail credentials
######################################


GMAIL_USERNAME = 'example@gmail.com'
GMAIL_PASSWORD = ''
FROM_EMAIL = ''  # email-sender
TO_EMAIL = ''  # email-recipient
EMAIL_SUBJECT = ''  # subject for your email alert, name of the metric for example
time = ''  # a global variable that will contain the time of the metric


# helper functions
def convert_timestamp(str_timestamp):
    """Convert string timestamp to a common format

    Converts given string which represents timestamp to the following format '2015-10-27 19:45'

    Args:
        str_timestamp (str): timestamp to convert as a sting

    Returns:
        a string representing the date and time in format '2015-10-27 19:46'
    """
    return datetime.fromtimestamp(str_timestamp).strftime('%Y-%m-%d %H:%M')


def convert_timestamp_in_EDT(timestamp):
    """Convert given timestamp in EDT\EST timezone

    Args:
        timestamp (str): POSIX timestamp

    Returns:
        a string representing the date and time in format '2015-10-27 19:46 EDT'
    """
    fmt = "%Y-%m-%d %H:%M %Z"
    tz = timezone('US/Eastern')  # you can the code here to convert the time to your timezone
    return datetime.fromtimestamp(timestamp, tz).strftime(fmt)


def send_email_alert_with_gmail(from_addr, to_addr, username, password, email_subject, message):
    """Send an email using Gmail and SMTP protocol

    Sends an email with your 'message' passed as a paramentr

    Args:
         from_addr (str): email-sender
         to_addr (str): email-recipient
         username (str): Gmail username
         password (str): password for Gmail account
         email_subject (str): subject of an email message
         message (str): message included in a body of an email

    Returns:
         -1 if an error was encountered
    """
    server = smtplib.SMTP('smtp.gmail.com:587')  # Gmail
    # Sending an email alert
    try:
        # forming the content of the email alert
        content = MIMEMultipart()
        content['From'] = from_addr
        content['To'] = to_addr
        content['Subject'] = email_subject + ' | ' + convert_timestamp_in_EDT(time)  # time of the metric
        content.attach(MIMEText(message, 'plain'))  # email body
        
        server.starttls()
        server.login(username, password)
        server.send_message(content,from_addr,to_addr)
    except Exception as e:
        print(e)
        return -1
    finally:
        server.quit()


def get_graphite_metric(url, index=0):
    """Request the Metric from Graphite instance

    Args:
        url (str): url to Graphite Render JSON API for GET request in order to receive JSON object as response
        index (int): index of the metric in a list of metrics

    Returns:
        int: metric value as an integer number
    """
    global time
    try:
        response = urllib.request.urlopen(url).read().decode('utf-8')
        response_json = json.loads(response)  # converting response text to JSON object
        time = response_json[0]['datapoints'][index][1]
        return int(response_json[0]['datapoints'][index][0])
    except Exception as e:
        print(e)


def generate_report(report_heading, links_to_metrics, metrics_values, change_rate_values ):
    """Generate report for list of metrics to be sent as an email message

    Args:
        report_heading (str): the heading of the report
        links_to_metrics (list): links to Graphite Render API for requesting metric`s values
        metrics_values (list): values of the monitored metrics
        change_rate_values (list): computed change rate for the respective metric

    Returns:
        str: formatted report to print or send in an email alert
    """
    report = report_heading + '\n  for the last hour: \n'
    report += convert_timestamp_in_EDT(time) + '\n'
    report += '--------------------\n'

    for i in range(len(links_to_metrics)):
        report += 'Metric: ' + str(links_to_metrics[i]) + '\n' + str(metrics_values[i]) + ' ' \
                  + str(change_rate_values[i]) + '\n'

    return report


def main():
    """Main function of the script
    """

    # the purpose of the lists below is to hold current and 'one hour behind' metrics
    # and the result of computing changing rate for respective metric
    # index is the key identifier of the metric
    current_metric = []
    previous_metric = []
    change_rate = []

    # links to Graphite Render API url for GET Request which returns Metrics as JSON object

    links = ['LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-2min&utill=now&format=json']

    # links to the metrics which are one hour behind for comparison purposes and computing the change rate
    one_hour_behind_links = [
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json',
             'LINK_TO_YOUR_GRAPHITE_INSTANCE/render?target=alias(statsd.fakesite.counters.session_start.desktop.count, "memory")&from=-1h&utill=now&format=json']

    # error check
    if len(links) != len(one_hour_behind_links):
        print("links to Graphite Render API for current and 'one hour behind' metrics should coincide "
              + "otherwise it's impossible to compute change rate")
        return -1

    # the length of the lists below should coincide with length of monitored metrics
    # initializing them
    for i in range(len(links)):
        current_metric.append(0)
        previous_metric.append(0)
        change_rate.append('')

    i = 0
    while True:
        if get_graphite_metric(one_hour_behind_links[i]) == -1:
            i = 0
            continue
        else:
            previous_metric[i] = get_graphite_metric(one_hour_behind_links[i])
            i += 1
        if i == 6:
            i = 0
            break

    i = 0
    change_rate_num = 0
    while True:
        if get_graphite_metric(links[i]) == -1:
            # try again
            i = 0
            continue
        else:
            current_metric[i] = get_graphite_metric(links[i])
            change_rate_num = 100 - round((previous_metric[i]/current_metric[i]*100))
            # fancy formatting
            if change_rate_num >=0:
                change_rate[i] = '+' + str(change_rate_num) + '%'
            else:
                change_rate[i] = str(change_rate_num) + '%'
            i += 1
            # resetting index counter
            if i == 6:
                i = 0
                # update previous values
                for k in range(6):
                    previous_metric[k] = current_metric[k]
                report = generate_report(EMAIL_SUBJECT, links, current_metric, change_rate)
                send_email_alert_with_gmail(FROM_EMAIL, TO_EMAIL, GMAIL_USERNAME, GMAIL_PASSWORD, EMAIL_SUBJECT, report)
                print(report)
                sleep(3600)  # delay for the next check == 60 min


if __name__ == '__main__':
    main()