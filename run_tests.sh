#!/bin/bash

cd Selenium/code

# pytest test_pyorg.py --browser=chrome --url=https://www.python.org/

pytest test_login.py --browser=chrome --url=https://education.vk.company/
