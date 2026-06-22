from abc import ABC, abstractmethod

class BaseLesson(ABC):
    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10

    def __init__(self, lesson_code, title):
        self.lesson_code = self.validate_lesson_code(lesson_code)
        self.title = title.strip().upper()
        self.__duration_minutes = 0

    @property
    def duration_minutes(self):
        return self.__duration_minutes

    def _update_duration(self, minutes):
        if minutes <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
        self.__duration_minutes += minutes

    @abstractmethod
    def calculate_completion_score(self):
        pass

    @abstractmethod
    def update_content(self, new_data):
        pass

    @staticmethod
    def validate_lesson_code(lesson_code: str):
        if not lesson_code.startswith("LMS") or len(lesson_code) != 10:
            raise ValueError("Mã bài học không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng LMS.")
        return lesson_code

    @classmethod
    def update_base_points(cls, new_points):
        cls.base_completion_points = new_points

    def __add__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes

    def __lt__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes


class VideoLesson(BaseLesson):
    def __init__(self, lesson_code, title, video_quality="1080p"):
        super().__init__(lesson_code, title)
        self.video_quality = video_quality
        self.view_count = 0

    def calculate_completion_score(self):
        return self.base_completion_points + (self.duration_minutes * 0.5)

    def update_content(self, new_data):
        if "video_quality" in new_data:
            self.video_quality = new_data["video_quality"]
        if "title" in new_data:
            self.title = new_data["title"].strip().upper()

    def play_video(self):
        self.view_count += 1
        print(f"Học viên đã xem video. Tổng lượt xem: {self.view_count}")


class CodingChallenge(BaseLesson):
    def __init__(self, lesson_code, title, number_of_testcases=1, difficulty_multiplier=1.0):
        super().__init__(lesson_code, title)
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        return self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier

    def update_content(self, new_data):
        if "number_of_testcases" in new_data:
            if new_data["number_of_testcases"] <= 0:
                raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
            self.number_of_testcases = new_data["number_of_testcases"]


class HybridAssessment(VideoLesson, CodingChallenge):
    def __init__(self, lesson_code, title, video_quality="1080p", number_of_testcases=1, difficulty_multiplier=1.0):
        super().__init__(lesson_code, title, video_quality)
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        score_video = self.base_completion_points + (self.duration_minutes * 0.5)
        score_code = self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier
        return score_video + score_code


# Duck Typing cho Cloud Storage
class AWSS3StorageService:
    def upload_lesson(self, lesson):
        print(f"[AWS S3] Đã upload bài học {lesson.lesson_code} ({lesson.title}) lên hệ thống.")


class GoogleCloudStorageService:
    def upload_lesson(self, lesson):
        print(f"[Google Cloud] Đã upload bài học {lesson.lesson_code} ({lesson.title}) lên hệ thống.")


def sync_to_cloud(cloud_service, lesson):
    try:
        cloud_service.upload_lesson(lesson)
    except AttributeError:
        raise AttributeError("Dịch vụ lưu trữ đám mây không hợp lệ hoặc chưa ký kết chứng chỉ API liên thông.")


# ================= MENU CLI =================
def main():
    lessons = []
    current_lesson = None

    while True:
        print("\n===== RIKKEI ACADEMY LMS SIMULATOR PRO =====")
        print("1. Khởi tạo bài học mới")
        print("2. Xem thông tin bài học & Kiểm tra MRO")
        print("3. Cập nhật thời lượng & Nội dung bài học")
        print("4. Xem chi tiết điểm thưởng hoàn thành")
        print("5. Kiểm tra gộp thời lượng & So sánh độ dài")
        print("6. Đồng bộ bài giảng lên Cloud")
        print("7. Thoát chương trình")
        choice = input("Chọn chức năng (1-7): ")

        try:
            if choice == "1":
                print("--- CHỌN LOẠI BÀI HỌC ---")
                print("1. Video Lesson")
                print("2. Coding Challenge")
                print("3. Hybrid Assessment")
                lesson_type = input("Chọn loại (1-3): ")
                code = input("Nhập mã bài học 10 ký tự: ")
                title = input("Nhập tiêu đề bài học: ")

                if lesson_type == "1":
                    lesson = VideoLesson(code, title)
                elif lesson_type == "2":
                    lesson = CodingChallenge(code, title)
                elif lesson_type == "3":
                    lesson = HybridAssessment(code, title)
                else:
                    print("Loại không hợp lệ!")
                    continue

                lessons.append(lesson)
                current_lesson = lesson
                print(f"Khởi tạo thành công: {lesson.title}")

            elif choice == "2":
                if not current_lesson:
                    print("Chưa có bài học được chọn!")
                else:
                    print("--- THÔNG TIN BÀI HỌC ---")
                    print(f"Loại: {current_lesson.__class__.__name__}")
                    print(f"Nền tảng: {current_lesson.platform_name}")
                    print(f"Mã: {current_lesson.lesson_code}")
                    print(f"Tiêu đề: {current_lesson.title}")
                    print(f"Thời lượng: {current_lesson.duration_minutes} phút")
                    if isinstance(current_lesson, VideoLesson):
                        print(f"Chất lượng video: {current_lesson.video_quality}")
                        print(f"Lượt xem: {current_lesson.view_count}")
                    if isinstance(current_lesson, CodingChallenge):
                        print(f"Số testcase: {current_lesson.number_of_testcases}")
                    print("MRO:", current_lesson.__class__.mro())

            elif choice == "3":
                if not current_lesson:
                    print("Chưa có bài học được chọn!")
                else:
                    print("1. Giả lập tăng lượt xem video")
                    print("2. Cập nhật thông số bài học")
                    task = input("Chọn tác vụ (1-2): ")
                    if task == "1" and isinstance(current_lesson, VideoLesson):
                        current_lesson.play_video()
                    elif task == "2":
                        if isinstance(current_lesson, CodingChallenge):
                            tc = int(input("Nhập số testcase mới: "))
                            current_lesson.update_content({"number_of_testcases": tc})
                            print("Cập nhật testcase thành công!")
                        else:
                            minutes = int(input("Nhập số phút thời lượng bổ sung: "))
                            current_lesson._update_duration(minutes)
                            print("Cập nhật thời lượng thành công!")
                    else:
                        print("Tác vụ không hợp lệ!")

            elif choice == "4":
                if not current_lesson:
                    print("Chưa có bài học được chọn!")
                else:
                    score = current_lesson.calculate_completion_score()
                    print(f"Tổng điểm XP: {score}")

            elif choice == "5":
                if not current_lesson or len(lessons) < 2:
                    print("Cần ít nhất 2 bài học để so sánh!")
                else:
                    for i, l in enumerate(lessons):
                        print(f"{i+1}. {l.title} ({l.lesson_code}) - {l.duration_minutes} phút")
                    idx = int(input("Chọn bài học đối ứng: ")) - 1
                    other = lessons[idx]
                    print("So sánh thời lượng:", current_lesson < other)
                    print("Tổng thời lượng:", current_lesson + other)

            elif choice == "6":
                if not current_lesson:
                    print("Chưa có bài học được chọn!")
                else:
                    print("1. AWS S3")
                    print("2. Google Cloud")
                    cloud_choice = input("Chọn dịch vụ (1-2): ")
                    if cloud_choice == "1":
                        cloud = AWSS3StorageService()
                    else:
                        cloud = GoogleCloudStorageService()
                    sync_to_cloud(cloud, current_lesson)

            elif choice == "7":
                print("Cảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!")
                break

            else:
                print("Lựa chọn không hợp lệ!")

        except Exception as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()
