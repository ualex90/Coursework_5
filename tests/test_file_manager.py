import pytest


def test_save_file(json_file_dict, json_file_list, yaml_file_dict, yaml_file_list):
    # Test case # 1
    assert json_file_dict.save_file({'jd_0': '0', 'jd_1': '1'})
    assert json_file_list.save_file([{'jL_0': '0_0', 'jL_1': '0_1'}, {'jL_0': '1_0', 'jL_1': '1_1'}])
    assert yaml_file_dict.save_file({'yd_0': '0', 'yd_1': '1'})
    assert yaml_file_list.save_file([{'yL_0': '0_0', 'yL_1': '0_1'}, {'yL_0': '1_0', 'yL_1': '1_1'}])


def test_save_file_exception(yaml_file_dict):
    with pytest.raises(TypeError):
        yaml_file_dict.save_file('asd')
    with pytest.raises(TypeError):
        yaml_file_dict.save_file(12345)


def test_load_file(json_file_dict, json_file_list, yaml_file_dict, yaml_file_list):
    assert json_file_dict.load_file() == {'jd_0': '0', 'jd_1': '1'}
    assert json_file_list.load_file() == [{'jL_0': '0_0', 'jL_1': '0_1'}, {'jL_0': '1_0', 'jL_1': '1_1'}]
    assert yaml_file_dict.load_file() == {'yd_0': '0', 'yd_1': '1'}
    assert yaml_file_list.load_file() == [{'yL_0': '0_0', 'yL_1': '0_1'}, {'yL_0': '1_0', 'yL_1': '1_1'}]


def test_update(json_file_dict, json_file_list, yaml_file_dict, yaml_file_list):
    pass
