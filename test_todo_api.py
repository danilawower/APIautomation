import requests

url = "https://todo.pixegami.io/"


def test_can_call_endpoint():
    response = requests.get(url)
    assert response.status_code == 200


def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    task_id = data['task']['task_id']

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


def test_can_update_task():

    #create_task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']


    #update_task
    new_payload = {
        'content': 'my updated content',
        'user_id': payload['user_id'],
        'task_id': task_id,
        'is_done': True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    #get_validate_changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']


def test_can_list_tasks():
    list_rask_response = list_tasks("test_user")
    assert list_rask_response.status_code == 200
    data = list_rask_response.json()
    tasks = data['tasks']
    assert len(tasks) == 10




def update_task(payload):
    return requests.put(url + '/update-task', json=payload)


def list_tasks(user_id):
    return requests.get(url+f'/list-tasks/{user_id}')


def create_task(payload):
    return requests.put(url + '/create-task', json=payload)



def get_task(task_id):
    return requests.get(url + f'/get-task/{task_id}')


def new_task_payload():
    return {
        "content": "test",
        "user_id": "test_user",
        "task_id": "test_task_id",
        "is_done": False,
    }
