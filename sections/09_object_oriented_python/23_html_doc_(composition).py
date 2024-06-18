# 3 parts that an HTML document must have: a line containing HTML version information that's called the document type
# definition or DTD, a header section and a document body.

# We can say that an HTML document has a DTD, and it has a header, and it has a body; when you've got 'has a'
# relationships like this, that's an indication that we could consider, and we should consider using 'composition' when
# creating a class.

class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)  # 1st 'file' is the parameter of the print function


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag("title", title)
            self.contents = self._title_tag


# You can create a class hierarchy using inheritance and then use those classes^^ in a composition relationship to
# build up another class:
class Body(Tag):

    def __init__(self):
        super().__init__('body', '')   # body contents will be built up separately
        self._body_contents = []  # Body is also a composition but now the body class has its own attributes aren't
        # just composed of its composite classes; it has a '_body_contents' data attribute and a method called add_tag.

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)  # << Composition
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()
    # HtmlDoc class is made up of instances of the three other classes, so you could say that it's composed of the
    # three other classes and that's composition.

    # This class is entirely composed of other classes, and it doesn't have any data attributes of its own. Now that
    # doesn't have to be the case, so I don't want to give the impression that composition means creating a class and
    # entirely out of other classes. The important thing is that our HtmlDoc class contains other classes and can make
    # use of the attributes that those classes provide.

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open("test.html", "w") as test_doc:
        my_page.display(file=test_doc)

# Alright, so we used both composition and inheritance in this program, and it's a good example of the differences
# between them, and when you use each one.

# So getting back to our code; our basic classes all inherit from tag and when we talk about 'head' f.e., would say
# that head is a tag, similarly body is a tag and so is doctype. So whenever you have a relationship that can be
# described using 'is a', that's an indication that you should consider using inheritance to model the objects.

# Composition is used when the relationship is described as 'has a', a document has a doctype and has a body, so
# composition is more appropriate to model the HtmlDoc.
