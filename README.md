# CMPUT404-lab_1

Question 1: What is your GitHub URL?
  ANS: https://github.com/Aden-Adar/CMPUT404-lab_1.git

Question 2: What version is the requests library installed on the system?
  ANS: 2.28.1
Question 3: What version is the requests library installed in the virtualenv?
  ANS: 2.28.0
Question 4: What is the difference between the virtual environment and the not virtual environment python?
  ANS: virtual environment is an isolated environments which only contain basic modules when first created. It allows you to hold modules of different version (compared to your system) for your project. Non virtual environment python is what the system uses to run modules.
Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?
  ANS: 301 Moved Permanently. The URL you must visit to get a 200 status code is http://www.google.com/
Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?
  ANS: For curl -i you get status code  301 and for curl -iL you get both 301 and 418 
Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?
  ANS: When I used -X POST the file specifies that the request method is post (as oppposed to get from file2.txt). Also, we can see the data passed ("X" and "Y"). Lastly, other fields were also different, such as date, unique id, content length, etc. This method allows you to send data to the webserver.
Question 8: What is the raw URL to your Python script on GitHub?
  ANS: https://raw.githubusercontent.com/Aden-Adar/CMPUT404-lab_1/main/lab1.py
