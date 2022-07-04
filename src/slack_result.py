#!/usr/bin/env python3
import argparse

import slackweb


def notify():
    footer_text = None
    parser = argparse.ArgumentParser(description='slack notification script')

    parser.add_argument('--webhook-url', help='incoming webhook url')
    parser.add_argument('--verdict', help='pass or fail', default='fail')
    parser.add_argument('--commit', help='commit of the build')
    parser.add_argument('--device', help='device version')
    parser.add_argument('--version', help='build version', default="n/a")
    parser.add_argument('--environment', help='build version', default="n/a")
    parser.add_argument('--report-link', help='report link')
    parser.add_argument('--screenshot-link', help='screenshot link')
    parser.add_argument('--build-link', help='build download link')
    parser.add_argument('--summary', help='summary')
    parser.add_argument('--timestamp', help='timestamp')
    parser.add_argument('--os-version', help='os version')
    parser.add_argument('--build-logs-link', help='build logs link')
    parser.add_argument('--jenkins-job-link', help='jenkins job link')
    parser.add_argument('--jenkins-job-number', help='jenkins job number')
    parser.add_argument('--additional-info', help='any other additional information will display at footer')

    args = parser.parse_args()

    attachment_fields = []

    if args.device is not None:
        attachment_fields.append({"title": "device", "value": "`{}`".format(args.device), "short": True})

    if args.environment is not None:
        attachment_fields.append({"title": "environment", "value": "`{}`".format(args.environment), "short": True})

    if args.os_version is not None:
        attachment_fields.append({"title": "os version", "value": "`{}`".format(args.os_version), "short": True})

    if args.commit is not None:
        attachment_fields.append({"title": "commit", "value": "`{}`".format(args.commit), "short": True})

    if args.version is not None:
        attachment_fields.append({"title": "version", "value": "`{}`".format(args.version), "short": True})

    if args.jenkins_job_number is not None:
        attachment_fields.append({"title": "jenkins job number", "value": "`{}`".format(args.jenkins_job_number), "short": True})

    if args.build_link is not None:
        attachment_fields.append(
            {"title": "build", "value": "(<{} | download>)".format(args.build_link), "short": True})

    if args.report_link is not None:
        attachment_fields.append(
            {"title": "html report", "value": "(<{} | open>)".format(args.report_link), "short": True})

    if args.build_logs_link is not None:
        attachment_fields.append(
            {"title": "build logs", "value": "(<{} | open>)".format(args.build_logs_link), "short": True})

    if args.jenkins_job_link is not None:
        attachment_fields.append(
            {"title": "jenkins job", "value": "(<{} | open>)".format(args.jenkins_job_link), "short": True})

    if args.screenshot_link is not None:
        attachment_fields.append(
            {"title": "screenshots", "value": "(<{} | download>)".format(args.screenshot_link), "short": True})

    if args.summary is not None:
        attachment_fields.append({"title": "summary", "value": args.summary, "short": False})

    if args.additional_info is not None:
        footer_text = args.additional_info + "\n"

    if args.timestamp is not None:
        if footer_text is None:
            footer_text = ""
        footer_text = footer_text + "Tests started at: " + args.timestamp

    slack = slackweb.Slack(url=args.webhook_url)
    attachments = [{"color": "good" if args.verdict == "pass" else "warning",
                    "fields": attachment_fields,
                    "footer": footer_text, }]
    slack.notify(attachments=attachments)


if __name__ == '__main__':
    notify()
