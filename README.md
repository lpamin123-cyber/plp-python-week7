# Week 7 Assignment: Shopping List Manager

## Overview
This repository contains Python programs developed for the PLP Python Week 7 assignment, covering basic list operations, interactive input management, and procedural data analysis.

## Files Description
* `list_warmup.py`: Demonstrates basic list operations including index access, `.append()`, `.remove()`, and `len()`.
* `shopping_list.py`: An interactive CLI tool to manage a shopping list supporting addition, safe removal, and display functions.
* `list_report.py`: Analyzes a list of items to format a numbered output, count items based on string length, and identify the longest item name using a comparative loop.
* `screenshots/`: Contains execution output screenshots for each script.

## Safety Reflection: Checking Membership with `in`
It is safer to check `if item in list:` before calling `.remove()` because calling `.remove()` on an item that does not exist raises a `ValueError` in Python, which crashes the program. Checking membership beforehand guarantees safe handling of missing items and prevents execution errors, ensuring a smooth user experience.
