# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_function_calling]
from vertexai.preview.generative_models import (
    FunctionDeclaration,
    GenerativeModel,
    Tool,
)

# Load the Vertex AI Gemini API to use function calling
model = GenerativeModel("gemini-pro")

# Specify a function declaration and parameters for an API request
get_current_weather_func = FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    # Function parameters are specified in OpenAPI JSON schema format
    parameters={
        "type": "object",
        "properties": {"location": {"type": "string", "description": "Location"}},
    },
)

# Define a tool that includes the above get_current_weather_func
weather_tool = Tool(
    function_declarations=[get_current_weather_func],
)

# Prompt to ask the model about weather, which will invoke the Tool
prompt = "What is the weather like in Boston?"

# Instruct the model to generate content using the Tool that you just created:
response = model.generate_content(
    prompt,
    generation_config={"temperature": 0},
    tools=[weather_tool],
)

# Print the entire response
print(response)

# Print the part of the response that contains info about the function call
print(response.candidates[0].content.parts[0].function_call)
# [END aiplatform_function_calling]