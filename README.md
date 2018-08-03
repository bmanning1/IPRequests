# IPRequests
This code is meant to be generic however the idea and main purpose of creation was for a challenge on OWASP Juice Shop (see the section at the bottom of this page).

### Purpose
This code does 2 main things:
1. Creates a list of all mutations of a given word
    - lower case (a-z)
    - upper case (A-Z)
    - leet speech (h3110)
2. Brute Force - Sends requests (based on the config) with each word created in 1. along with a different X-Forwarded-For-header to bypass rate limiting.

### Config
The config file makes this code easily reusable. Just replace each value to make in unique to the requests you want.

```{
    "word": "snowball",
    "payloadValueReplace": "answer",
    "url": "http://localhost:3000/rest/user/reset-password",
    "payload": {
        "email": "morty@juice-sh.op",
        "answer": "",
        "new": "morty01",
        "repeat": "morty01"
    }
}
```

| Config              | Description                                                              |
|---------------------|--------------------------------------------------------------------------|
| word                | word to create word list from                                            |
| payloadValueReplace | field in payload to put each word from the word list in for each request |
| url                 | post to this url on each request |
| payload             | request body to post with for each request (it doesn't matter what you put in the value of the field being replaced) | 


### OWASP Juice Shop Challenge - *Reset Morty's password via the Forgot Password mechanism*
- Trying to find out who "Morty" might be should eventually lead you to Morty Smith as the most likely user identity
Morty Smith

- Visit http://rickandmorty.wikia.com/wiki/Morty and skim through the Family section
- It tells you that Morty had a dog named Snuffles which also goes by the alias of Snowball for a while.
- Visit http://localhost:3000/#/forgot-password and provide morty@juice-sh.op as your Email
- Create a word list of all mutations (including typical "leet-speak"-variations!) of the strings snuffles and snowball using only
  - lower case (a-z)
  - upper case (A-Z)
  - digit characters (0-9)
- Write a script that iterates over the word list and sends well-formed requests to http://localhost:3000/rest/user/reset-password. A rate limiting mechanism will prevent you from sending more than 100 requests within 5 minutes, severely hampering your brute force attack.
- Change your script so that it provides a different X-Forwarded-For-header in each request, as this takes precedence over the client IP in determining the origin of a request.
- Rerun your script you will notice at some point that the answer to the security question is 5N0wb41L and the challenge is marked as solved.
