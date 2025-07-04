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
</body>
</html>
    """
    resp = make_response(page)
    # Set cookie for flag 3
    resp.set_cookie('admin', 'false')
    return resp

# FLAG NUMBER ONE
# User can isit a common website page
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
        page =  "Welcome, BlackSun member. flag{i_can_change_user_agents}"
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
                    


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)