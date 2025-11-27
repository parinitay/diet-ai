🥗 AI Diet Recommender

An AI-powered offline diet planning app that generates personalized meal plans using LangChain + Ollama (llama3) through a clean Streamlit UI.

🚀 Features

Personalized diet plan generation

Fully offline (local LLM via Ollama)

LangChain LCEL for prompt → model chaining

No API keys required

Simple Streamlit interface

🧠 Tech Stack
Tool	Purpose
Streamlit	Frontend UI
LangChain	Prompt templates + chaining
LCEL	Connects prompts to LLM
Ollama	Local LLM runner
llama3	LLM used
Python	Backend logic


📁 Project Structure

```bash
📁 diet-app/
├── app.py
├── generate_diet.py
└── requirements.txt
```


🖥️ Setup Instructions (Fully Offline)
✅ Step 1: Clone the Repository

```bash
git clone https://github.com/parinitay/diet-ai

```

```bash
cd diet-app

```




✅ Step 2: Create a Virtual Environment
Windows:

```bash
python -m venv venv
```


```bash
venv\Scripts\activate
```


Mac/Linux:

```bash
python3 -m venv venv
```


```bash
source venv/bin/activate
```



✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```



requirements.txt contains:

streamlit
langchain
langchain-core
langchain-community
langchain-ollama

✅ Step 4: Install Llama3 via Ollama

```bash
ollama pull llama3
```


✅ Step 5: Run the App

```bash
streamlit run app.py
```



Open in your browser at:

```bash
[streamlit run app.py](http://localhost:8501)
```


![Screenshot 2025-07-10 110123](https://github.com/user-attachments/assets/cdf150ce-7b13-4ad7-ad8e-e1a635051400)


![Screenshot 2025-07-10 110146](https://github.com/user-attachments/assets/b2fb1e60-0957-4931-9a29-b3daa5b91765)

![Screenshot 2025-07-10 110208](https://github.com/user-attachments/assets/8d3fa3c9-188b-43fd-b518-eb4438db6a2a)



