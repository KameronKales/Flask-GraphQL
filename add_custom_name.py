import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"),
    	age=graphene.Argument(graphene.Int))

    def resolve_hello(self, args, context, info):
        return 'Hello {} you are {} years old'.format(args['name'], args['age'])
def main():
	schema = graphene.Schema(query=Query)
	result = schema.execute('{ hello(name:"Kameron", age:13) }')
	print result.data['hello'] # "Hello stranger"

if __name__ == '__main__':
	main()
