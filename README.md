# Data Analytics Bootcamp Homework Assignment

## Table of Contents
1. [Project Overview](#project-overview)
2. [Scope and Objectives](#scope-and-objectives)
   - [Part 1: Financial Analysis](#part-1-financial-analysis)
   - [Part 2: Election Results Analysis](#part-2-election-results-analysis)
3. [Tools and Technologies](#tools-and-technologies)
4. [Data Sources](#data-sources)
5. [Results and Conclusions](#results-and-conclusions)
   - [Financial Analysis Summary](#financial-analysis-summary)
   - [Election Results Summary](#election-results-summary)
6. [How to Use](#how-to-use)
7. [Acknowledgments](#acknowledgments)

---

## Project Overview

This project consists of two main analytical tasks:
1. A financial data analysis of company profit/losses over time.
2. An election data analysis to determine vote counts and identify the winning candidate.

These tasks demonstrate the ability to extract insights from datasets using Python scripting.

---

## Scope and Objectives

### Part 1: Financial Analysis
The goal of this analysis is to parse a dataset of company profits and losses to:
- Calculate the total number of months included in the dataset.
- Compute the net total amount of "Profit/Losses" over the dataset period.
- Determine the average change in "Profit/Losses" over the dataset period.
- Identify the greatest increase and decrease in profits (date and amount).

### Part 2: Election Results Analysis
The objective of this analysis is to analyze a dataset of election results to:
- Count the total number of votes cast.
- Identify all the candidates who received votes.
- Calculate the percentage of votes each candidate won.
- Determine the total number of votes each candidate received.
- Identify the winner of the election based on the popular vote.

---

## Tools and Technologies

This project utilizes the following tools:
- **Python**: Core programming language used for analysis.
- **CSV Module**: To read and process the data files.
- **OS Module**: For handling file paths and directories.
- **Text Files**: To save and present the results.

---

## Data Sources

- **Financial Data**: `budget_data.csv`
- **Election Data**: `election_data.csv`

---

## Results and Conclusions

### Financial Analysis Summary
- **Total Months Analyzed**: 86
- **Net Total Profit/Loss**: 22564198
- **Average Change in Profit/Loss**: $-8311.105882
- **Greatest Increase in Profits**: Aug-16 ($1862002)
- **Greatest Decrease in Profits**: Feb-14 ($-1825558)

### Election Results Summary
- **Total Votes Cast**: 369711
- **Candidate Vote Shares**:
  - Charles Casper Stockham: 23.0% (85213)
  - Diana DeGette: 73.8% (272892)
  - Raymon Anthony Doane: 3.1% (11606)
- **Winner**: Diana DeGette

---

## How to Use

1. Place the input CSV files (`budget_data.csv` and `election_data.csv`) in the `Resources` directory.
2. Run the Python scripts:
   - `main.py` (financial analysis)
   - `main.py` (election analysis)
3. Output files with the analysis results will be generated in the `analysis` directory.

---

## Acknowledgments

This project was completed as part of the Data Analytics Bootcamp curriculum. Special thanks to the instructors and peers for their guidance and support.