# Deploying Python API with Dash App

Welcome to our first API in Python, deployed with a Dash app! Explore the project by checking out the following files:

- `my_api.py` in the `scripts` folder contains the core of our API.
- `app.py` showcases the implementation of the Dash app.

To get started, replace the placeholder `IMDB_KEY` in `app.py` with your IMDb account API key if you wish to use our API. Don't worry; it's easy to obtain one from the IMDb website.

After updating the IMDb key, run the following command:

```bash
python app.py
```

You'll see a message like this:

```bash
 * Running on http://127.0.0.1:8050/
```

Follow the provided URL in your web browser, and you should encounter the Dash app interface.

![image](https://user-images.githubusercontent.com/119404054/205507975-9faa8965-ec58-41e5-a186-ff17bb1ad20b.png)

Congratulations! You've successfully deployed a Dash app with your API. Feel free to explore the app and interact with the provided features.

If you want to make changes to the API functionality, head to `my_api.py` and customize it to suit your needs. Once you're satisfied with the modifications, deploy your updated app to the web.

To deploy to the web, consider using platforms like Heroku, AWS, or others that support Dash applications. Refer to their documentation for deployment instructions.

Happy coding! If you have any questions or encounter issues, don't hesitate to reach out and make this project your own.
