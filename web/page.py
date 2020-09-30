count = [0]

def html():
  count[0] += 1
  return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello, world!</title>
  <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
    crossorigin="anonymous">
</head>
<body>
  <div class='container-fluid'>
    <h1>Hello, world!</h1>
    Usage count:
    <span class="badge badge-info">{count[0]}</span>
  </div>
</body>
</html>
""".strip()
