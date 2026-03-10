from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: \
{encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: \
{decrypted_text}"

# Route hiển thị trang Vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

# Route xử lý mã hóa Vigenere
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    # Giả sử bạn có class VigenereCipher trong cipher/vigenere.py
    # from cipher.vigenere import VigenereCipher
    # cipher = VigenereCipher()
    # encrypted_text = cipher.encrypt(text, key)
    return f"Vigenere Encrypt - Text: {text}, Key: {key}"

# Route xử lý giải mã Vigenere
@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    return f"Vigenere Decrypt - Text: {text}, Key: {key}"

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)