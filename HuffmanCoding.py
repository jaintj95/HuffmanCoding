import sys
import heapq
from collections import Counter


class BinaryNode:
    def __init__(self, char, freq):
        self.left = None
        self.right = None
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, BinaryNode)):
            return -1
        return self.freq < other.freq


def huffman_encoding(data):
    
    if data == "":
        return None, None

    # data = data.lower()
    data_dict = Counter(data)

    freqs = []
    for (key,value) in data_dict.items():
        node = BinaryNode(key, value)
        heapq.heappush(freqs, node)

    if len(freqs) == 1:
        node = heapq.heappop(freqs)
        root = BinaryNode(node.char, node.freq)
        root.left = node
        heapq.heappush(freqs, root)

    # generate huffman tree
    while len(freqs) > 1:
        node1 = heapq.heappop(freqs)
        node2 = heapq.heappop(freqs)
        mergedNode = BinaryNode(None, node1.freq + node2.freq)
        mergedNode.left = node1
        mergedNode.right = node2
        heapq.heappush(freqs, mergedNode)

    # encoding begins here
    tree = heapq.heappop(freqs)

    encoding_dict = generate_code(tree, "")
    encoded_data = encode(data, encoding_dict)
    #encoded_data = int(encoded_data)
    return encoded_data, tree

def generate_code(node, encoding):

    encoding_map = {}

    if node is None:
        return {}

    if node.char is not None:
        encoding_map[node.char] = encoding

    encoding_map.update(generate_code(node.left, encoding + "0"))
    encoding_map.update(generate_code(node.right, encoding + "1"))

    return encoding_map


def encode(data, encoding_dict):
    output = ''

    for char in data:
        output += encoding_dict[char]

    return output


def huffman_decoding(data,tree):
    node = tree
    decoded_data = ""

    if data == "":
        return ""

    for bit in data:
        
        if bit == '0':
            node = node.left

        elif bit == '1':
            node = node.right

        if node.char is not None:
            decoded_data += node.char
            node = tree 

    return decoded_data


if __name__ == "__main__":
    codes = {}

    print("\nTest Case 1: Default string\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data is None:
        print("Empty sentence cannot be encoded\n")
        
    else:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))

    # empty string
    print("\nTest Case 2: Empty String\n")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)
    if encoded_data is None:
        print("Empty sentence cannot be encoded\n")
        
    else:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))


    print("\nTest Case 3: Same chars\n")
    a_great_sentence = "TTTTT"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data is None:
        print("Empty sentence cannot be encoded\n")
        
    else:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))