<h1 align="center">Bard Assistant Web Application 😃</h1>

<p align="center">
  <img src="https://your-image-url.com/your-logo.png" alt="Logo" width="200" height="200">
</p>

<p align="center">
  <strong>A Flask web application that provides a user interface to interact with a chatbot.</strong>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

## Installation

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/your-username/your-repository.git
    cd your-repository</code></pre>
  </li>
  
  <li>Create a virtual environment (optional but recommended):
    <pre><code>python3 -m venv venv
    source venv/bin/activate</code></pre>
  </li>
  
  <li>Install the dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  
  <li>Obtain a Bard Token:
    <ul>
      <li>Sign up on the <a href="https://www.bard.ai/">Bard</a> website to get an API token.</li>
      <li>Replace the <code>token</code> variable in <code>app.py</code> with your token.</li>
    </ul>
  </li>
  
  <li>Download Whisper models:
    <ul>
      <li>Download the <code>tiny</code> and <code>base</code> models from the <a href="https://github.com/snakers4/whisper">Whisper</a> repository.</li>
      <li>Place the models in the same directory as <code>app.py</code>.</li>
    </ul>
  </li>
  
  <li>Run the application:
    <pre><code>python app.py</code></pre>
  </li>
  
  <li>Open your web browser and visit <code>http://localhost:5000</code> to access the chatbot interface.</li>
</ol>

## Usage

- Enter text input: Type your message in the input field and press Enter or click the "Send" button. The chatbot will respond accordingly.
- Speech input: Click the "Listen" button and speak your prompt to the chatbot. It will transcribe your speech, send it to the chatbot, and provide a spoken response.
- Speech output: Enter your prompt in the input field and click the "Speak" button. The chatbot's response will be spoken aloud.

## License

This project is licensed under the <a href="LICENSE">MIT License</a>.
