__all__ = [
    'search',
]

import gpts

prompt = """
COMMAND
I want you to act like a soft version of the unix grep command.
Given an irregular expression, I want you to extract the matches.

EXAMPLES
If I tell you to extract all the matches to the irregular
expression 'fruit' from the text:

```
One apple...
Three cupcakes?
I like bananas!
A big red car.
```

Then you should return:

```
['apple', 'banana']
```

REQUIREMENTS

- The output should be a python list that can be passed to `eval`.
- Do not modify the sub-strings you extract from the text in any way.
- You may strip leading whitespace if it is shared by all lines in
  a multi-line match, but do not modify the results in any other way.
- You must NOT say any other words before or after your answer.
- If you say ANY other words except the answers, you've failed.
- If you insist on adding commentary like LLMs often do, prefix
  each line of commentary with an '@' symbol. I want the output
  to be machine readable, so I need it to be as easy as possible
  to remove anything except the answer. In other words, nothing
  you say aside from the answer will help me at all, and may
  break my code, so just return me a list of matches.


MAIN REQUEST
Now, please extract all instances of type:

{irregex!r}

from the following text:

```
{text}
```
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


