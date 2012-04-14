class Outputter():
    def output(self, data, format):
        getattr(self, "output_%s" % format.lower()).__call__(data)

    def output_xml(self, data):
        print "xml %s" % data

    def output_ascii(self, data):
        print "ascii %s" % data

    def output_serializable(self, data):
        print "seria... %s" % data

def output(data, format="xml"):
    c = Outputter()
    c.output(data, format) 

if __name__ == "__main__":
    output("hej");
    output("hej", "ascii")
    output("hej", "serializable")
