
<h1 align="center" id="title">SciNanoAI</h1>

<p id="description">SciNanoAI</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repo:

```bash
git clone git@github.com:VinaVolo/SciNanoAI.git
```
<p>2. Create a virtual environment and install the necessary libraries </p>

- For Linux/MacOS system:
  ```bash
  uv sync
  ```

<p>3. Download data and vectore store from S3 bucket</p>
	
- Create a file .env according to the following template and insert the access keys
  ```bash
	S3_ACCESS_KEY=
	S3_SECRET_KEY=
	OPENAI_API_KEY=
	OPENAI_API_BASE=
	YANDEX_API_KEY=
	YANDEX_API_BASE=
	SBER_API_KEY=
	username=
	password=
  ```

- To download data from S3 bucket, run
  ```bash
	python download_data.py
  ```
  
- To download vector store from S3 bucket, run
  ```bash
	python download_db.py
  ```

<h2>💻 Built with</h2>

*  Run the vector database service. To do this, go to the **vector_service** folder and run the command from root dir:
      ```bash
      uvicorn vector_service.main:app --host 0.0.0.0 --port 8000
      ```

*  Run the chatbot. To do this, go to the **chatbot_app** folder and run the command from root dir:
	```bash
      uvicorn chatbot_app.main:app --host 0.0.0.0 --port 8001
   ```
* To launch the application, go to the chatbot_app folder and run:
	```bash
	python app.py
	```
To access the web interface, open a browser and go to: http://localhost:8517 . Log in using the username and password from the .env file.
