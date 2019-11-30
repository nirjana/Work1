from django.db import models


# Create your models here.
class TaskManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['task_name'])<2:
            errors.append('Tasks name must be longer than 1 Characters')
        if len(form['done_by'])<2:
            errors.append('Done_bys name must be longer than 1 Characters')
        if len(form['description'])<6:
            errors.append('Task description must be longer than 5 Characters')
        return errors

    def save_task(self, form, cap_done_by):
        new_done_by = Done_by.objects.get(t_name=cap_done_by)
        new_task = self.create(
            name = form['task_name'],
            done_by = new_done_by,
            description = form['description'],
        )
        return new_task

    def save_done_by(self, form, cap_done_by):
        if len(Done_by.objects.filter(t_name=cap_done_by)) == 0:
            print('Adding done_by')
            new_done_by = self.create(
                t_name = form['done_by'].capitalize()
            )
            return new_done_by
        print('did not add done_by')
        return Done_by.objects.get(t_name=cap_done_by).id


class Done_by(models.Model):
    t_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()

    def __str__(self):
        string = f'{self.t_name}'
        return string


class Task(models.Model):
    name = models.CharField(max_length=255)
    done_by = models.ForeignKey(Done_by, related_name='tasks')
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()

    def __str__(self):
        string = f'{self.name}: taught by: {self.done_by} {self.description}'
        return string

