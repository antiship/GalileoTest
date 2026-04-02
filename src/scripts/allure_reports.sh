#!/bin/bash

if [[ ! -d ~/Allure/bin/ ]]; then
  # shellcheck disable=SC2242
  exit "You should install Allure locally first."
fi

~/Allure/bin/allure.bat open ../allure_/allure_reports/
