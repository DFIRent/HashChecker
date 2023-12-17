from py_essentials import hashing as hash
import os

def create_hash_file(hash_file):
    with open(hash_file, 'w'):
        pass

def create_hash(file_path):
    hash_result = hash.fileChecksum(file_path, "sha256")
    return hash_result

def store_hash(hash_file, hash_result):
    with open(hash_file, 'w') as store:
        store.write(hash_result)

def compare_hash(file_path, hash_file):
    with open(hash_file, 'r') as openhash:
        readhash = openhash.read().strip()

    current_hash = create_hash(file_path)

    if readhash == current_hash:
        print("SHA-256 hashes match!")
    elif readhash != hash:
        print("SHA-256 hashes DO NOT match!")
    else:
        print("Error")

if __name__ == '__main__':
    file_path = "testfile.txt" # file path to the file that will be checked
    hash_file = "hash.txt" # file to store the hash to be checked. delete the file if you want to create a new hash with a new file

    if not os.path.exists(hash_file):
        create_hash_file(hash_file)
        current_hash = create_hash(file_path)
        store_hash(hash_file, current_hash)
        print("hash.txt file has been created. Run the program again whenever to check the hash")
    elif os.path.exists(file_path):
        compare_hash(file_path, hash_file)
    else:
        print("File does not exist")


"""
decision = print(input("Would you like to make a hash or compare? (m/c): ").upper())

    if decision == "M":
        create_hash(file_path)
        store_hash(hash_file)
    elif decision == "C":
        create_hash(file_path)
        compare_hash(file_path, hash_file)
    else:
        print("Invalid response. Please type 'm' or 'c'")
"""

