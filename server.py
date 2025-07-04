#! /usr/bin/env python3
from flask import Flask, request, make_response, render_template
from urllib.parse import urlparse

app = Flask(__name__)

#HOME
@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:center;">
<h1> Web Technology Practice </h1>
<p> There are <strong> five </strong> flags hidden on this website. Can you find them? </p>
<br>
<br>
<p> Some helpful tools may be: </p>
<ul> Dirb/Gobuster </ul>
<ul> curl </ul>
<ul> BurpSuite </ul> 
<ul> Browser Inspector </ul>
<! NOTE: Don't forget the /curl and /post pages..... -->     
</body>
</html>
    """
    # HTML comment added for flag 5
    resp = make_response(page)
    # Set cookie for flag 3
    resp.set_cookie('admin', 'false')
    return resp

# FLAG NUMBER ONE
# User can visit a common website page
@app.route('/robots.txt', methods=['GET'])
def robots():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:center;">
<h1> Web Technology Practice </h1>
<p> User-agent: * </p>
<p> Crawl-delay: 10 </p>
<p> flag{i_know_common_URIs} </P>
</html> 
    """
    return page

# FLAG NUMBER TWO:
# User can enumerate multiple webpages using Dirb/GoBuster
@app.route('/xls', methods=['GET'])
def xls():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:left;">
<h1> 1 </h1>
<p> flag{I </p>    
</body>
</html>
    """
    return page

@app.route('/.profile', methods=['GET'])
def profile():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:left;">
<h1> 2 </h1>
<p> _can </p>    
</body>
</html>
    """
    return page

@app.route('/files', methods=['GET'])
def files():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:left;">
<h1> 3 </h1>
<p> _enume </p>    
</body>
</html>
    """
    return page

@app.route('/daemon', methods=['GET'])
def daemon():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:left;">
<h1> 4 </h1>
<p> rate_web </p>    
</body>
</html>
    """
    return page

@app.route('/africa', methods=['GET'])
def africa():
    page = """
<html>
<head>
    <title>Web Technology Practice</title>
</head>
<body style="text-align:left;">
<h1> 5 </h1>
<p> sites} </p>    
</body>
</html>
    """
    return page

# FLAG NUMBER THREE
# User can modify client-side cookies
@app.route('/flag',methods = ['GET'])
def link():
    # get user input
    role = request.cookies.get('admin')
    if role == "true":
        page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> Cookies should never authenticate client side..... </p>
<p> flag{i_can_modify_clientside_cookies} </p>

</body>
</html>
        """
        return page
    else:
        return "Not authorized." 

# FLAG NUMBER 4
# User can change their user-agent
@app.route('/agent',methods = ['GET'])
def agent():
    # get user input
    agent = request.headers.get('User-Agent')
    agentLower = agent.lower()
    if "blacksun" in agentLower:
        page =  "Welcome, BlackSun member. 6"
    else:
        page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> You use <p> {{ agentVar }} 
<p> We don't take that here. </p>
<p> Sincerely, the BlackSun staff. </p>
</body>
</html>
        """
    return render_template('agent.html', agentVar=agent)
                    

# FLAG NUMBER 5
# User can request a webpage using Curl
@app.route('/curl',methods = ['GET'])
def curl():
    # get user input
    agent = request.headers.get('User-Agent')
    agentLower = agent.lower()
    if "curl" in agentLower:
        page =  "You can use headless HTTP requests-- curl! flag{i_can_use_curl}"
    else:
        page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> Visiting me in a browser? Old school.....
</body>
</html>
        """
    return page

# FLAG NUMBER 6 
# User can POST to a website
@app.route('/post',methods = ['POST'])
def post():
    page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> Good choice, you can POST! flag{i_can_change_HTTP_options}
</body>
</html>
        """
    return page

@app.route('/post',methods = ['GET'])
def postGET():
    page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> Not the right OPTION for this page...
</body>
</html>
        """
    return page

@app.route('/post',methods = ['OPTION'])
def postOPTIONS():
    page = """
<html>
<head>
    <title>Web Technology Practice </title>
</head>
<p> GET, POST, OPTION
</body>
</html>
        """
    return page


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)