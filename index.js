require('http')
    .createServer(function(req, resp) {
        resp.end("Hello, world!")
    })
    .listen(80)
    