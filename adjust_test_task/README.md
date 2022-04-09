Adjust Home Task

**Description**

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.<br/>
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.<br/>
Dataset is expected to be stored and processed in a relational database. 

Client of this API should be able to:
1) filter by time range (date_from+date_to is enough), channels, countries, operating systems
2) group by one or more columns: date, channel, country, operating system
3) sort by any column in ascending or descending order
4) see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

**Results**

Common API use-cases:
1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. Hint:
```
=> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from sampledataset where date < '2017-06-01' group by channel, country order by clicks desc;
     channel      | country | impressions | clicks 
------------------+---------+-------------+--------
 adcolony         | US      |      532608 |  13089
 apple_search_ads | US      |      369993 |  11457
 vungle           | GB      |      266470 |   9430
 vungle           | US      |      266976 |   7937
 ...
```

Result: <a href="http://127.0.0.1:5000/database_interaction/result?_query=select+channel%2C+country%2C+sum%28impressions%29+as+impressions%2C+sum%28clicks%29+as+clicks+from+dataset+where+date+%3C+%272017-06-01%27+group+by+channel%2C+country+order+by+clicks+desc%3B">click here.</a>  

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.  
Query: select date, sum(installs) as installs from dataset where date like '2017-05%' and os='ios' group by date order by date;  
Result: <a href="http://127.0.0.1:5000/database_interaction/result?_query=select+date%2C+sum%28installs%29+as+installs+from+dataset+where+date+like+%272017-05%25%27+and+os%3D%27ios%27+group+by+date+order+by+date%3B">click here.</a>  

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.  
Query: select os, revenue from dataset where date = '2017-06-01' and country='US' group by os order by revenue desc;  
Result: <a href="http://127.0.0.1:5000/database_interaction/result?_query=select+os%2C+revenue+from+dataset+where+date+%3D+%272017-06-01%27+and+country%3D%27US%27+group+by+os+order+by+revenue+desc%3B">click here.</a>

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.  
Query:  select avg(cpi), spend from dataset where country='CA' group by channel order by cpi desc;  
Result: <a href="http://127.0.0.1:5000/database_interaction/result?_query=select+round%28avg%28cpi%29%2C+2%29+as+avg_cpi%2C+spend+from+dataset+where+country%3D%27CA%27+group+by+channel+order+by+cpi+desc%3B">click here.</a>

**Instructions**

- The project consists of the modules:
  - `app.py` – the main application module; contains the logic of the project.
  - `fill_db_dataset.py` – auxiliary module to import sample dataset into the database.
  - `config.py` – configuration file for convenience.
- There are also two directories: `data` for dataset(s) and `templates` for templates. 
- To fill in the database to be able to work with it, please, run fill_db_dataset.py first. 
- The name of the table is dataset. So, please, use it when trying to access data. 
- The code itself might seem a little over-commented but, since I did a project like that for the first time as well as used most of the libraries, it was important to me to document it along the way, so I did and that's why I won't go into the details here.
