import orchest
from pyclarify import ClarifyClient
from datetime import datetime, timedelta
import os

print("Getting data from Clarify")

item_id = orchest.get_step_param("item_id")

res = {}
credentials = os.environ["credentials"]
client = ClarifyClient(credentials)

ts_start = orchest.get_step_param("ts_start")
get_all_data = orchest.get_step_param("get_all_data")

if get_all_data:
    response = client.select_items_data(ids = [item_id], not_before = ts_start, before = datetime.today())
    print(response)
    orchest.output((response.json()), name = "response")

else:
    orchest.output(("None"), name = "response")
# Store data on disk
# with open("data/response.json", "w") as f:
#    f.write(response.json())
