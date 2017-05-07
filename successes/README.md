# Successes #

### Example1 ###
- This example contains a vulnerability in which the developer grabs input from the URL that is posted to the "/newRedirect" route in Flask.
- Whatever input that is entered is then not sanitized and decoded. It is directly used in a document.write() statement. This allows for the user to run anything contained in "<script></script>" tags. The user can also inject their own HTML tags to render custom formatting on a page, which has no limitation.

### Example2 ###
- This example takes advantage of the document.location DOM node, which allows for the path of the web page to be returned. This, if user input is included in the URL path, can allow for DOM XSS. Like the previous example, the input is decoded and not sanitized at all, which allows raw input to be executed in a similar fashion to the previous example.
