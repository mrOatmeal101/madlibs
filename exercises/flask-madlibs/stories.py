"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """
    # using def __init__ (dunder init) so that the code below will run when the class Story is called ().
    # self is refering to the specific instance the user is currently running. 
    def __init__(self, words, text): # words & text are the parameters needed to initalize the story.
        # so in this case words are drawn from the list in story.
        # and text is drawn from the string template literal ("""""")
        """Create story with words and template text."""
        # setting variable prompts (assign words a property) equal to the variable words. first would be 'place'
        self.prompts = words # these will show up as attributes under dir()
        # setting variable template (assign text a property) equal to the variable text. 
        self.template = text

    # making function called generate() as an instance method 
    # passing in self so that  function has access to self.promts and self.template
    # passing in answers which are user inputs from the query string (they are stored in the url bar)
    def generate(self, answers):
        """Substitute answers into text."""
        # setting the attribute self.template equal to the variable text
        text = self.template
        # for loop with with vars key & val which are in answers.items(): 
        # setting key equal to place and val to the user input from the form
        # 
        for (key, val) in answers.items():
            # updating the text variable every time the loop is ran
            # replacing the key inside of text with the user input stored in val.
            text = text.replace("{" + key + "}", val)
        # return the text var after the loop finishes. 
        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

s = Story(["noun", "verb"],"I love to {verb} a good {noun}.")
ans = {"verb": "eat", "noun": "mango"}