# Failures #

### Example1 ###
- This example is a counter example to the successful [example1.](../successes/example1) The URL information is not decoded, but it is still put into immediate use in document.write(). If the user inputs special characters, they will be properly escaped and the attempt will fail.
- However, if the user is using a browser that is old enough to not support URL encoding (percent-encoding), then this attempt will work.
- There is also still the potential of a malicious payload being used as input that does not possess special characters, which would also work in this situation.

### Example2 ###
- This example is a counter example to the successful [example2.](../successes/example2) The URL information here is also not decoded, and document.location is immediately trusted and used as a variable without being properly filtered. However, like the previous example, due to modern browsers this attempt will still fail due to URL encoding.
- On an older browser, this will work.
