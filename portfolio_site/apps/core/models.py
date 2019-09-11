from django.db import models


class Info(models.Model):
    name = models.CharField('ФИО', max_length=100)
    position = models.CharField('Должность', max_length=100)
    description = models.TextField('О себе')
    linkedin_link = models.CharField('Linkedin', max_length=50)
    github_link = models.CharField('Github', max_length=50)
    website_link = models.CharField('Website', max_length=50)
    email = models.CharField("E-mail", max_length=75)
    phone_number = models.CharField("Номер телефона", max_length=20)
    profile_image = models.ImageField(upload_to='media/pictures', blank=True)

    def __str__(self):
        return self.name + ' ' + self.position


class WorkExperience(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    position = models.CharField('Должность', max_length=50)
    company_name = models.CharField('Наименовние места работы', max_length=100)
    position_time = models.CharField('Период работы', max_length=50)
    description = models.TextField('Описание деятельности')


class Skill(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    skill_direction = models.CharField('Направление навыка', max_length=100)

    def __str__(self):
        return self.skill_direction


class SkillType(models.Model):
    info = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_type_name = models.CharField('Название навыка', max_length=100)
    skill_level = models.IntegerField('Уровень владения')

    def __str__(self):
        return self.skill_type_name


class Education(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    university_name = models.CharField('Название учебного заведения', max_length=100)
    degree = models.CharField('Учебная степень', max_length=150)
    study_period = models.CharField('Период обучения', max_length=15)

    def __str__(self):
        return self.university_name


class Language(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    language_name = models.CharField("Язык", max_length=30)
    level = models.CharField('Уровень владения', max_length=50)

    def __str__(self):
        return self.language_name


class Interest(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    interest = models.CharField('Увлечение', max_length=150)

    def __str__(self):
        return self.interest
