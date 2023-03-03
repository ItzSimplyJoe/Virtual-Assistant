# Virtual Assistant
![python image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
###### Virtual Assistant is a Python-based application that provides a conversational interface to perform various tasks. This project is built on the basis of natural language processing and machine learning.

## Installation
1. Clone the repository by running git clone `https://github.com/ItzSimplyJoe/Virtual-Assistant.git`
2. Change into the project directory by running cd Virtual-Assistant
3. Install the required dependencies by running `pip install -r requirements.txt`
## Usage
To start the virtual assistant, run python virtual_assistant.py in your terminal. This will open a command-line interface where you can interact with the virtual assistant.

## The virtual assistant can perform various tasks, including:

- Can answer questions about a wide range of topics.
- Can perform basic arithmetic calculations.
- Uses machine learning
- Can tell jokes
- Can tell you the weather
- Can create a personal profile
- Can tell the time
- Can tell you the date
- Can tell you the day of the week
- Can tell the user how to spell things
- Can theoretically control my light, but i moved house and havent set it up again
- Has half a quiz feature built in
- Has the ability to use several languages, such as French, Spanish, German, Italian, Chinese
- Has a shopping list that you can add things to
- Has a fully functional UI
- Has Voice control using the wakeword 'oi badger'
- Can speak and print responses back to you
- Can create a timer
- Can facilitate a friendly conversation
- Can Tell you where you are currently
- Can provide weather data about your current area
- Can use ChatGPT to do anything that you need.
- And more

## Configuration
The virtual assistant allows you to customise the project.

 - name: The name of your virtual assistant, this can be found in the `main.py` file
 - wake_words: A list of wake words that trigger the virtual assistant. This can be found inside of both the `voice.py` file and `assistant_functions/wakedetection.py`. You can simply train another wakeword here https://picovoice.ai/docs/quick-start/porcupine-python/ and then add that to the `Keywords` file and change the location inside of the `voice.py` file
 - colour of UIs: All colours can be changed in the program and they are saved per each user
 - Font in UIs: All fonts can be changed in the program and they are saved per each user
 - Voice of Virtual Assistant: All voices can be changed in the program and they are saved per each user
## Contribution Guidelines
If you would like to contribute to this project, please follow these guidelines:

 - Fork the repository and make your changes on a new branch.
 - Submit a pull request to have your changes reviewed and merged into the main branch.
 - Please ensure that your code is well-documented and follows PEP 8 style guidelines.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

If you have any questions or encounter any issues with this project, please feel free to create an issue on GitHub. Thank you for using Virtual Assistant!
