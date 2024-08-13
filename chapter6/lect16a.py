# function arguments
def print_info(**args):
    if 'age' in args:
        print(f"Hi, my name is {args.get('n')}, age is {args['a']} ")
    else:
        print('you must provide age value!')

print_info(a= 20, n = "Hossam",s="CS")