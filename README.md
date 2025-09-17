# Financial Document QA Application

A web application that processes financial documents (PDF and Excel) and provides an interactive question-answering system using natural language processing with local LLMs.

## Features

- **Document Processing**: Upload and extract data from PDF and Excel financial documents
- **Natural Language QA**: Ask questions about revenue, expenses, profits, and other financial metrics
- **Local LLM Integration**: Uses Ollama with local Small Language Models (no cloud required)
- **Interactive Web Interface**: Clean, intuitive Streamlit-based UI
- **Multi-format Support**: Handles various financial document layouts (Income statements, Balance sheets, Cash flow statements)

## Technology Stack

- **Frontend**: Streamlit
- **Document Processing**: PyPDF2, pdfplumber, pandas, openpyxl
- **NLP/LLM**: Ollama, LangChain
- **Backend**: Python 3.8+

## Prerequisites

- Python 3.8 or higher
- Ollama installed on your system

## Installation & Setup

### 1. Clone the Repository
### 2. Create Virtual Environment
### 3. Install Dependencies
### 4. Install and Setup Ollama

1. Download Ollama from [https://ollama.com/download](https://ollama.com/download)
2. Install the application
3. Download the LLM model: `ollama pull llama3`
## 💻 Usage

### Running the Application

1. Activate your virtual environment: .venv\Scripts\activate # Windows / source .venv/bin/activate # macOS/Linux
2. Start the Streamlit app: streamlit run app.py

3. Open your browser and navigate to the displayed URL (typically `http://localhost:8501`)

### Using the App

1. **Upload Documents**: Click "Browse files" and select your financial PDF or Excel files
2. **Wait for Processing**: The app will extract and process the document content
3. **Ask Questions**: Type natural language questions about the financial data
4. **Get Answers**: The local LLM will analyze the content and provide relevant answers

### Example Questions

- "What is the total revenue?"
- "Is the payment completed?"
- "What are the main expenses?"
- "Show me the profit margins"
- "When was this transaction made?"

## 🔧 Configuration

### Supported File Formats
- **PDF**: Financial statements, invoices, reports
- **Excel**: Spreadsheets with financial data (.xlsx format)

### Model Configuration
The app uses Ollama's `llama3` model by default. To use a different model:

1. Download the model: `ollama pull model-name`
2. Update `qa_engine.py` line with the new model name: `llm = Ollama(model="your-model-name")`

## 🐛 Troubleshooting

### Common Issues

**1. "ollama: command not found"**
- Ensure Ollama is installed and added to your system PATH
- Restart your terminal after installation

**2. "ModuleNotFoundError"**
- Make sure you've activated your virtual environment
- Install dependencies: `pip install -r requirements.txt`

**3. "Model not found"**
- Download the required model: `ollama pull llama3`

**4. Large file processing errors**
- Check file size limits (200MB per file in Streamlit)
- Ensure sufficient system memory for large documents



##  Author

**Adhitya Baskaran**
- GitHub: [@Adh1tya](https://github.com/Adh1tya)
- Email: adhityaramya12@gmail.com

---


