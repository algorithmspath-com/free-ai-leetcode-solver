# Setup Guide for Free AI LeetCode Solver - Windows
This guide will help you set up and use the Free AI LeetCode Solver with ease. Follow the instructions to get everything running smoothly.

## Clone the repo:

```bash
git clone https://github.com/algorithmspath-com/free-ai-leetcode-solver.git
cd free-ai-leetcode-solver
```

## Directory Structure

Make sure your project directory is structured as follows:

```
windows/
    ├── AssistServer/                   # Backend engine
    ├── Tesseract/                      # OCR magic
    └── free-ai-leetcode-solver.exe      # Launcher
config.py                               # Configuration file
```

## Step 1: Define the Configuration File

Create a `config.py` file in the root of your project directory with the following content:

```python
{
  "openai_api_key": "my_openai_api_key",  # Replace with your OpenAI API key
  "tesseract_cmd": "C:/Tesseract/tesseract.exe",  # Path to the Tesseract executable
  "host": "0.0.0.0",  # Host for the FastAPI server
  "port": 10010  # Port for the FastAPI server
}
```

### Notes:
- Make sure to replace `"my_openai_api_key"` with your actual OpenAI API key.
- Ensure that the path to `tesseract.exe` is correct based on your Tesseract installation.

## Step 2: Start the Backend Server

To start the backend engine:

1. Navigate to the `AssistServer` directory in your terminal or command prompt.
2. Execute the following command:

   ```bash
   path_of_AssistServer.exe path_of_config.py
   ```

This command launches the FastAPI server which will handle the requests from the client.

## Step 3: Start the Client Application

After the server is running, you can launch the client:

1. Run the `free-ai-leetcode-solver.exe` by double-clicking it or using the command prompt.

## Step 4: Usage Instructions

Once both the server and client are running, you can use the application with the following keyboard shortcuts:

- **Ctrl + H**: Capture a screenshot.
- **Ctrl + Enter**: Send the captured image to the AI for solving.
- **Ctrl + R**: Reset the current state.

## Troubleshooting

- If the server does not start, ensure the port is not blocked or used by another application.
- If screenshots do not work, verify that Tesseract is properly installed and the path in the `config.py` is correct.
- Reach out to support@algorithmspath.com for any questions!

---

By following the above steps, you should be able to set up and use the Free AI LeetCode Solver without issues. Happy coding!
