# Wiki_task
### Description:
#### Using libs:
* Pandas - work with data.
* urllib - download web pages.
* lxml - select data from downloaded pages.
* BeautifulSoup, bs4 - select data from downloaded pages.

##### The repository contains two scripts (script_bs4.py , script_lxml.py).
Only the "find_link" function is different.
In one script, data extraction function(find_link) is done using lxml lib, in the other using BeautifulSoup lib.
This task can also be performed using the data extraction framework "Scrapy", but it is more suitable for production(large) projects.

The 'task' folder contains the condition of the task.
The 'data' folder contains all data. After running script, output-data saves in main folder and also save in this folder (In my opinion structure of the work project must logically separated).
