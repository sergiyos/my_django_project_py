from django.db import models


class Practice(models.Model):

    practice_title = models.CharField('Назва практики', max_length = 200)
    pub_date = models.DateTimeField('Дата створення', auto_now_add = True)
    start_date = models.DateTimeField('Дата початку практики')
    end_date = models.DateTimeField('Дата закінчення практики')

    def __str__(self):
        return self.practice_title

    class Meta:
        verbose_name = 'Практика'
        verbose_name_plural = 'Практика'


class Group(models.Model):
    #practice = models.ForeignKey(Practice, on_delete = models.CASCADE)
    group_title = models.CharField('Назва групи', max_length=50)

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'


class Student(models.Model):

   # group = models.ForeignKey(Group, on_delete = models.CASCADE)
    student_Specialty = models.CharField('Спеціальність', max_length=50, null=True, blank=True)
    student_Group = models.CharField('Група', max_length=50, null=True, blank=True)
    student_Number = models.PositiveSmallIntegerField('Номер', null=True, blank=True)
    student_Name = models.CharField('ПІБ', max_length=100, null=True, blank=True)
   # student_First_name = models.CharField('Імя', max_length=50)
   # student_Middle_name = models.CharField('По батькові', max_length=50)
    student_Enterprise = models.CharField('Підприємство (<назва українською>, м. <місто>)', max_length=80, null=True, blank=True)
    student_Contract = models.CharField('Договір', max_length=50, null=True, blank=True)
    student_Points = models.PositiveSmallIntegerField('Бали', null=True, blank=True)
    student_Rating = models.CharField('Оцінка', max_length=50, null=True, blank=True)
    student_The_theme_of_work = models.TextField('Тема роботи', max_length=250, null=True, blank=True)
    student_The_topic_of_work_in_English = models.TextField('Тема роботи англійською мовою', max_length=250, null=True, blank=True)
    student_Last_name_First_name_in_English = models.CharField('Прізвище Ім\'я англійською', max_length=100, null=True, blank=True)
    student_Manager = models.CharField('Керівник', max_length=50, null=True, blank=True)
    student_Email = models.CharField('E-mail', max_length=80, null=True, blank=True)

    def __str__(self):
        return  self.student_Name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'




class Teacher(models.Model):

    teacher_Surname = models.CharField('Прізвище', max_length=50)
    teacher_First_name = models.CharField('Імя', max_length=50)
    teacher_Middle_name = models.CharField('По батькові', max_length=50)
    teacher_scientific_Degree = models.CharField('Наукова ступінь', max_length=50, null=True, blank=True)
    teacher_Email = models.CharField('E-mail', max_length=80, null=True, blank=True)

    def __str__(self):
        return  self.teacher_Surname

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'


class Enterprise(models.Model):

    enterprise_Title = models.CharField('Назва', max_length=150)
    enterprise_City = models.CharField('Місто', max_length=50)


    def __str__(self):
        return self

    class Meta:
        verbose_name = 'Підприємство'
        verbose_name_plural = 'Підприємства'