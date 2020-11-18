# New York City Crashes

Helping the mayors office and other stakeholders to derive insights from Motor Vehicle Collisions/Crashes

## Goal

To provide an interactive means for the mayors office and other stakeholders from New York City (NYC) to easily access motor vehicle collision information in an interactive manner thereby aiding them to make informed decisions.

## System Description

### Stakeholders

**Primary Stakeholder**

* Mayors office

**Secondary Stakeholders**

* Police officers
* Insurance companies
* Medical facilities
* Fire departments
* Ordinary citizens
* Roadusers / drivers
* NYC city council

### Main Systems of Interest
* A Power BI Dashboard that allows **analysts** in the mayors office to visualize number of crashes by time period and location. 
* In addition our Power BI Dashbaord should provide some statistical information about crashes in New York City.
* Finally our Power BI Dashbaord will show the closest police station as well as closeset hospitals to crashes.

### Enabling Systems
Systems that will enable us build our primary system are automated cron jobs or schedulers that will fecth, clean and store data from the sources listed below

**Data Sources**

* Primary data source:
  https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95
* Supporting/Secondary data sources:
  * Firehouse locations
    https://data.cityofnewyork.us/Public-Safety/FDNY-Firehouse-Listing/hc8x-tcnd
  * Neighbourhood Population
    https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Neighborhood-Tabulatio/swpk-hqdp
  * Realtime Traffic Data
    https://data.cityofnewyork.us/Transportation/Real-Time-Traffic-Speed-Data/qkm5-nuaq
  * Historical Traffic Data
    https://data.cityofnewyork.us/Transportation/Traffic-Volume-Counts-2012-2013-/p424-amsu
  * Parking Violations
    https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/i4p3-pe6a
  * Metropolitan transportation data
    https://data.cityofnewyork.us/Transportation/MTA-Data/mmu8-8w8b
  * Emergency calls
    https://data.cityofnewyork.us/Public-Safety/911-End-to-End-Data/t7p9-n9dy
  * List of hospitals as of 2011
    https://data.cityofnewyork.us/Health/NYC-Health-Hospitals-Facilities-2011/ymhw-9cz9
  * List of police stations
    https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz

**ETL**
* Azure Data Factory

**Storage**
* Azure Data Lake Storage

**Dashboards/Reports**
* Azure Power BI
* Azure Synapse Analytics

### System Boundaries
**Roles and Responsibilities**

* Automated Software i.e Background Processes
* Data Owner
  - Police Department provides the motor vehicle crash information
* Data Analysts in Mayors office
* Developers/ System Admenistrators
* General Punblic


**Possible Functionalities of System**

* Easily query data about crushes with little to no technical knowlegde
* Easily create and share informative visualizations with people
* Access to basic informative visualizations:
  * Visualize places where accidents happened for last several days
  * Visualize nearest hospitals to the places of accidents
* Provide statistics and predictions:
  * Get information about what are the districts / crossroads where accidents occured most frequently for last week / month
  * Predict districts where an accident is more likely to occur today
  * Get information about how often does crashes take place on a specific street / crossroad
* Easily export data, visualizations or reports in some desired format
* Easily import current information about accidents




## TODO:

* SRS (software requirements specification) 

* Process models 

  * Current state (if exists) 

  * Reengineering of processes/new processes 

  * Definition of data artifacts 

* Data models 

  * Conceptual data model 

  * Logical data model 

* BPM implementation description 

  * Business process automation principals 

  * Business rules 

* Testing 

* Validation 

* Conclusion 



## Extra Reading

https://towardsdatascience.com/new-to-data-visualization-start-with-new-york-city-107785f836ab?gi=54183ba7443f

https://cawemo.com/diagrams/0b163bee-a87b-4d0e-a0e3-72af2b8c2ec3--etl-and-other-processes?v=960,378,1


https://azure.microsoft.com/en-in/solutions/big-data/#products
