# County Report

This folder contains visualizations and data for PPP (Payroll Protection Program) loans within Miami-Dade, FL.  All data is based upon the *project* state and county (as opposed to borrower state/county).  
The data in this report can be freely obtained from the U.S. Small Business Administration website at: [https://data.sba.gov/dataset/ppp-foia](https://data.sba.gov/dataset/ppp-foia).  
For information on NAICs codes or to look up a code, use: [https://www.census.gov/naics/](https://www.census.gov/naics/).

The county report folder should include the following contents.  Note that each file can be toggled on or off at the creation of the report (and pie charts will be automatically omitted if the county represents less than 1% of the state total).  If any desired graphs or figures are missing from the report, try navigating to the section "Choose Files to Save" in the Jupyter Notebook `county_report_generator.ipynb` to adjust these settings.

# Folder Contents
- [`cities.html`](#citieshtml)
- [`counties_map.html`](#countiesmaphtml)
- [`county_level_boxplots.png`](#county_level_boxplotspng)
- [`county_report.xlsx`](#county_reportxlsx)
- [`loan_level_boxplots.png`](#loan_level_boxplotspng)
- [`state_totals_pie_charts.png`](#state_totals_pie_chartspng)

## `cities.html`
An interactive scatter plot of the cities in Miami-Dade with respect to number of loans and loan amount. Hover over a mark to display the city name and the precise number of loans and loan dollars.

## `counties_map.html`
An interactive map of FL divided by county. Miami-Dade is highlighted in red and each county is colored by loan dollars approved. Hover over a county for more details.

## `county_level_boxplots.png`
A series of boxplots summarizing, at the county level, the number of loans approved, the amount of money approved, the number of jobs reported, and the charge-off rate. Each graph includes a boxplot for counties nationally, a boxplot for only those counties within FL, and a red line indicating Miami-Dade.

## `county_report.xlsx`
A complete breakdown of PPP loan information for Miami-Dade, FL as an Excel workbook with 8 sheets. They are:

* Overview: Provides summary loan statistics for the county, the rest of the state, and the U.S. This sheet also displays how long it took to generate the report and the top three cities in Miami-Dade by number of loans and loan dollars.
* Outliers (at a glance): The report generator dynamically locates key categories in which Miami-Dade differs from the rest of the state. For example, if "Manufacturing" appears as an outlier under the header "Top 5 Outliers (by loan dollars)," it indicates that the proportion of loan dollars in the county given to the manufacturing sector is significantly higher (or lower) than the proportion given to manufacturing across the rest of the state. See the included statistics to determine the direction (higher or lower) of this difference.
* County Level Descriptive Stats: Summarizes loan statistics per county at the state and national level. Note that "count" actually represents the number of counties which were given PPP loans across the nation and the state, respectively.  This sheet can be used to compare, for instance, the number of loans approved in Miami-Dade to the average approved per county on the national or state level.
* Loan Level Descriptive Stats: Summarizes loan statistics per loan at the state and national level and within Miami-Dade.
* Demographics: Provides demographics information on PPP loans at the state and national level and within Miami-Dade. Note that most loans in the data provided by the SBA do not provide demographics information.  For instance, approximately 61% of PPP loans nationally do not identify gender and approximately 75% do not identify race.
* Business Types: Breaks down loan information by business sector and provides a list of the five sectors with the most loans and the five sectors with the most loan dollars approved within Miami-Dade.
* Outliers (by loans): Provides a more complete set of outliers in which the number of loans approved in Miami-Dade differed from the rest of the state.
* Outliers (by loans): Provides a more complete set of outliers in which the amount of loan dollars approved in Miami-Dade differed from the rest of the state.

## `loan_level_boxplots.png`
Two sets of boxplots summarizing, at the loan level, the number of loans approved and the amount of money approved. Each graph includes a boxplot for loans nationally, a boxplot for only those loans within FL, and a boxplot for loans within Miami-Dade.

## `state_totals_pie_charts.png`
Includes a simple pie chart comparing Miami-Dade, FL to the rest of the state in number of loans, loan dollars, jobs reported, and charge-offs.  If the county represents less than 1% compared to the rest of the state, then that chart is omitted.  
>[!NOTE]  
>If the county represents less than 1% in each category, then no charts are included and the file `state_totals_pie_charts.png` is omitted.

