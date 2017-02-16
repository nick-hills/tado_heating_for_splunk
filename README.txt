# tado Heating App for Splunk
Splunk App to collect and report on data from the tado Heating System - see http://www.tado.com for more information.

The author of this Splunk App has no affiliation with tado, other than as a user of the product.

##Installation
After installing the package from: 

	* git https://github.com/nickhills81/tado_heating_for_splunk
	* Splunkbase https://splunkbase.splunk.com/app/3479

###Credentials
When the application is run for the first time you will be prompted to enter your credentials for tado.
These credentials are used to query the tado API in order to fetch the status of your installation and local weather.

###The tado Index
You are also asked if you would like to disable the "tado" index. 
**Most users should uncheck this box**

In distributed or cluster deployments, automaticaly adding indexes can cause complications. You may prefer to create your indexes via a master app or by hand. 

In order for the dashboards and datamodels to work by default they expect the index to be called tado, however if you wish to change the index name, you will need to change the following:

	* Clone inputs.conf into your ./local folder. Edit the input entries and specify your desired index name.
	* Edit the macro "tadoIndex" and replace index=tado with the index name of your choice. 


##Known Issues
* Not all weather types may be handled correctly - If you spot a weather type which does not render with the correct (or sensible) icon, please let the author know. You can obtain a list of all the weather types you have experience using the query: `'tadoIndex' weather=*|dedup weather|table weather`
