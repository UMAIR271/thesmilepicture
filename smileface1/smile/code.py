import uuid 

def generate_code():
    code = str(uuid.uuid4()).replace("-","")[:12]
    print(code)
    return code