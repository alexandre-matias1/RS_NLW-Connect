from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Insert on DB")

def test_insert():
    subscriber_info = {
        "name":"meuNome",
        "email":"mail@mail.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select on DB")

def test_select_subscriber():
    email = "mail@mail.com"
    evento_id = 2


    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)

    print(resp.nome)
