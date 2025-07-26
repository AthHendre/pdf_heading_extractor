# PDF Heading Extractor

Extract hierarchical headings (main, sub, and sub-sub) from a structured PDF using Python and regular expressions.  
⚠️ No LLMs are used — this project showcases classical text processing + engineering skills.

---

## 🧠 Key Features

- 📌 Identifies **main headings** (e.g. `SECTION 4    VOLTAGE DROP`)
- 📎 Captures **subheadings** like `4.3` and `4.3.3` using regex patterns
- 🧹 Removes repetitive headers/footers via frequency-based similarity search
- 🧱 Outputs a **structured JSON hierarchy** of the document

---

## 📂 Project Structure

