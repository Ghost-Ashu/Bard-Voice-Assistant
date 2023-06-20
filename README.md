<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bard Assistant Web Application</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.5;
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    p {
      text-align: center;
    }

    img {
      display: block;
      margin: 0 auto;
      margin-top: 20px;
      margin-bottom: 20px;
    }

    ol {
      padding-left: 20px;
    }

    code {
      background-color: #f4f4f4;
      padding: 4px;
    }

    a {
      color: #0366d6;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }
  </style>
</head>

<body>
  <h1>Bard Assistant Web Application 😃</h1>

  <p>
    <img src="https://your-image-url.com/your-logo.png" alt="Logo" width="200" height="200">
  </p>

  <p><strong>A Flask web application that provides a user interface to interact with a chatbot.</strong></p>

  <p>
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#license">License</a>
  </p>

  <h2 id="installation">Installation</h2>

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

  <h2 id="usage">Usage</h2>

  <ul>
    <li><strong>Text Input:</strong> Type your message in the input field and press Enter or click the "Send" button. The chatbot will respond accordingly.</li>
    <li><strong>Speech Input:</strong> Click the "Listen" button and speak your prompt to the chatbot. It will transcribe your speech, send it to the chatbot, and provide a spoken response.</li>
    <li><strong>Speech Output:</strong> Enter your prompt in the input field and click the "Speak" button. The chatbot's response will be spoken aloud.</li>
  </ul>

  <h2 id="license">License</h2>

  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>

</html>
