from mycroft import MycroftSkill, intent_file_handler


class ToDoList(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('list.do.to.intent')
    def handle_list_do_to(self, message):
        self.speak_dialog('list.do.to')


def create_skill():
    return ToDoList()

