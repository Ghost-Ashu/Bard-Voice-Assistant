<h1 align="center">Bard Voice Assistant Web Application😃</h1>


  <div style="position:relative;width:fit-content;height:fit-content;">
            <a style="position:absolute;top:20px;right:1rem;opacity:0.8;" href="https://clipchamp.com/watch/f3upHwgtMNk?utm_source=embed&utm_medium=embed&utm_campaign=watch">
                <img style="height:22px;" src="https://clipchamp.com/e.svg" alt="Made with Clipchamp" />
            </a>
            <iframe allow="autoplay;" allowfullscreen style="border:none" src="https://clipchamp.com/watch/f3upHwgtMNk/embed" width="640" height="360"></iframe>
        </div>


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
