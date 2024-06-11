# Visualizing Test Data
Code that analyzes multiple choice pre/post test data and produces data visualizations to better show trends in student learning.

## Purpose of the Program
Effectiveness of instruction is often measured through a multiple choice assessment given before and after the completion of the course: “pre” and “post” tests. Growth or lack thereof is commonly quantified using a normalized gain metric, (post-pre)/(100-pre), which gives an overview of students’ learning but does not provide insights on how answers to specific questions changed. 

Our goal in introducing the transition analysis metrics is to extract more information about student learning trends, including how students interact with specific questions, what ideas students come to the course with and how they change, and identifying where and in what ways students get confused.

## Transition Analysis Metrics

<img width="655" alt="transanalysismetrics" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/b31b7c21-676f-4f51-84fc-6f3dcf4809a6">

Then metrics are created according to the frequency of these transitions:

<img width="678" alt="Screenshot 2024-06-11 at 2 11 06 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/03f7e156-c8a1-4327-b349-8aa83c1a62df">

## Running the Program

If python is downloaded on the user’s computer, the program script (Visualizing_Test_Data.py) can run in the terminal by using command cd to navigate to the working directory then command python3 to run the script.
cd path/to/folder_containing_script
python3 Visualizing_Test_Data.py
The script can also be run through an integrated development environment such as IDLE, or Visual Studio, or through a Jupyter Notebook.
**Note: File names in script should be changed before running.

### Packages Needed

The program only requires 3 basic packages: pandas, matplotlib, and seaborn, which will need to be installed before code can be run. Generally these packages can be installed through the command prompt using the command:
pip install matplotlib

## Uploading Test Files
### Formatting Files
In order for the program to work properly, test files (pre and post tests) need to be formatted according to the picture below and saved as a csv file.

<img width="625" alt="Screenshot 2024-06-11 at 2 15 40 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/445d272c-097f-42d7-8f75-daf0b48831e7">

With a unique identifier (can also be a number or combination of numbers and letters) under an ‘ID’ column and each student answer under a ‘Q1’, ‘Q2’,.... column. Ensure that columns are capitalized. The program will still run if some cells are left blank (if students do not answer).
Answer keys should be formatted according to the picture below and saved as a csv file.

<img width="578" alt="Screenshot 2024-06-11 at 2 16 35 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/79c778e5-b86d-4ded-aa61-5ca9c691cf09">

### Inserting File Paths
This section of code at the top of the script (shown below) is where file paths and test specifications must be added before the program can run.

<img width="1037" alt="Screenshot 2024-06-11 at 2 18 40 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/aed18a07-ffca-418d-be0b-2acbeb94e72b">

Data from multiple classes and years can be entered as long as the pre/post test given is the same. In the example shown, two classes are entered, General Physics 2015 and Intro Physics 2016, each with their own csv containing student answers.

As shown below, ensure that file paths and data specifications (class name and year) are entered as strings, separated by commas, in the correct order. If two filepaths are from the same year or class, enter the specification twice. i.e. General Physics 2015 and General Physics 2016 would be entered as class_set=[‘General Physics’, ‘General Physics’] and year_set=[‘2015’ , ’2016’].

<img width="1170" alt="Screenshot 2024-06-11 at 2 20 10 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/805fa5d2-6428-4275-ac67-9249b0dd417d">

There should not be a limit on how many class datasets can be entered, but runtime will increase as the number of files to analyze increases.

The last things to input in this section is the answer key file path, as a string, the number of questions in the pre/post test (num_questions), and the question number to be considered (question_num) in the question-specific outputs, answer tables and transition plots).

## Overview of Each Data Visualization
### Answers Table
The answers table, displayed as a program output, is designed  to give the user an idea of the most popular answer choices on the pre and post tests. Answers are listed in order of decreasing popularity and includes the number and percentage of students who gave the answer. Answers are only displayed for one question, which the user changes at the top of the script.

<img width="300" alt="Screenshot 2024-06-11 at 2 22 02 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/78654acc-6b28-4b8e-bb46-7945bcb9f99d">

### Transition Plots
The transition plot, displayed in a pop up window, is designed to give the user an idea of the most common answer transitions. More frequent answer transitions appear as darker lines. Answers are only displayed for one question, which the user changes at the top of the script.

<img width="725" alt="Screenshot 2024-06-11 at 2 23 41 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/92ed4b58-458d-4035-b79d-a2679b4600ea">

### Metric Display
The metric display, displayed in a pop up window, plots the metric values for each question along with a red line showing the mean and a green line and yellow line showing 1 standard deviation above and below the mean. We find that questions that fall outside this range are often interesting to look into. Hovering the cursor over the graphs will show the question numbers as x axis values. The graphs will appear in a pop up window.

<img width="756" alt="Screenshot 2024-06-11 at 2 24 40 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/044d93b4-8b9f-4bca-b2be-7c66650c9b70">

Alongside the graphs, a dataframe will be created as an output which shows the specific parameter values for each question. 

<img width="719" alt="Screenshot 2024-06-11 at 2 25 33 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/793eef8e-d09e-47e8-a149-4ce870b79c3e">

Note: For small datasets, many metrics may appear as 0. This is due to some transitions not being present (often RW or WSW).

### Density Plots
The density plots, displayed in a pop up window, show the distribution of each metric for different classes.

<img width="767" alt="Screenshot 2024-06-11 at 2 26 45 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/254cefec-4bbd-4915-a521-7d3f309250cd">

## Selecting Outputs
The program outputs can be changed at the bottom of the script by commenting out (#) all functions that the user does not wish to call. Note: the more outputs chosen, the longer the program run time.

<img width="1087" alt="Screenshot 2024-06-11 at 2 27 40 PM" src="https://github.com/ereadling/analyzing-test-data/assets/159862778/955e76a9-f9e8-4b7c-a8a3-95144bf0b67c">


