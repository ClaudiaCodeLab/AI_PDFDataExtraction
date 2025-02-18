# Bank Loan Application Data Extraction with LLM

This Streamlit application extracts customer data from bank loan application PDFs using OpenAI's language model and Langchain.

---

## **Project Structure**

- `app.py`: Main Streamlit application code.
- `requirements.txt`: List of dependencies.

---

## **Setup Instructions**

### 1. Clone the repository:
```bash
git clone https://github.com/claudiacodelab/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file for your OpenAI API key:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## **Run the Application**

```bash
streamlit run app.py
```

---

## **Deployment to Streamlit Cloud**

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy your repository.
3. In Streamlit Cloud, set your API key in the `Secrets` section as:
   ```
   OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

---

## **License**
This project is licensed under the MIT License.

---

### **Contributions**
Feel free to submit issues or pull requests for improvements!

---

*Happy coding! 🚀*
