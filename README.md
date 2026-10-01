# Week 7 Assignment: Shopping List Manager

## Overview
This repository contains Python scripts demonstrating list management, conditional validation, and summary reporting.

## Files Description
- `list_warmup.py`: Demonstrates basic list operations such as indexing, `.append()`, and `.remove()`.
- `shopping_list.py`: An interactive console application allowing users to view, add, and remove items dynamically.
- `list_report.py`: Generates a smart report calculating total items, total price, and average price per item.
- `screenshots/`: Folder containing output screenshots of each script executing.

## Why check `in` before calling `.remove()`?
Checking for membership using the `in` keyword before invoking `.remove()` is essential to prevent runtime errors. Calling `.remove()` on an item that does not exist in a list raises a `ValueError` and causes the program to crash. Verifying membership first allows the script to handle missing items gracefully without crashing.
