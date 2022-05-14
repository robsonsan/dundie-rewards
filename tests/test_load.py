import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

@pytest.fixture(scope='function', autouse=True)
def create_new_file(tmpdir):
    tmpdir.join('new_file.txt').write('isso e sujeira...')

@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test load function"""
    with open(f'arquivo_indesejado-{uuid.uuid4()}.txt', 'w') as file_:
        file_.write('dados uteis somente para o teste')
    assert len(load(PEOPLE_FILE)) == 2
    load(PEOPLE_FILE)[0][0] == 'R'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function"""
    with open(f'arquivo_indesejado-{uuid.uuid4()}.txt', 'w') as file_:
        file_.write('dados uteis somente para o teste')
    assert len(load(PEOPLE_FILE)) == 2
    load(PEOPLE_FILE)[0][0] == 'R'