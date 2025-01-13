from Remote import Remote, REMOTE_TYPES
import json

benny = Remote(name="Benny", current_type=REMOTE_TYPES.CAMERA)
data = {}
benny.addToJSON(data)
json_object = json.dumps(data)
print(json_object)
