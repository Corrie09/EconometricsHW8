markdown# Policy Evaluation Assignment 8: Difference-in-Differences

## Overview
This folder contains all materials required for Assignment 8. It includes:
- **PDF report** with analytical answers and all required figures/tables
- **Stata do-files** used for replication of figures and tables
- **Dataset** (`assignment8.dta`) required to run the code

## Folder Structure
```
assignment8_folder/
├── EconometricsHW8.pdf
├── assignment8_q1.do
├── assignment8.dta
└── README.md
```

## Team Members
Joshua Castillo,
Nikoloz Darsalia, 
Corneel Moons

## Questions Covered
- **Question 1.1**: Replication of Figure 1 from Card and Krueger (1994)
- **Question 1.2**: Estemating the model as in the paper
- **Question 1.3**: Investigating full meal pricing policy

---

## Question 1.1: Replication of Figure 1

### Requirements
- Stata 17 or later
- Dataset: `assignment8.dta`

### How to Run the Code
1. Open Stata
2. Set the working directory to the project folder
3. Run the do-file: `assignment8_q1.do`

The script will automatically:
- Load the dataset `assignment8.dta`
- Generate **Figure 1a**: Distribution of starting wages in February 1992 (before minimum wage increase)
- Generate **Figure 1b**: Distribution of starting wages in November 1992 (after minimum wage increase)
- Save figures as `figure1_feb1992.png` and `figure1_nov1992.png`

### Expected Output
- `figure1_feb1992.png`: Shows similar wage distributions in NJ and PA before the policy change
- `figure1_nov1992.png`: Shows dramatic divergence, with NJ wages clustering at $5.05 (new minimum)

### Notes
- The code uses overlapping histograms (rather than side-by-side bars) to make the comparison clearer
- Ensure that `assignment8.dta` is located in the same folder as the do-file

### Key Variables Used
- `state`: 1 = New Jersey, 0 = Pennsylvania
- `wage_st`: Starting wage (dollars per hour)
- `time`: 0 = Wave 1 (February 1992), 1 = Wave 2 (November 1992)

---

## Question 1.2:



---

## Question 1.3: 


