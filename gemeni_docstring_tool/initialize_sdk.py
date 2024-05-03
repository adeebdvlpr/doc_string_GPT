import vertexai
from vertexai.preview import reasoning_engines

#MAY NOT BE IN USE WITH CREWAI 
vertexai.init(
    project=" docstringtool",
    location="us-central1",
    staging_bucket="gs://vertex_app_bucket ",
)