function Request()
{
    var request = new XMLHttpRequest();
    request.onreadystatechange = function()
    {
        if (request.readyState != 4) return;
        if (request.status != 200)
        {
            alert(request.status + ': ' + request.statusText);
        }
        else
        {
            alert(request.responseText);
        }
    }
    this.get = function(url)
    {
        request.open("GET", url, true);
        request.send();
    };
    this.post = function(url)
    {
        request.open("POST", url, true);
        request.send();
    }
}

function User(name)
{
    this.name = name;
    this.sayHello = function()
    {
        alert("Hello, " + name);
    };
}

function nextBackgroundColor(style)
{
    if (style.background == 'red')
    {
        style.background = '';
    }
    else
    {
        style.background = 'red';
    }
}

function nextBackground(style, user)
{
    var v = new Request();
    v.get('/blog/');
}