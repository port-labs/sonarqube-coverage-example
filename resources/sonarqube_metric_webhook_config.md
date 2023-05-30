```json showLineNumbers
{
    "identifier": "sonarqubeMetricMapper",
    "title": "Sonarqube Metric Mapper",
    "description": "A webhook configuration to map Sonarqube Metrics to Port",
    "icon": "sonarqube",
    "mappings": [
        {
            "blueprint": "sonarqubeMetrics",
            "itemsToParse": ".body.component.measures",
            "entity": {
                "identifier": ".body.component.id + \"-\" + .item.metric",
                "title": ".item.metric",
                "properties": {
                    "value": ".item.value",
                    "bestValue": "item.bestValue"
                },
                "relations": {
                    "repository": ".body.component.name"
                }
            }
        }
    ],
    "enabled": true,
    "security": {}
}
```