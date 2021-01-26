## Tool for checking GCP permissions for a Service Account

## You must set the environment variable for the credentials file.
## Example: GOOGLE_APPLICATION_CREDENTIALS='mycredfile.json'

from google.cloud import resource_manager
import sys
import os
import googleapiclient.discovery
from google.oauth2 import service_account
from pprint import pprint

creds_file = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
gcp_client = resource_manager.Client()
gcp_creds = service_account.Credentials.from_service_account_file(creds_file)

service = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=gcp_creds)

try:
    request = service.projects().list()
    response = request.execute()

    for project in response.get('projects', []):
        projname=project['name']
        projid=project['projectId']
        print(f'Project found: {projname}')
        req = service.projects().getIamPolicy(resource=projid)
        resp = req.execute()
        pprint(resp)
except:
    sys.exit()
