
# Streamlit App - How to deploy it locally

The app is located within the `streamlit-app` folder and is named `app.py`.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Streamlit


Install Streamlit using pip with the following command:

```bash
pip install streamlit
```

## Running the App

Follow these steps to run the app:

1. Open a terminal or command prompt.
2. Change directory to where `app.py` is located:



3. Execute the app with Streamlit:

```bash
streamlit run app.py
```

or alternatively

```bash
 python -m streamlit run test-app.py
 ```

Streamlit will start a server, and you should see the following:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

4. Open a browser and navigate to `http://localhost:8501` to view the app.

## Stopping the App

To stop the app, return to the terminal and press `Ctrl + C`.

## Troubleshooting
If you encounter any issues:

- Confirm app.py resides within the streamlit-app folder.
- Make sure you have installed all the necessary libraries. If you're unsure which libraries are needed, they are imported at the top of the app.py script. Install any that are missing using ```pip install library-name```.
- Make sure you're in the correct directory when running streamlit run app.py 