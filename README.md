# Policy, Risk, and Norms Shape Collective Behaviors Worldwide

This repository contains code, data, and analysis for the study of mask-wearing behavior during the COVID-19 pandemic.  
It includes tools for **model calibration**, **uncertainty quantification**, and **data analysis**, applied to data from 47 countries.  

The main model is a **utility-based decision framework** that incorporates policy mandates, risk perception from disease incidence, and social norms.  
We calibrate the model using daily data on mask usage, COVID-19 deaths, and policy stringency, then validate it temporally.

---

## Repository Structure

```
.
├── Mask_wearing_analysis.ipynb    # Main notebook for model calibration, uncertainty quantification, and analysis
├── simulation_A.py                # Runs simulation for Model A
├── simulation_B.py                # Runs simulation for Model 
├── simulation_C.py                # Runs simulation for Model A
├── simulation_D.py                # Runs simulation for Model A
├── simulation_E.py                # Runs simulation for Model A
├── simulation_F.py                # Runs simulation for Model A
├── simulation_G.py                # Runs simulation for Model A

├── Data/
│   ├── mask_complete.pickle              # Self-reported mask usage for entire time period
│   ├── mask_calibration.pickle              # Self-reported mask usage for entire time period
│   ├── mask_validation.pickle              # Self-reported mask usage for entire time period
│   ├── new_deaths_mil.pickle              # WHO/OWID COVID-19 deaths per million
│   ├── new_cases_mil.pickle               # WHO/OWID COVID-19 cases
│   ├── policy.pickle         # Oxford COVID-19 Government Response Tracker
│   ├── SE_factors.pickle            # GDP, literacy, population density
│   ├── Tightness_Scores.xlsx            # GDP, literacy, population density
│   └── collectivism.pickle     # Cultural tightness & collectivism
└── README.md                         # This file
```

---

## Data Sources

The analysis presented in this study relies on multiple data sources:

1. **COVID-19-related deaths**  
   - Source: World Health Organization (WHO) via *Our World in Data* ([OWID COVID-19 deaths](https://ourworldindata.org/covid-deaths))  
   - Data: Daily counts of COVID-19-related fatalities per million  
   - Pre-processing: Smoothed using a 7-day moving average  
   - Usage: Estimates risk in the model

2. **Mask mandates**  
   - Source: Oxford COVID-19 Government Response Tracker ([OxCGRT](https://github.com/OxCGRT/covid-policy-tracker))  
   - Variable: `H6M_Facial Coverings` (scale 1–5, daily)  
   - Usage: Policy stringency signal

3. **Self-reported mask usage**  
   - Source: University of Maryland Social Data Science Center Global COVID-19 Trends and Impact Survey (UMD Global CTIS) in partnership with Facebook ([API](https://covidmap.umd.edu/api.html))  
   - Variable: `pct_mc` (percentage of respondents reporting wearing masks all/most of the time in public)  
   - Survey question: C5  
   - Period: April 26, 2020 – July 26, 2021 (457 days)  
   - Data split: 276 days for calibration + 181 days for validation  
   - Usage: Primary behavioral outcome

4. **Socio-cultural and economic indicators**  
   - Cultural tightness & collectivism: From literature ([Gelfand et al., 2011](https://science.sciencemag.org/content/332/6033/1100), [Gelfand et al., 2021](https://www.pnas.org/content/118/3/e2021793118), [Pelham et al., 2022](https://www.nature.com/articles/s41562-021-01266-7))  
   - GDP per capita, population density, literacy rate: *Our World in Data*

---

## How to Use

### Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Notebook
Open:
```bash
jupyter notebook notebooks/calibration_analysis.ipynb
```
Follow the cells in order to:
- Calibrate the model for selected countries
- Perform uncertainty quantification
- Generate validation and analysis plots


---

## Citation
If you use this code or data, please cite the original data sources and this repository:
```
Mittal, D. (2025). Mask-wearing behavior during COVID-19. GitHub repository: https://github.com/d-mittal/Mask_wearing_COVID
```
