#!/bin/sh
ALLURE_RESULTS="tests/allure_raw"
ALLURE_REPORT="allure_report"
SLACK_PY_FILE="./slack_result.py"
BASH_FILE_NAME=`basename "$0"`


# reporting related
# debug channel
webhook_url="https://hooks.slack.com/services/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"
aws_bucket="siz-tests-api-gw"
version="N/A"
platform="N/A"
timestamp=$(date +'%Y.%m.%d-%H.%M')
send_report=true

if [ -f ~/.bash_profile ]; then
   source ~/.bash_profile
fi


usage()
{
    echo "e.g. ./$BASH_FILE_NAME "
    echo "e.g. ./$BASH_FILE_NAME --tags @lol"
    echo "e.g. ./$BASH_FILE_NAME --version 7.4.0.5178 --platform android"
}


# send report if user specify so
if [ "$send_report" == true ]; then


    allure generate --clean ${ALLURE_RESULTS} -o ${ALLURE_REPORT}

    #parse test result summary
    SUMMARY_JSON="${ALLURE_REPORT}/widgets/summary.json"
    TOTAL_TC=`cat "${SUMMARY_JSON}" | jq '.statistic.total'`
    PASS_TC=`cat "${SUMMARY_JSON}" | jq '.statistic.passed'`
    summary_text="${PASS_TC} tests passed (total ${TOTAL_TC}) test cases"
    echo $summary_text

    verdict='false'

    if [[ $PASS_TC == $TOTAL_TC ]]; then
        verdict='pass'
    fi

    # push report to aws
    target_aws_dir="s3://${aws_bucket}/test-reports/android-app/$version/$timestamp/"
    export AWS_ACCESS_KEY_ID=AKIAYTSTEVU36E5LJHPZ
    export AWS_SECRET_ACCESS_KEY=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
    export AWS_DEFAULT_REGION=eu-central-1

    aws s3 sync $ALLURE_REPORT "$target_aws_dir"


    echo "----------------------------------------"
    echo "sending results via slack"
    echo "----------------------------------------"
    aws_report_link="http://${aws_bucket}.s3-website.eu-central-1.amazonaws.com/test-reports/android-app/$version/$timestamp/index.html"
    chmod 700 ${SLACK_PY_FILE}
    ${SLACK_PY_FILE}  --webhook-url $webhook_url \
                    --version "1.0" \
                    --verdict $verdict \
                    --summary "${summary_text}" \
                    --device "Android Emulator" \
                    --timestamp "$timestamp" \
                    --report-link "${aws_report_link}"
fi