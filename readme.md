# Theorem of the day email

tiny script that emails you the day's Theorem of the Day (https://www.theoremoftheday.org/) every morning w/githun actions.

Instructions:

1. Fork/clone this
2. activate on 2FA for your Google account and make a Gmail App Password.
3. In your repo, go to **Settings → Secrets and variables → Actions**.
4. Add:

   * `GMAIL_ADDRESS`
   * `GMAIL_APP_PASSWORD`
5. edit `.github/workflows/daily.yml` if you want to change what time it runs.
6. Go to **Actions → Daily Theorem Email → Run workflow** to test it.

That's it. GitHub will run it every day without your computer needing to be on.

Do not commit your Gmail address/password directly into the code!
