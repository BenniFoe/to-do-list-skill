from mycroft import MycroftSkill, intent_handler
from BulletPointClass import BulletPoint


class ToDoList(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.bullet_points = []

    def initialize(self):
        pass

    # @intent_handler('list.do.to.intent')
    # def handle_list_do_to(self, message):
    #     self.speak_dialog('list.do.to')

    @intent_handler('add.smiply.one.bullet.point.intent')
    def handle_add_one_bullet_point(self):
        answer = self.get_response('what.is.the.bullet.point', num_retries=0)
        bp = BulletPoint(name=answer)
        self.bullet_points.append(bp)
        self.speak_dialog('bullet.point.added')

    @intent_handler('read.all.bullet.points.intent')
    def handle_read_all_bullet_points(self):
        count = 1
        for bp in self.bullet_points:
            self.speak_dialog('read.bullet.point.name', {'position': count, 'content': bp.get_name()})




def create_skill():
    return ToDoList()

