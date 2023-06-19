class global_var:
    # case_id
    Id = 1
    request_name = 2
    url = 3
    run = 4
    request_way = 5
    header = 6
    case_depend = 7
    data_depend = 8
    field_depend = 9
    data = 10
    expect = 11
    result = 12


# 获取caseid
def get_id():
    return global_var.Id


# 获取url
def get_url():
    return global_var.url


# 获取是否执行
def get_run():
    return global_var.run


# 获取请求方式
def get_run_way():
    return global_var.request_way


# 获取header
def get_header():
    return global_var.header


# 获取header默认值
def get_header_value():
    return {"Content-Type": "application/json;charset=utf-8"}


# 获取依赖case_id
def get_case_depend():
    return global_var.case_depend


# 获取依赖数据key
def get_data_depend():
    return global_var.data_depend


# 获取依赖数据所属字段
def get_field_depend():
    return global_var.field_depend


# 获取请求数据
def get_data():
    return global_var.data


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result
