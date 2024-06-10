# Working with Google Spreadsheets

## Overview

This module provides an introduction to working with Google Spreadsheets in Python. It covers how to use the `gspread` library to read from and write to Google Sheets.

## Learning Objectives

-   Understand how to set up and use the `gspread` library.
-   Learn how to authenticate with the Google Sheets API.
-   Learn how to read from and write to Google Sheets.

## Key Concepts

-   **Google Sheets API**: An interface that allows you to interact with Google Sheets programmatically.
-   **gspread**: A Python library for interacting with Google Sheets.

## Prerequisites

-   A Google account
-   A Google Cloud project with the Google Sheets API enabled
-   A service account and its JSON key file

## Code Examples

### Setting Up

The following script demonstrates how to set up the `gspread` library and authenticate with the Google Sheets API.

#### `setup_gspread.py`

This script covers:

-   Installing the `gspread` and `oauth2client` libraries
-   Authenticating with Google Sheets API

### Reading from Google Sheets

The following script demonstrates how to read data from a Google Sheet.

#### `reading_google_sheets.py`

This script covers:

-   Opening a Google Sheet by its title
-   Reading data from the sheet

### Writing to Google Sheets

The following script demonstrates how to write data to a Google Sheet.

#### `writing_google_sheets.py`

This script covers:

-   Writing data to specific cells
-   Adding rows of data to the sheet

## Running the Examples

To run the examples, navigate to this directory in your terminal and execute the following commands:

```
python setup_gspread.py
```

```
python reading_google_sheets.py
```

```
python writing_google_sheets.py
```
