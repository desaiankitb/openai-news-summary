openai-news-summary
==============================

News to summary using openai

The main functionality is separated into two files: `main.py` and `news_cms_parser.py`.

The `main.py` file serves as the entry point. It imports the `NewsCMSParser` class from the `news_cms_parser.py` module. It also uses the argparse module to parse command-line arguments, specifically the `--url` argument, which is required to specify the URL to parse. The main function is responsible for calling the `NewsCMSParser` class and printing the results.

The `news_cms_parser.py` file contains the `NewsCMSParser` class, which encapsulates the URL cleaning and content extraction functionalities, as explained in the previous example.

To run the code, you can execute the main.py file and pass the URL as a command-line argument. For example:

Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

Run the app:
    ```bash 
    $ python main.py --url https://www.example.com/news/article?param1=value1&param2=value2
    ```