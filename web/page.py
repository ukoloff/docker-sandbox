count = [0]

def html():
  count[0] += 1
  return f"""
Hello, world!
<hr>
{count[0]}
""".strip()
