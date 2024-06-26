import os
import requests
import base64

# Jira API configuration
JIRA_BASE_URL = os.getenv("ATLASSIAN_BASE_URL")
JIRA_API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")
JIRA_USER_EMAIL = os.getenv("ATLASSIAN_USER_EMAIL")

def get_jira_headers():
    auth = f"{JIRA_USER_EMAIL}:{JIRA_API_TOKEN}"
    auth_base64 = base64.b64encode(auth.encode('ascii')).decode('ascii')
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/json"
    }
    return headers

def fetch_jira_project_state():
    url = f"{JIRA_BASE_URL}/rest/api/3/search"
    query = {
        'jql': 'project = MVP',
        'fields': 'summary,status,assignee,parent'
    }
    response = requests.get(url, headers=get_jira_headers(), params=query)
    return response.json()

def main():
    # Fetch current Jira project state
    jira_data = fetch_jira_project_state()
    with open("jira_data.txt", "w") as f:
        f.write(str(jira_data))

if __name__ == "__main__":
    main()