class TrainingCourse:
    def __init__(self, title, duration, ppp):
        self.title = title
        self.duration = duration
        self.ppp = ppp
        self.delegates =[] 
    def add_delegate(self, delegate_name):
        self.delegates.append(delegate_name)

    def get_total_revenue(self):
        revenue = self.ppp * len(self.delegates)
        return revenue

python1 = TrainingCourse("Python 1", 4, 2_000)
python1.add_delegate("Keith")
python1.add_delegate("Alan")
print(python1.get_total_revenue())