# Springfield-Crime Data

The Springfield-Crime dataset consists of monthly totals of police reports filed in Springfield Missouri between January, 2004,and December, 2016. The data is stored in a pandas multindex dataframe to allow for easy analysis of the data in full or within specified time periods. A series of Jupyter Notebooks are included to show how the data was visualized. 

### Collection Method

Data was collected from the website SpringfieldCrimeAlert using the Pandas read_html() method. See Scraper.py for details. 

### Limitations

##### Data Limitations

The data cannot be verified as complete as the collection methods for SpringfieldCrimeAlert(assumed to be a third party and not the Springfield Police Department) are not known. There is a strong case that reports are collected through the [police calls search page](https://www.springfieldmo.gov/1724/Police-Calls-Search) as descripitions and "approximate location" addresses are identical. This leaves concern that reports are being missed that are [filed online](https://www.springfieldmo.gov/873/Online-Police-Report). However, its also unclear how many reports are filed online rather than over the phone, and may be statistically insignificant to begin with.

##### External Factors. 
Given that 12 years of data are presented in the dataset the user must be careful in analyzing data without knowing what changes in reporting methods.