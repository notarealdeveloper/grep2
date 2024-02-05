__all__ = [
    'search',
]

import gpts

prompt = """
I want you to act like a soft version of the unix grep command.
Extract all the instances of type {irregex!r}
from the following text:

```
{text}
```

Requirements:
- If you find multiple answers, please separate them using
  output delimeter: {output_delimeter}.
- Do not modify the sub-strings you extract from the text,
  just return them unmodified, as is.
- You may strip leading whitespace if it is shared by all
  lines in a multi-line match, but do not modify the result
  in any other way.
- You must NOT say any other words before or after your answer.
- If you say ANY other words except the answers, you've failed
  and I will be very disappointed in you.
"""

OUTPUT_DELIMETER = 'two newline characters'

def search(irregex, text, output_delimeter=OUTPUT_DELIMETER):
    """ Search text for an irregular expression. """
    model = gpts.Mixtral()
    question = prompt.format(
        irregex=irregex,
        text=text,
        output_delimeter=output_delimeter,
    )
    return model.ask(question)
