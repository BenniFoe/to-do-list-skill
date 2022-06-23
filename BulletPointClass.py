class BulletPoint():
    def __int__(self, name='', prio='B', tags=None, deadline=''):
        if tags is None:
            tags = []
        self.name = name
        self.prio = prio
        self.tags = tags
        self.deadline = deadline

    def get_name(self):
        return self.name