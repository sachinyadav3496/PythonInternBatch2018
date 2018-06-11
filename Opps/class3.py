class Robot:
    robot_count = 0
    def __init__(self,name,work):
        Robot.robot_count += 1
        self.name = name
        self.work = work
    def show(self):
        print("Robot name = ",self.name)
        print("Robot Work = ",self.work)

    def count(self):
        print("Total Robot : ",Robot.robot_count)


