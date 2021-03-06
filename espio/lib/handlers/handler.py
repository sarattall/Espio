


class Handler(object):
    def __init__(self, id, authorized_ids=None):
        """
        id ==> string id, Ex: '3234tjegje9834sf'
        secret ==> string secret, Ex: '3234tjegje9834sf', None by default
        """
        self.id = id
        self.authorized_ids = authorized_ids


    def add_subordinate(self, subordinate):
        """
        Add a subordinate, which is an instance of Agent or Handler.
        This allows handlers to handle other handlers, who in turn
        might handle agents
        """
        raise NotImplementedError("{classname}.add_subordinate function not implemented".format(classname=self.__class__.__name__))


    def report(self, handler_id, query=None):
        """
        report any data agent has to whoever asks for it
        the handler who asks has established a secret with you right?
        """
        raise NotImplementedError("{classname}.report function not implemented".format(classname=self.__class__.__name__))


    def flush(self):
        """
        oh no!!! Handler caught by enemy operatives!!
        flush() will delete all state immediately
        agent will still be functional though
        """
        raise NotImplementedError("{classname}.flush function not implemented".format(classname=self.__class__.__name__))












