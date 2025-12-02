# Policy Evaluation Assignment 8: Difference-in-Differences

## Overview
This folder contains all materials required for Assignment 8. It includes:
- **PDF report** with analytical answers and all required figures/tables
- **Stata do-files** used for replication of figures and tables
- **Dataset** (`assignment8.dta`) required to run the code

## Folder Structure
```
assignment8_folder/
├── EconometricsHW8.pdf
├── assignment8_q1.py
├── assignment8_q3.ipynb
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

## Question 1.1:

### Requirements
- Python 3.13 or later
- Required packages:
  - `pandas>=2.3.3`
  - `numpy>=2.3.5`
  - `matplotlib>=3.9.0`
- Dataset: `assignment8.dta`

### How to Run the Code
1. Ensure the dataset `assignment8.dta` is in the same folder as the script
2. Run the Python script: `assignment8_q1.py`

The script will automatically:
- Load the dataset `assignment8.dta`
- Calculate wage distribution percentages for each state and time period
- Generate **Figure 1a**: Distribution of starting wages in February 1992 (before minimum wage increase)
- Generate **Figure 1b**: Distribution of starting wages in November 1992 (after minimum wage increase)
- Save figures as `figure1_feb1992.png` and `figure1_nov1992.png`
- Print diagnostic statistics to console

### Expected Output
- `figure1_feb1992.png`: Shows similar wage distributions in NJ and PA before the policy change, with both states having wages clustered around $4.25
- `figure1_nov1992.png`: Shows dramatic divergence, with approximately 85% of NJ stores clustering at $5.05 (new minimum wage), while PA distribution remains relatively unchanged

### Notes
- The code uses side-by-side bars matching the original paper's presentation style
- Black solid bars represent New Jersey stores
- White hatched bars represent Pennsylvania stores
- Bins are defined as 10-cent intervals from $4.25 to $5.65 (14 bins total)
- The visualization includes light horizontal gridlines for easier reading
- All percentages are calculated relative to the total number of stores in each state-time combination
- Ensure that `assignment8.dta` is located in the same folder as the Python script

### Key Variables Used
- `state`: 1 = New Jersey, 0 = Pennsylvania
- `wage_st`: Starting wage (dollars per hour)
- `time`: 0 = Wave 1 (February 1992), 1 = Wave 2 (November 1992)

---

## Question 1.2:

---

## Requirements

### Python Version
- `requires-python = ">=3.13"`

### Required Packages
- `pandas>=2.3.3`
- `statsmodels>=0.14.5`

### Installation
Run the following command to install dependencies:
```bash
pip install pandas>=2.3.3 statsmodels>=0.14.5
```

Alternatively, if using `uv`:
```bash
uv sync
```

---

## Dataset

**Filename:** `assignment8.dta`

**Format:** Stata data file

**Structure:** Panel data with two observations per restaurant (Wave 1: pre-treatment, Wave 2: post-treatment)

---

## How to Run the Code

1. Open `assignment8_q3.ipynb` 
2. Ensure `assignment8.dta` is in the same directory as Notebook file
3. Run all cells sequentially

---

## What the Script Does

### 1. Loads the Dataset
Reads `assignment8.dta` 

### 2a. Creates the Dataset to Match Original n = 357
Using chaining, the code selects variables, creates the appropriate target variable, applies filters, does one hot encoding, and cleans the data for modeling.
- this uses FTE = full time + 0.5 * part time + managers
- store filter: existence FTE = full time + 0.5 * part time AND nmgrs is not missing in second period
- this method allows for missingness in managers data only for the second period to match the desired n = 357

### 2b. Creates the Dataset to Match Original Target Var Definition (FTE)
Using chaining, the code selects variables, creates the appropriate target variable, applies filters, does one hot encoding, and cleans the data for modeling.
- this uses FTE = full time + 0.5 * part time + managers
- store filter: existence FTE = full time + 0.5 * part time + nmgrs 
- this methods follows the FTE definition in detail and retains a smaller set of the sample (n = 351)

### [OPTIONAL] 3. Validates Creation of Data in 2b by Comparing Disrepancies and Characteristics
Sees differences in stores used from dataset in 2a and 2b. Then, characteristics (especially missingness of the nmgrs data) are compared to validate the decisions that arrive at n = 357.

### 4. Runs Model 1a of Card and Kruger (1944) on Datasets in 2a and 2b With and Without Controls
The full form equation, d_E ~ state + co_owned + chain_K + chain_R + chain_W, and reduced form without controls, d_E ~ state, are ran for both samples with 351 stores and 357 stores.

## Expected Output
Four model summaries. The summaries contain estimates of the following specifications:
1. No controls, n = 351
2. Controls, n = 351
3. No controls, n = 357
4. Controls, n = 357


## Notes
Section 3 is optional (validation). Commentary is provided on the results.



---

## Question 1.3: 

---

## Requirements

### Python Version
- `requires-python = ">=3.13"`

### Required Packages
- `pandas>=2.3.3`
- `statsmodels>=0.14.5`

### Installation
Run the following command to install dependencies:
```bash
pip install pandas>=2.3.3 statsmodels>=0.14.5
```

Alternatively, if using `uv`:
```bash
uv sync
```

---

## Dataset

**Filename:** `assignment8.dta`

**Format:** Stata data file

**Structure:** Panel data with two observations per restaurant (Wave 1: pre-treatment, Wave 2: post-treatment)

---

## How to Run the Code

1. Open `assignment8_q3.ipynb` 
2. Ensure `assignment8.dta` is in the same directory as Notebook file
3. Run all cells sequentially

---

## What the Script Does

### 1. Loads the Dataset
Reads `assignment8.dta` using `pandas.read_stata`:
```python
df = pd.read_stata('assignment8.dta')
```

### 2. Constructs the Full Meal Price Variable
Creates the dependent variable by summing component prices:
```python
df['pricemeal'] = df['priceentree'] + df['pricesoda'] + df['pricefry']
```
A full meal consists of:
- One entree
- One medium soda
- One small fries

### 3. Reshapes Panel Data to Cross-Section
Separates pre-period (Wave 1, `time==0`) and post-period (Wave 2, `time==1`) observations:
```python
pre = df[df['time'] == 0].copy()
post = df[df['time'] == 1].copy()
merged = pre.merge(post, on='store', suffixes=('_pre', '_post'))
```
This creates one observation per restaurant with both pre and post values.

### 4. Constructs the Outcome Variable
Calculates the change in full meal price (ΔP):
```python
merged['delta_price'] = merged['pricemeal_post'] - merged['pricemeal_pre']
```

### 5. Creates Control Variables
Generates control variables using **pre-period values only**:

**Company ownership indicator:**
```python
control_candidates = ['co_owned_pre']
```

**Chain dummy variables (reference category: Burger King, chain==1):**
```python
for i in range(2, 5):
    merged[f'chain_{i}'] = (merged['chain_pre'] == i).astype(int)
