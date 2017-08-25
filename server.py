from flask import Flask
from flask import request
import graphene
import json

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"),
    	age=graphene.Argument(graphene.Int))

    def resolve_hello(self, args, context, info):
        return 'Hello {} you are {} years old'.format(args['name'], args['age'])


schema = graphene.Schema(query=Query)


## To test this route:
## Run server with flask run 
## Open postman and hit the route with json
'''
{
	"query": "{hello (name: \"Kameron\" age:13)}"
}'''

@app.route("/graphql", methods=['POST'])
def graphql():
	data = json.loads(request.data)
	return json.dumps(schema.execute(data['query']).data)

