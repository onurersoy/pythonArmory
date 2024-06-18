class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')   # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc('Demo HTML Document')
    # my_page.add_tag('h1', 'Main heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)

    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          " of objects to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
                          " - if it's destroyed, those objects continue to exist.")

    new_docType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)

# So the difference now is that the objects are created independently of 'my_page', but then passed to the
# constructor to create the new document. Now when it's done that way, in other words, when the class is rewritten to
# use aggregation rather than composition, then the difference between aggregation and composition becomes more obvious.

# Arguably the hardest part of object-oriented programming is that you have to think carefully about how the various
# classes will work together and also what sort of things you want to do with them.
# Now sometimes the relationship is obvious, thinking back to our player class in the game program, we probably want to
# give the players weapons of some sort, now there's an obvious 'has a' relationship there, a player will have a
# weapon, now the weapons will probably be strung across the dungeons waiting to be found by the players. So they need
# to exist independently of the players, players will also exchange their weapons when they stumble across better ones.
# So in that scenario, you'd probably be better off choosing aggregation rather than composition, but other times such
# as our document here, the relationship is less clear. You could make a case for either aggregation or composition
# when considering the body of a document. It really does depend on what you want to do with it.