```
Creates dummies for:
- `chain_2`: KFC
- `chain_3`: Roy Rogers
- `chain_4`: Wendy's

### 6. Creates the Treatment Variable
Defines the New Jersey treatment indicator:
```python
merged['NJ'] = merged['state_pre']
```
Where:
- `NJ = 1`: Restaurant located in New Jersey (treatment group)
- `NJ = 0`: Restaurant located in Pennsylvania (control group)

### 7. Drops Missing Observations
Removes observations with missing values in:
- Change in meal price (`delta_price`)
- Treatment indicator (`NJ`)
- Control variables (`co_owned_pre`, chain dummies)
```python
regression_data = merged[['delta_price', 'NJ'] + control_candidates].dropna()
```

### 8. Runs OLS Regressions

The script estimates the difference-in-differences specification:

**ΔPᵢ = α₀ + β·Xᵢ + γ·NJᵢ + εᵢ**

Where:
- **Dependent variable:** `delta_price` (change in full meal price)
- **Treatment variable:** `NJ` (New Jersey indicator)
- **Control variables:** `co_owned_pre`, `chain_2`, `chain_3`, `chain_4`
- **Parameter of interest:** γ (coefficient on NJ)

#### Specification 1: With Controls
```python
X = regression_data[['NJ'] + control_candidates]
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
```
Includes chain dummies and company ownership indicator.

#### Specification 2: Without Controls
```python
X_simple = sm.add_constant(regression_data['NJ'])
model_simple = sm.OLS(y_simple, X_simple)
results_simple = model_simple.fit()
```
Simple difference-in-differences without control variables (robustness check).

### 9. Produces Outputs

The script prints detailed regression results for both specifications:

#### Model Summary (With Controls)
- Full regression table with all coefficients
- Standard errors (OLS)
- t-statistics and p-values
- R-squared and adjusted R-squared
- Number of observations

#### Key Results Section
- Treatment effect coefficient (γ)
- Standard error
- t-statistic
- p-value
- Sample size

#### Summary Statistics
- Mean price change in New Jersey
- Mean price change in Pennsylvania
- Raw difference between treatment and control groups

#### Alternative Specification (Without Controls)
- Full regression results without control variables
- Robustness check to assess sensitivity to controls

---

## Output Structure

### Console Output Format
```
================================================================================
Effect of Minimum Wage Increase on Full Meal Price
================================================================================
                            OLS Regression Results
==============================================================================
Dep. Variable:            delta_price   R-squared:                       0.058
Model:                            OLS   Adj. R-squared:                  0.047
Method:                 Least Squares   F-statistic:                     5.422
...
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0729      0.050     -1.467      0.143      -0.171       0.025
NJ             0.1105      0.049      2.278      0.023       0.015       0.206
co_owned_pre  -0.0254      0.057     -0.448      0.655      -0.137       0.086
chain_2        0.0473      0.062      0.767      0.444      -0.074       0.169
chain_3        0.0877      0.065      1.352      0.177      -0.040       0.215
chain_4       -0.0126      0.067     -0.188      0.851      -0.145       0.120
==============================================================================

Key Results:
================================================================================
Coefficient on NJ (treatment effect): 0.1105
Standard error: 0.0485
t-statistic: 2.278
p-value: 0.0233
Number of observations: 356

Summary Statistics:
================================================================================
Mean change in meal price (NJ): $0.0901
Mean change in meal price (PA): $-0.0100
Difference: $0.1001
```

---
