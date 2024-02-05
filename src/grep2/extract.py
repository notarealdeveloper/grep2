__all__ = [
    'search',
]

import gpts
import textwrap

prompt = """
Extract all the instances of type {irregex!r} from the following text

```
{text}
```

You must not say any other words before or after your answer. If you
say any other words except the answers, you failed. If you find multiple
answers, please separate each answer using {output_delimeter}
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
