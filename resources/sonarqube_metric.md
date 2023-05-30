```json showLineNumbers
{
  "identifier": "sonarqubeMetrics",
  "description": "This blueprint represents a SonarQube metric in our catalog",
  "title": "SonarQube Metric",
  "icon": "sonarqube",
  "schema": {
    "properties": {
      "value": {
        "type": "number",
        "title": "Metric Value"
      },
      "bestValue": {
        "type": "string",
        "title": "Metric Best Value"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "repository": {
      "title": "Repository",
      "target": "repository",
      "required": true,
      "many": false
    }
  }
}
```