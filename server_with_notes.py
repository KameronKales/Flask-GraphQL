from flask import Flask
from flask import request
import graphene
import json

app = Flask(__name__)

'''When first setting up a new flask app make sure to export FLASK_APP=server file 
so you can run flask run'''

'''Below we are setting up our Query properties where we define what data we want to provide to the endpoint
and our return statement sends the information back to the client'''

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"),
    	age=graphene.Argument(graphene.Int))

    def resolve_hello(self, args, context, info):
        return 'Hello {} you are {} years old'.format(args['name'], args['age'])




schema = graphene.Schema(query=Query)
'''You can add more Schemas here and call the classes you created above to return the needed information
test = graphene.Schema(query=Query)

## You must also switch line 41 where it returns json dumps with test.execute. This variable must match 
the above defined variable such as test. '''

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
	return json.dumps(test.execute(data['query']).data)

