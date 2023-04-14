def reverse(body):
    if 'string' not in body:
        return {'error': 'string is required'}, 400
    return {'string': body['string'][::-1]}