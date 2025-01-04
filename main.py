from flask import Flask, render_template, request, jsonify
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(text):
    if not text:
        return None
    frequency = Counter(text)
    nodes = [Node(char, freq) for char, freq in frequency.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left, merged_node.right = left, right
        nodes.append(merged_node)
    return nodes[0]

def huffman_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    huffman_codes(node.left, current_code + '0', codes)
    huffman_codes(node.right, current_code + '1', codes)

def compress(text, codes):
    return ''.join(codes[char] for char in text)

def decompress(compressed_text, root):
    if root is None:
        return ""
    current_node = root
    decompressed_text = ""
    for bit in compressed_text:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decompressed_text += current_node.char
            current_node = root
    return decompressed_text

def huffman_compress(text):
    root = huffman_tree(text)
    if root is None:
        return "", None, {}
    codes = {}
    huffman_codes(root, '', codes)
    compressed_text = compress(text, codes)
    return compressed_text, root, codes

def huffman_decompress(compressed_text, root):
    return decompress(compressed_text, root)

app = Flask(__name__)

compressed_text = None
huffman_tree_root = None
codes = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_route():
    global compressed_text, huffman_tree_root, codes
    text = request.form.get('text', '').strip()
    if not text:
        return jsonify({"error": "Input text cannot be empty."}), 400

    compressed_text, huffman_tree_root, codes = huffman_compress(text)
    if not compressed_text:
        return jsonify({"error": "Compression failed."}), 500

    return jsonify({
        "compressed_text": compressed_text,
        "compressed_length": len(compressed_text)
    })

@app.route('/decompress', methods=['POST'])
def decompress_route():
    global compressed_text, huffman_tree_root

    if not compressed_text or not huffman_tree_root:
        return jsonify({"error": "No compressed text available."}), 400

    decompressed_text = huffman_decompress(compressed_text, huffman_tree_root)
    return jsonify({
        "decompressed_text": decompressed_text,
        "decompressed_length": len(decompressed_text)
    })

if __name__ == '__main__':
    app.run(debug=True)
