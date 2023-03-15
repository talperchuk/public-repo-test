def raising_step(event):
    if 'error' in event:
        raise Exception(f'On event Fail')
    print(f'Got event: {event}\n')
    return 'All good'


def handle_error(event, *args, **kwargs):
    print('Handling error')
    print(f'event vars: {vars(event)}')
    event_fields = {k: v for k, v in vars(event).items() if k in [
        'body', 'key', 'origin_state', 'error']}
    print(f'selected fields: {event_fields}')
    return None
