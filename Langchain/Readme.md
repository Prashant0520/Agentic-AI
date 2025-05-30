# Product Details AI Assistant

**Product Details AI Assistant** is a powerful AI-driven tool that extracts structured product information—such as name, description, and estimated price—based on a natural language product query. It leverages the `gemma2-9b-it` model via the GROQ API for fast and intelligent responses, and features a UI built on **Streamlit** and **Chainlit**.

## 🔧 Tech Stack

-  **LLM**: [`gemma2-9b-it`](https://groq.com) (via GROQ API)
-  **Pydantic**: For JSON validation
-  **LangChain**: For chaining prompts, models, and parsing
-  **UI Frameworks**: 
  - [Streamlit](https://streamlit.io/)
  - [Chainlit](https://www.chainlit.io/)

## 🚀 Getting Started

Follow the steps below to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Prashant0520/Agentic-AI.git
```

### 2. Change Directory
```bash
cd Langchain/
```

### 3. Create a Virtual Environment using Conda
```bash
conda create -n agentic_ai python==3.12 -y
```

### 4. Activate the Environment
#### Windows/macOS/Linux:
```bash
conda activate agentic_ai
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit App
```bash
streamlit run langchain_streamlit.py
```

### 7. Run the Chainlit App
```bash
chainlit run langchain_chainlit.py -w
```

## 📦 Output Schema

| Field           | Type    | Description                   |
|-----------------|---------|-------------------------------|
| product_name    | string  | The product's name            |
| details         | string  | Description of the product    |
| price           | integer | Tentative price in USD        |


## 🖥️ UI Previews

### Streamlit UI
![Streamlit UI](https://github.com/user-attachments/assets/ec27acd5-c3cf-4742-b1d3-9348a28a5bbe)

### Chainlit UI
![Chainlit UI](https://github.com/user-attachments/assets/62cf6198-fe2f-490c-8a8d-183373c37e71)
