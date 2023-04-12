# Aisling's Bus tours, using Django and Azure App Service

Azure App Service automatically creats a virtual envoirnment for Python projects. It also automatically does a pip install -r requirements.txt

Fork the repo

In Azure you must create an:
* App Service Plan
* App Service
* Azure SQL DB
* Azure Storage - Container

Using the SQL queries code, create and populate the tables in the Azure SQL DB

# Setting up Slots in App Service
1. In the Azure App Service, go to the Deployment Slots and create a slot called 'staging'
2. Navigate to the staging slot and go to Configuration.

Add Application Settings:
* Name: WEBSITE_HEALTHCHECK_MAXPINGFAILURES Value: 10 - tick deployment slot setting
* Name: SCM_DO_BUILD_DURING_DEPLOYMENT Value: 1 - tick deployment slot setting
* Name: ALLOWED_HOSTS : Value: `<your-domain-name>`
* You must press save

Go to general settings:
* choose Python 3.9, 
* You must press save
3. Navigate to the the Deployment Center of staging slot and select GitHub, choose your github account and repo, choose your development slot

# Managed Identity
1. In the Azure App Service, go to the Identity and turn on System Assigned Managed Identity
2. In the Azure Active Directory go to Enterprise Applications and search for your App Service (you may need to remove some of the preset filters), click on it and go to Properties

# Blob Storage
In your Storage account navigate to Containers, create a container with access level of Container.
Upload your images and copy their URL for use in the HTML template of base.html (which is in home/templates)
