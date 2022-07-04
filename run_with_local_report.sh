rm -rf src/tests/allure_raw
cd src/tests

echo "Starting smoke"
#python - m pytest --alluredir=allure_raw test_smoke.py
pytest --alluredir=allure_raw test_smoke.py

echo "Finish smoke"
echo "Open report"
#cd ..
deactivate
allure serve allure_raw