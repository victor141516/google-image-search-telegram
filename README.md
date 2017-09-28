# Google Image search Telegram inline bot


This bot is just like @bing but using Google Images as backend

# Install instructions
##### First you need some Google search keys

1. Go to https://console.developers.google.com and make a new project.
2. Go to `Library`, enable `Custom Search API` and make a new credential using the button you will be prompted
3. Copy your API key `[CSE_KEY]`


1. From the Google Custom Search homepage ( http://www.google.com/cse/ ), click Create a Custom Search Engine.
2. Type a name and description for your search engine.
3. Under Define your search engine, in the Sites to Search box, enter at least one valid URL (For now, just put www.anyurl.com to get past this screen. More on this later ).
4. Select the CSE edition you want and accept the Terms of Service, then click Next. Select the layout option you want, and then click Next.
5. Click any of the links under the Next steps section to navigate to your Control panel.
6. In the left-hand menu, under Control Panel, click Basics.
7. In the Search Preferences section, select Search the entire web but emphasize included sites.
8. Click Save Changes.
9. In the left-hand menu, under Control Panel, click Sites.
10. Delete the site you entered during the initial setup process.
11. Copy your `Search engine ID` using the button for this purpose `[CSE_CX]`.

##### Then your Telegram Bot API key
1. Talk to @botfather using your Telegram account and he will give you your fresh new API key. `[API_TOKEN]`
2. Copy your bot nickname `[BOT_NAME]`.
3. This is that easy

##### Deploy environment
I deploy my Telegram bots using Heroku, so this part will be based on this service but you can use any other if you know how to deploy a webapp using Flask

1. Make a new Heroku app and copy its URL `[WEBHOOK_URL]`
2. Copy the `config_example.py` file to `config.py` and place there all the vars you copied from previous steps: `[BOT_NAME, CSE_KEY, CSE_CX, API_TOKEN, BATCH, WEBHOOK_URL]`
3. Add this file to the repo: `git add config.py`
4. You will have to add all the Heroku related files: `app.json`, `Procfile`, `Procfile.windows`
5. Add them: `git add app.json Procfile Procfile.windows`
5. Commit and push it: `git commit -am "This is a push" && git push heroku master`
6. Done!