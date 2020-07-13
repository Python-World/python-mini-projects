import click

@click.group()
@click.pass_context
def todo(ctx):
    '''Simple CLI Todo App'''
    ctx.ensure_object(dict)
    #Open todo.txt – first line contains latest ID, rest contain tasks and IDs
    with open('./todo.txt') as f:
        content = f.readlines()
    #Transfer data from todo.txt to the context
    ctx.obj['LATEST'] = int(content[:1][0])
    ctx.obj['TASKS'] = {en.split('```')[0]:en.split('```')[1][:-1] for en in content[1:]}

@todo.command()
@click.pass_context
def tasks(ctx):
    '''Display tasks'''
    if ctx.obj['TASKS']:
        click.echo('YOUR TASKS\n**********')
        #Iterate through all the tasks stored in the context
        for i, task in ctx.obj['TASKS'].items():
            click.echo('• ' + task + ' (ID: ' + i + ')')
        click.echo('')
    else:
        click.echo('No tasks yet! Use ADD to add one.\n')

@todo.command()
@click.pass_context
@click.option('-add', '--add_task', prompt='Enter task to add')
def add(ctx, add_task):
    '''Add a task'''
    if add_task:
        #Add task to list in context 
        ctx.obj['TASKS'][ctx.obj['LATEST']] = add_task
        click.echo('Added task "' + add_task + '" with ID ' + str(ctx.obj['LATEST']))
        #Open todo.txt and write current index and tasks with IDs (separated by " ``` ")
        curr_ind = [str(ctx.obj['LATEST'] + 1)] 
        tasks = [str(i) + '```' + t for (i, t) in ctx.obj['TASKS'].items()]
        with open('./todo.txt', 'w') as f:
            f.writelines(['%s\n' % en for en in curr_ind + tasks])

@todo.command()
@click.pass_context
@click.option('-fin', '--fin_taskid', prompt='Enter ID of task to finish', type=int)
def done(ctx, fin_taskid):
    '''Delete a task by ID'''
    #Find task with associated ID
    if str(fin_taskid) in ctx.obj['TASKS'].keys():
        task = ctx.obj['TASKS'][str(fin_taskid)]
        #Delete task from task list in context
        del ctx.obj['TASKS'][str(fin_taskid)]
        click.echo('Finished and removed task "' + task + '" with id ' + str(fin_taskid))
        #Open todo.txt and write current index and tasks with IDs (separated by " ``` ")
        if ctx.obj['TASKS']:
            curr_ind = [str(ctx.obj['LATEST'] + 1)] 
            tasks = [str(i) + '```' + t for (i, t) in ctx.obj['TASKS'].items()]
            with open('./todo.txt', 'w') as f:
                f.writelines(['%s\n' % en for en in curr_ind + tasks])
        else:
            #Resets ID tracker to 0 if list is empty
            with open('./todo.txt', 'w') as f:
                f.writelines([str(0) + '\n'])
    else:
        click.echo('Error: no task with id ' + str(fin_taskid))

if __name__ == '__main__':
    todo()