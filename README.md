Python script that takes the link of an application from linkedin's jobs screen (as of March 23) and writes that info to an excel document to track your applications.

FOR SCRIPT TO WORK:

1. You either have to submit link BEFORE applying. If you want to submit AFTER applying, you simply need to click another job in the list on linkedin, then click back onto the job you just applied to. This resets to link to the correct format.

2. You will need to create an env file in the same directory as this called "secrets.env",
   secrets.env will need to contain:
   USERNME="yourusernamehere"
   PASSWORD="yourpasswordhere"
