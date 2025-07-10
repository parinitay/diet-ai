🥗 AI Diet Recommender –
An AI-powered app that generates personalized diet plans based on user attributes like age, gender, body composition, and activity level.

This was built using:

🧠 LangChain: For structured prompt templates and chaining logic

🤖 Ollama (local LLM): Running Meta’s llama3 model

💻 Streamlit: For the user interface

🔁 LangChain LCEL: To connect prompts to models seamlessly


💡 What the App Does
Users enter:

Age

Gender

Body type (Lean, Overweight, etc.)

Activity level (Sedentary, Active, etc.)

Click a button → the app generates a detailed AI-powered diet plan using a locally running LLM via LangChain + Ollama. No cloud API keys needed 


🧠 Tech Stack
Tool	Purpose
Streamlit	Frontend UI
LangChain	PromptTemplate + LCEL chaining
Ollama	Local LLM runner
llama3	Language model
Python	Backend logic


📁 Project Structure
bash
Copy
Edit
📁 diet-app/
├── app.py                # Streamlit frontend
├── generate_diet.py      # LangChain + LLM backend logic
└── requirements.txt      # Install dependencies


🖥️ Setup Instructions (Works Fully Offline)

✅ Step 1: Clone or Download
bash
Copy
Edit
git clone https://github.com/yourusername/diet-app
cd diet-app

✅ Step 2: Create a Virtual Environment (Optional but clean)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux

✅ Step 3: Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt contains:

nginx
Copy
Edit
streamlit
langchain
langchain-core
langchain-community
langchain-ollama

✅ Step 4: Install Llama3 via Ollama
If you haven't already:

bash
Copy
Edit
ollama pull llama3
Make sure Ollama is installed. Download from https://ollama.com

✅ Step 5: Run the App!
bash
Copy
Edit
streamlit run app.py

open in your browswer
http://localhost:8501

![Screenshot 2025-07-10 110123](https://github.com/user-attachments/assets/cdf150ce-7b13-4ad7-ad8e-e1a635051400)


![Screenshot 2025-07-10 110146](https://github.com/user-attachments/assets/b2fb1e60-0957-4931-9a29-b3daa5b91765)

![Screenshot 2025-07-10 110208](https://github.com/user-attachments/assets/8d3fa3c9-188b-43fd-b518-eb4438db6a2a)



