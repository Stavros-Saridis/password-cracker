import hashlib

SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def hash_password(password, algorithm='sha256'):
    algorithm = algorithm.lower()
    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    h = hashlib.new(algorithm)
    h.update(password.encode('utf-8'))
    return h.hexdigest()

def identify_hash(hash_string):
    length_map = {
        32: 'md5',
        40: 'sha1',
        56: 'sha224',
        64: 'sha256',
        96: 'sha384',
        128: 'sha512'
    }
    return length_map.get(len(hash_string), 'unknown')

def hash_file(filepath, algorithm='sha256'):
    h = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None