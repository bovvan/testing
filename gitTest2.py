import json

x = {
	"name": {
		"givenName": "John",
		"lastName": "Doe"
			},
	"array": [
	{
	"test": "test"
	},
	{
	"test": "test"
	}
	]
}

indented = json.dumps(x, indent=2)


print (indented)