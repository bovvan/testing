import json

x = {
	"name": {
		"givenName": "hugo",
		"lastName": "bouvier"
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