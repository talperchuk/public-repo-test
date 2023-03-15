import mlrun

mlrun.set_env_from_file('~/Repos/servingames/mlrun.env', return_dict=True)


def deploy_error_tester_function(project_name='test', func_name='func', tag='', image='mlrun/mlrun'):
    project = mlrun.get_or_create_project(project_name, context='./')
    project.set_source(
        source='git://github.com/talperchuk/public-repo-test.git#error-handler', pull_at_runtime=False)

    function = mlrun.new_function(
        name=func_name, project=project.name, kind='serving', image=image)

    graph = function.set_topology('flow')

    graph.to(name='raise', handler='src.handlers.raising_step').respond()
    graph.add_step(name='error_catcher',
                   handler='src.handlers.handle_error', full_event=True, after='')
    graph.error_handler('error_catcher')

    function.spec.readiness_timeout = 300
    function.spec.max_replicas = 1

    project.set_function(func=function, with_repo=True, requirements=[])
    output = project.deploy_function(function=function, verbose=True, tag=tag)
    print(output)


if __name__ == '__main__':
    deploy_error_tester_function(project_name='exploration',
                                 image='mlrun/mlrun',
                                 func_name='cmd-with-error',
                                 tag='v0',
                                 )
