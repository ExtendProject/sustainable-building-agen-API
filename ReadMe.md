### API Endpoint Documentaion

This endpoint allows you to analyze user data and provide recommendations based on the input.

#### Request Body Parameters

- `user_name` (text): The name of the user.
- `budget` (text): The budget for the analysis.
- `location` (text): The location for the analysis.
- `current_weather_condition` (text): The current weather condition at the location.
- `images` (file): Images related to the analysis.

#### Response

The response is in JSON format and follows the schema below:

```json
{
  "budget": 0,
  "final_remarks": "",
  "remaining_amount_form_budget": 0,
  "results": [
    {
      "materials_objects_tools": "",
      "observed_in_images": "",
      "sustainable_alternative": "",
      "found_alternatives_from_market": "",
      "cost_efficient": "",
      "notes": "",
      "budget_allocation": ""
    }
  ],
  "total_estimated_spendings": 0,
  "user_name": ""
}

```

This endpoint allows you to analyze user data and provide recommendations based on the input parameters.

#### Request Body Parameters

- `user_name` (text): The name of the user submitting the data.
- `budget` (text): The budget set by the user for the analysis.
- `location` (text): The location for which the analysis is being conducted.
- `current_weather_condition` (text): The current weather condition at the location.
- `images` (file): Images related to the analysis.

#### Response

The response is in JSON format and includes the following fields:

- `budget` (number): The budget set for the analysis.
- `final_remarks` (string): Final remarks or recommendations based on the analysis.
- `remaining_amount_form_budget` (number): The remaining amount from the budget after the analysis.
- `results` (array): An array of objects containing detailed analysis results, including materials, observed objects, sustainable alternatives, found alternatives from the market, cost efficiency, notes, and budget allocation.

  - `materials_objects_tools` (string): Details of materials, objects, or tools used in the analysis.
  - `observed_in_images` (string): Objects observed in the images provided.
  - `sustainable_alternative` (string): Sustainable alternatives recommended.
  - `found_alternatives_from_market` (string): Alternatives found in the market.
  - `cost_efficient` (string): Cost-efficient options identified.
  - `notes` (string): Additional notes related to the analysis.
  - `budget_allocation` (string): Allocation of the budget for different aspects of the analysis.
- `total_estimated_spendings` (number): The total estimated spendings based on the analysis.
- `user_name` (string): The name of the user for whom the analysis was conducted.

#### JSON Schema

```json
{
  "type": "object",
  "properties": {
    "budget": { "type": "number" },
    "final_remarks": { "type": "string" },
    "remaining_amount_form_budget": { "type": "number" },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "materials_objects_tools": { "type": "string" },
          "observed_in_images": { "type": "string" },
          "sustainable_alternative": { "type": "string" },
          "found_alternatives_from_market": { "type": "string" },
          "cost_efficient": { "type": "string" },
          "notes": { "type": "string" },
          "budget_allocation": { "type": "string" }
        }
      }
    },
    "total_estimated_spendings": { "type": "number" },
    "user_name": { "type": "string" }
  }
}

```

This endpoint allows you to analyze the user's input for budget, location, current weather condition, and images to provide insights and recommendations.

#### Request Body

- `user_name` (text): The name of the user.
- `budget` (text): The budget for the analysis.
- `location` (text): The location for which the analysis is being conducted.
- `current_weather_condition` (text): The current weather condition at the location.
- `images` (file): Images related to the analysis.

#### Response

The response is in JSON format and includes the following fields:

- `budget` (number): The budget for the analysis.
- `final_remarks` (string): Final remarks or conclusions from the analysis.
- `remaining_amount_form_budget` (number): The remaining amount from the budget.
- `results` (array): An array of objects containing analysis results with fields like materials/objects/tools, observed in images, sustainable alternatives, found alternatives from the market, cost efficiency, notes, and budget allocation.
- `total_estimated_spendings` (number): The total estimated spendings for the analysis.
- `user_name` (string): The name of the user.

#### JSON Schema

```json
{
  "type": "object",
  "properties": {
    "budget": { "type": "number" },
    "final_remarks": { "type": "string" },
    "remaining_amount_form_budget": { "type": "number" },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "materials_objects_tools": { "type": "string" },
          "observed_in_images": { "type": "string" },
          "sustainable_alternative": { "type": "string" },
          "found_alternatives_from_market": { "type": "string" },
          "cost_efficient": { "type": "string" },
          "notes": { "type": "string" },
          "budget_allocation": { "type": "string" }
        }
      }
    },
    "total_estimated_spendings": { "type": "number" },
    "user_name": { "type": "string" }
  }
}

```
