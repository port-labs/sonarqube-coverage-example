#!/bin/bash

# Get environment variables
WEBHOOK_URL="$WEBHOOK_URL"
PROJECT_KEY="$PROJECT_KEY"
SONARQUBE_URL="$SONARQUBE_URL"
SONARQUBE_TOKEN="$SONARQUBE_TOKEN"

add_entity_to_port() {
    # A function to create the passed entity in Port using the webhook URL

    entity_object="$1"
    headers="Content-Type: application/json"

    response=$(curl -s -X POST -H "$headers" -d "$entity_object" "$WEBHOOK_URL")
    echo "$response"
}

retrieve_sonarqube_metrics() {
    # Function to make API request to SonarQube Web API and retrieve metrics

    # Get SonarQube components/projects within the account
    headers="Authorization: Bearer $SONARQUBE_TOKEN"
    components_response=$(curl -s -H "$headers" "$SONARQUBE_URL/api/components/search?organization=$PROJECT_KEY")
    component_keys=$(echo "$components_response" | jq -r '.components[].key')

    # Iterate through the component keys and fetch all metrics associated with each component
    for component_key in $component_keys; do
        metrics_response=$(curl -s -H "$headers" "$SONARQUBE_URL/api/measures/component?component=$component_key&metricKeys=coverage,code_smells,sqale_index,sqale_debt_ratio,bugs,security_rating,vulnerabilities,alert_status,ncloc,sqale_rating,duplicated_lines_density,reliability_rating")
        webhook_data="$metrics_response"
        add_entity_to_port "$webhook_data"
    done
}

retrieve_sonarqube_metrics