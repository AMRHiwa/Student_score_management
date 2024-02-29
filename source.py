class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score

    def __str__(self):
        return f"{self.student_id} - {self.course_code} - {self.score}"


class CourseUtil:
    def set_file(self, address):
        temp = []
        self.address = address
        file =  open(self.address, 'r')
        self.texts = file.readlines()
        for line in self.texts:
            line = line.replace('\n', '')
            id_, course, score = line.split()
            id_ = int(id_)
            course = int(course)
            score = float(score)
            temp.append([id_, course, score])
        file.close()
        self.texts = temp
        # print(f'{self.texts = }')
         

    def load(self, line_number):
        with open(self.address) as fp:
            for i, line in enumerate(fp):
                if i == line_number - 1:
                    stu, crc, score = line.split()
                    return Grade(int(stu), int(crc), float(score))

    def calc_student_average(self, student_id):
        count = 0
        average = 0
        for line in self.texts:
            id_st, _, score = line
            if id_st == student_id:
                average += score
                count += 1
        return average/count

    def calc_course_average(self, course_code):
        count = 0
        average = 0
        for line in self.texts:
            _, code, score = line
            if code == course_code:
                average += score
                count += 1
        return average/count

    def count(self):
        with open(self.address, 'r') as file:
            lines = file.readlines()
        return len(lines)

    def save(self, grade):
        grade_str = [grade.student_id, grade.course_code, grade.score]
        self.set_file(self.address)
        Entire_flag = False
        for line in self.texts:
            if line == grade_str:
                Entire_flag = True
        if Entire_flag == False:
            with open(self.address, 'a') as file:
                file.write(f'\n{grade.student_id} {grade.course_code} {grade.score}')
                
if __name__ == '__main__':
    util = CourseUtil()
    util.set_file('sample_scores.txt')
    print(util.count())

    print(util.load(3))

    grade = Grade(445612,1234,12)
    util.save(grade)
    print(util.count())

    util.set_file('sample_scores.txt')
    print(util.count())