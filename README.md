
# 🕵️‍♂️ Encrypted LSB Steganography

A Python project to **hide encrypted text inside an image** using the **Least Significant Bit (LSB) technique** combined with **XOR encryption**. This project ensures both **security** (via encryption) and **stealth** (via steganography).

---

## 📌 Features

- Encrypt text using a custom XOR key.
- Embed encrypted data into PNG images using LSB steganography.
- Decode and decrypt the hidden message from the image.
- Simple command-line interface.
- Lightweight and easy to use.

---

## 📂 Project Structure

```
encrypted_lsb_steganography/
├── main.py                 # Entry point script for the CLI
├── stego_utils.py          # Core encryption and steganography logic
├── example_input.png       # Sample image to test hiding text
├── encoded_image.png       # Output image with hidden data
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🛠️ Requirements

- Python 3.8 or higher

### 📦 Libraries

Install the required libraries:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
Pillow
```

---

## 🚀 How to Use

### ▶️ Hide Text in Image

```bash
python main.py
```

Enter:
- Image path (e.g., `example_input.png`)
- Secret message (e.g., `This is top secret!`)
- XOR key (e.g., `pass123`)
- Output path (e.g., `encoded_image.png`)
- Choose: [1] to hide the data

### 🔍 Reveal Hidden Text

```bash
python main.py
```

Enter:
- Encoded image path (e.g., `encoded_image.png`)
- XOR key (same used while encoding)
- Choose: [2] to extract the data

---

## 🔐 How It Works

- **XOR Encryption:** The input message is encrypted using a repeating key XOR cipher.
- **Binary Conversion:** The encrypted message is converted into a binary stream.
- **LSB Embedding:** Each bit is hidden in the least significant bit of each RGB channel in the image.
- **Extraction:** LSBs are read from the image to rebuild the binary string and decrypt the message using the same key.

---

## 🧪 Example

- Input Image: `example_input.png`
- Message: `The password is swordfish`
- Key: `abc123`
- Output: `encoded_image.png` *(looks identical but contains hidden message)*

---

## 📌 Notes

- Use **lossless** formats like `.png` to avoid data corruption.
- Ensure the image is large enough to hide the full message.
- The encryption key must match during encode and decode.

---

## 📚 References

- [Wikipedia - LSB Steganography](https://en.wikipedia.org/wiki/Steganography#Digital_steganography)
- [Pillow Library Docs](https://pillow.readthedocs.io/)

---

## 📃 License

MIT License © 2025

---

## 👩‍💻 Author

Made with 💻 by Gunika Tyagi

