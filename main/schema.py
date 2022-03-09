import graphene
from graphene_django import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'title', 'text', 'status')


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(root, info, **kwargs):
        return Task.objects.all()



class UpdateTask(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        status = graphene.String()
        id = graphene.ID(required = True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, text, status, id, **kwargs):
        if status != 'no_change':
            if status in ('later', 'doing', 'done'):

                task = Task.objects.get(pk=id)
                task.status = status
                task.save()

                return UpdateTask(task=task)

        if text != 'no_change':
            task = Task.objects.get(pk=id)
            task.text = text
            task.save()

            return UpdateTask(task=task)



class CreateTask(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        status = graphene.String(required=True)

    # Class attributes define the response of the mutation
    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, title, text, status):
        task = Task()
        task.title = title
        task.text = text
        task.status = status
        task.save()

        return CreateTask(task=task)


class DeleteTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        obj = Task.objects.get(pk=id)
        obj.delete()
        return None


class Mutation(graphene.ObjectType):
    update_task = UpdateTask.Field()
    create_task = CreateTask.Field()
    delete_task = DeleteTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
