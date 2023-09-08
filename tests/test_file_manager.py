import pytest

from src.utils.file_manager import FileManager


def test_init_exception(json_file_none, yaml_file_none):
    with pytest.raises(TypeError):
        FileManager('file')
    with pytest.raises(TypeError):
        FileManager('file.txt')
    assert str(json_file_none.file) == '/home/zerg/PyCharm_projects/SkyPro/5/Coursework_5/tests/test_fixtures/none.json'
    assert str(json_file_none.type) == 'json'
    assert str(yaml_file_none.file) == '/home/zerg/PyCharm_projects/SkyPro/5/Coursework_5/tests/test_fixtures/none.yaml'
    assert str(yaml_file_none.type) == 'yaml'


def test_repr(json_file_none, yaml_file_none):
    assert str(json_file_none) == ('Path: /home/zerg/PyCharm_projects/SkyPro/5/Coursework_5/'
                                   'tests/test_fixtures/none.json\nType: JSON')
    assert str(yaml_file_none) == ('Path: /home/zerg/PyCharm_projects/SkyPro/5/Coursework_5/'
                                   'tests/test_fixtures/none.yaml\nType: YAML')


def test_save_file(json_file_dict, json_file_list, yaml_file_dict, yaml_file_list):
    assert json_file_dict.save_file({'jd_0': '0', 'jd_1': '1'})
    assert json_file_list.save_file([{'jL_0': '0_0', 'jL_1': '0_1'}, {'jL_0': '1_0', 'jL_1': '1_1'}])
    assert yaml_file_dict.save_file({'yd_0': '0', 'yd_1': '1'})
    assert yaml_file_list.save_file([{'yL_0': '0_0', 'yL_1': '0_1'}, {'yL_0': '1_0', 'yL_1': '1_1'}])


def test_save_file_exception(json_file_dict, yaml_file_dict):
    with pytest.raises(TypeError):
        json_file_dict.save_file('asd')
    with pytest.raises(TypeError):
        json_file_dict.save_file(12345)
    with pytest.raises(TypeError):
        yaml_file_dict.save_file('asd')
    with pytest.raises(TypeError):
        yaml_file_dict.save_file(12345)


def test_load_file(json_file_dict, json_file_list, yaml_file_dict, yaml_file_list, json_file_bad):
    assert json_file_dict.load_file() == {'jd_0': '0', 'jd_1': '1'}
    assert json_file_list.load_file() == [{'jL_0': '0_0', 'jL_1': '0_1'}, {'jL_0': '1_0', 'jL_1': '1_1'}]
    assert yaml_file_dict.load_file() == {'yd_0': '0', 'yd_1': '1'}
    assert yaml_file_list.load_file() == [{'yL_0': '0_0', 'yL_1': '0_1'}, {'yL_0': '1_0', 'yL_1': '1_1'}]
    assert json_file_bad.load_file() is None


def test_update(json_file_dict, json_file_list, json_file_none,
                yaml_file_dict, yaml_file_list, yaml_file_none):
    # Test case # 1
    assert json_file_dict.update_file({'jd_0': '0000', 'jd_2': '2'})
    assert json_file_dict.load_file() == {'jd_0': '0000', 'jd_1': '1', 'jd_2': '2'}
    # Test case # 2
    assert json_file_list.update_file([{'jL_0': '2_0', 'jL_1': '2_1'}])
    assert json_file_list.load_file() == [{'jL_0': '0_0', 'jL_1': '0_1'},
                                          {'jL_0': '1_0', 'jL_1': '1_1'},
                                          {'jL_0': '2_0', 'jL_1': '2_1'}]
    # Test case # 3
    assert yaml_file_dict.update_file({'yd_0': '0000', 'yd_2': '2'})
    assert yaml_file_dict.load_file() == {'yd_0': '0000', 'yd_1': '1', 'yd_2': '2'}
    # Test case # 4
    assert yaml_file_list.update_file([{'yL_0': '2_0', 'yL_1': '2_1'}])
    assert yaml_file_list.load_file() == [{'yL_0': '0_0', 'yL_1': '0_1'},
                                          {'yL_0': '1_0', 'yL_1': '1_1'},
                                          {'yL_0': '2_0', 'yL_1': '2_1'}]
    # Test case # 5
    assert json_file_none.update_file({'jd_0': '1', 'jd_2': '1'})
    assert json_file_none.load_file() == {'jd_0': '1', 'jd_2': '1'}
    assert yaml_file_none.update_file([{'yL_0': '0_0', 'yL_1': '0_1'}])
    assert yaml_file_none.load_file() == [{'yL_0': '0_0', 'yL_1': '0_1'}]


def test_update_exception(json_file_dict, json_file_list):
    with pytest.raises(TypeError):
        json_file_dict.update_file([{'yL_0': '2_0', 'yL_1': '2_1'}])
    with pytest.raises(TypeError):
        json_file_list.update_file({'yL_0': '2_0', 'yL_1': '2_1'})

