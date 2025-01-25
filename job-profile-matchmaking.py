from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {
    "resume_skills": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@stutijain2006/job-profile-matchmaking/{version}"
else:
    flow_name = "@stutijain2006/job-profile-matchmaking"

result = client.flow.execute(flow_name, input_data)
print(result)