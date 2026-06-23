from abc import ABC, abstractmethod

class BaseLesson(ABC):
    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10

    def __init__(self, lesson_code, title):
        self.lesson_code = lesson_code
        self.title = title
        self.__duration_minutes = 0

    @property
    def duration_minutes(self):
        return self.__duration_minutes

    @abstractmethod
    def calculate_completion_score(self) -> float:
        pass

    @abstractmethod
    def update_content(self, new_data):
        pass

    def __add__(self, other):
        return self.duration_minutes + other.duration_minutes

    def __lt__(self, other):
        return self.duration_minutes < other.duration_minutes

    @staticmethod
    def validate_lesson_code(lesson_code):
        return (
            lesson_code.startswith("LMS")
            and len(lesson_code) == 10
        )

    @classmethod
    def update_base_points(cls, new_points):
        cls.base_completion_points = new_points
        
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = " ".join(value.strip().upper().split())

        
class VideoLesson(BaseLesson):
    def __init__(
            self,
            lesson_code,
            title,
            duration_minutes,
            video_quality,
            view_count=0
    ):
        super().__init__(lesson_code, title)

        self._BaseLesson__duration_minutes = duration_minutes
        self.video_quality = video_quality
        self.view_count = view_count

    def calculate_completion_score(self):
        return (
            self.base_completion_points
            + self.duration_minutes * 0.5
        )

    def update_content(self, new_data):
        if "video_quality" in new_data:
            self.video_quality = new_data["video_quality"]

        if "title" in new_data:
            self.title = new_data["title"]

    def play_video(self):
        self.view_count += 1
        
class CodingChallenge(BaseLesson):
    def __init__(
            self,
            lesson_code,
            title,
            number_of_testcases,
            difficulty_multiplier
    ):
        super().__init__(lesson_code, title)

        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        return (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )

    def update_content(self, new_data):
        if "number_of_testcases" in new_data:
            self.number_of_testcases = new_data[
                "number_of_testcases"
            ]
            
class HybridAssessment(VideoLesson, CodingChallenge):
    def __init__(
            self,
            lesson_code,
            title,
            duration_minutes,
            video_quality,
            number_of_testcases,
            difficulty_multiplier
    ):
        BaseLesson.__init__(
            self,
            lesson_code,
            title
        )

        self._BaseLesson__duration_minutes = duration_minutes
        self.video_quality = video_quality
        self.view_count = 0

        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        video_score = (
            self.base_completion_points
            + self.duration_minutes * 0.5
        )

        coding_score = (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )

        return video_score + coding_score
    
def create_lesson():
    print("\n--- CHỌN LOẠI BÀI HỌC KHỞI TẠO ---")
    print("1. Video Lesson")
    print("2. Coding Challenge")
    print("3. Hybrid Assessment")

    lesson_type = input("Chọn loại bài học (1-3): ")

    lesson_code = input("Nhập mã bài học: ")

    if not BaseLesson.validate_lesson_code(lesson_code):
        print("Mã bài học không hợp lệ!")
        return None

    title = input("Nhập tiêu đề bài học: ")

    if lesson_type == "1":
        return VideoLesson(
            lesson_code,
            title,
            45,
            "1080p"
        )

    elif lesson_type == "2":
        return CodingChallenge(
            lesson_code,
            title,
            5,
            1.5
        )

    elif lesson_type == "3":
        return HybridAssessment(
            lesson_code,
            title,
            45,
            "1080p",
            5,
            1.5
        )

    print("Lựa chọn không hợp lệ!")
    return None
    
new_lesson =[]
header = """===== RIKKEI ACADEMY LMS SIMULATOR PRO =====
1. Khởi tạo bài học mới (Chọn loại bài học nội dung)
2. Xem thông tin bài học & Kiểm tra thứ tự kế thừa (MRO)
3. Cập nhật thời lượng & Nội dung bài học (Tính đa hình)
4. Xem chi tiết điểm thưởng hoàn thành bài học
5. Kiểm tra gộp thời lượng & So sánh độ dài bài học (Overloading)
6. Đồng bộ bài giảng lên Nền tảng Đám mây (Duck Typing)
7. Thoát chương trình
============================================"""

while True:
    print(f"{header}")
    choice = input("Chọn chức năng (1-7): ")
    if choice == '7':
        print("Cảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!")
        break
    elif choice == '1':
        pass