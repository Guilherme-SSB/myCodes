from hashlib import sha256
import time

def apply_sha256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mining(num_block, transactions, previous_hash, num_zeros):
    nonce = 0
    while True:
        text = str(num_block) + transactions + previous_hash + str(nonce)
        my_hash = apply_sha256(text=text)
        if my_hash.startswith(num_zeros * "0"):
            return nonce, my_hash
        nonce += 1

if __name__ == "__main__":
    num_block = 15
    transactions = """
    guilherme->gustavo->10
    gustavo->doctor->200
    doctor->engineering->2000
    """
    previous_hash = "abc"
    num_zeros = 6
    
    t0 = time.time()
    result = mining(num_block, transactions, previous_hash, num_zeros)
    print(result)
    print(round(time.time()-t0, 2))
