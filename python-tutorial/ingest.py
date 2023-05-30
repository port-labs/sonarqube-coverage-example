## Import the needed libraries
import requests
from decouple import config

# Get environment variables using the config object or os.environ["KEY"]
# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
WEBHOOK_URL = config("WEBHOOK_URL")
PROJECT_KEY = config("PROJECT_KEY")
SONARQUBE_URL = config("SONARQUBE_URL")
SONARQUBE_TOKEN = config("SONARQUBE_TOKEN")


def add_entity_to_port(entity_object):
    """A function to create the passed entity in Port using the webhook URL

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog
    
    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=entity_object, headers=headers)
    print(response.json())


def retrieve_sonarqube_metrics():
    """A function to make API request to SonarQube and retrieve metrics"""

    ## First, get SonarQube components/projects within the account
    headers = {'Authorization': f'Bearer {SONARQUBE_TOKEN}'}
    components_response = requests.get(f'{SONARQUBE_URL}/api/components/search?organization={PROJECT_KEY}', headers=headers)
    components = components_response.json()['components']

    # ## Iterate through the components and fetch all metrics associated with it
    for component in components:
        metrics_response = requests.get(f'{SONARQUBE_URL}/api/measures/component?component={component["key"]}&metricKeys=coverage,code_smells,sqale_index,sqale_debt_ratio,bugs,security_rating,vulnerabilities,alert_status,ncloc,sqale_rating,duplicated_lines_density,reliability_rating', headers=headers)

        webhook_data = metrics_response.json()
        add_entity_to_port(webhook_data)

retrieve_sonarqube_metrics()