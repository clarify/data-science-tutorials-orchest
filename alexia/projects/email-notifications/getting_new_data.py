import orchest
from pyclarify import ClarifyClient
from datetime import datetime, timedelta
import os

item_id = orchest.get_step_param("item_id")
hours = orchest.get_step_param("hours")

print("Getting data from Clarify")
credentials = os.environ["credentials"]
client = ClarifyClient(credentials)
from_date = datetime.today() - timedelta(hours=hours) #days= 1, hours=1, minutes=5
response = client.select_items_data(ids = [item_id], not_before = from_date, before = datetime.today())
df = response.result.data.to_pandas().drop_duplicates()

print(df)
orchest.output((df), name = "response")

print("Success!")