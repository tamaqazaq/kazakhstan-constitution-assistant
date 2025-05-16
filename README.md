# Kazakhstan Constitution Assistant

This project is an AI assistant built using Streamlit and Ollama that allows users to ask questions related to the Constitution of Kazakhstan. The assistant processes the Constitution's text and generates responses based on its content.

## Usage

1. Clone the repository:
   git clone https://github.com/tamaqazaq/kazakhstan-constitution-assistant.git
   cd kazakhstan-constitution-assistant

2. Install dependencies:
   python -m venv venv
   source venv/bin/activate        (macOS/Linux)
   venv\Scripts\activate           (Windows)
   pip install -r requirements.txt

3. Make sure the file konstitutsiya_kz.json is in the project folder.

4. Run the app:
   streamlit run app.py

5. Open http://localhost:8501 in your browser.

6. Ask questions like:
   - What does the Constitution of Kazakhstan say about human rights?
   - In which chapter of the Constitution of Kazakhstan is the right to work discussed?

The assistant will find relevant content and answer based on the document.

## Demo Screenshot

[Insert demo.png](screenshots/demo.png)

## Examples

- What are the human rights guaranteed by the Constitution of Kazakhstan?
- How does the Constitution define the structure of government?
- What are the duties of citizens?

## License

This project is licensed under the MIT License. See LICENSE file.  
Reference: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/LICENSE
