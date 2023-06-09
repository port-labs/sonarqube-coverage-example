# Ingesting SonarQube Metrics


## Getting started

In this example, you will create a blueprint for `sonarqubeMetric` that ingests all metrics and analysis performed on your SonarQube projects. You will then relate this `sonarqubeMetric` blueprint to a `repository` blueprint, allowing you to display all the metrics generated on your repositories. Also, you will add some script to make API calls to SonarQube Web API and fetch data for your webhook. Finally, you will configure your Gitlab to create/update your entities in Port every time a deployment or commit is made to a specified branch such as main/dev.

## Repository Blueprint
Create the repository blueprint in Port [using this json file](./resources/repository.md)

## SonarQube Metric Blueprint
Create the metric blueprint in Port [using this json file](./resources/sonarqube_metric.md)

## SonarQube Metric Webhook Configuration
Use the [webhook configuration file](./resources/sonarqube_metric_webhook_config.md) to create your Port webhook. 

Follow the example guide on how to [create a Port webhook](https://docs.getport.io/build-your-software-catalog/sync-data-to-catalog/webhook/#configuring-webhook-endpoints). You will then use the webhook URL to ingest data to Port via REST API.

### Gitlab CI yaml
Place this example `.gitlab-ci.yml` file in your project's root folder

### Gitlab CI Variables
To interact with Port using Gitlab CI Pipeline, you will first need to define your Port credentials [as variables for your pipeline](https://docs.gitlab.com/ee/ci/variables/index.html#define-a-cicd-variable-in-the-ui). Then, pass the defined variables to your ci pipeline script. This tutorial requires that the identifiers of your `repository` entities in Port corresponds to the actual name of your repository. This enables us to relate the `sonarqubeMetric` blueprint with the `repository` blueprint.

The list of the required variables to run this pipeline are:
- `PROJECT_KEY`
- `WEBHOOK_URL`
- `SONARQUBE_URL`
- `SONARQUBE_TOKEN`


Follow the documentation on how to [obatin a SonarQube token](https://docs.sonarqube.org/latest/user-guide/user-account/generating-and-using-tokens/). 

### Example SonarQube Metric Payload
Below is an example payload from the SonarQube Web API. It retrieves all the metrics related to a particular component.

```json showLineNumbers
{
    "component": {
        "id": "AYhnRZt5Led4AO_hsfL_",
        "key": "PeyGis_Chatbot_For_Social_Media_Transaction",
        "name": "Chatbot_For_Social_Media_Transaction",
        "qualifier": "TRK",
        "measures": [
            {
                "metric": "bugs",
                "value": "6",
                "bestValue": false
            },
            {
                "metric": "code_smells",
                "value": "214",
                "bestValue": false
            },
            {
                "metric": "vulnerabilities",
                "value": "1",
                "bestValue": false
            },
            {
                "metric": "sqale_debt_ratio",
                "value": "0.6",
                "bestValue": false
            },
            {
                "metric": "sqale_index",
                "value": "1427",
                "bestValue": false
            }
        ]
    }
}
```
### Package Entity Created
![Metric Entity Created](./assets/metric.PNG "Metric Entity Created")

### Python Resources
This project contains [example python resources](./python-tutorial/) that can be replaced with the shell script if you're using Python programming.
