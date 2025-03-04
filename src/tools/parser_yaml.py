import yaml

def parse_yaml(yaml_file):
    try:
        if not yaml_file or not isinstance(yaml_file, str):
            raise ValueError("YAML文件路径必须是非空字符串")

        with open(yaml_file, 'r', encoding='utf-8') as file:
            content = file.read()
        if not content.strip():
            raise ValueError("YAML文件内容为空")

        data = yaml.safe_load(content)
        if data is None:
            return {}            
        return data
        
    except FileNotFoundError:
        raise FileNotFoundError(f"找不到YAML文件: {yaml_file}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"YAML解析错误: {str(e)}")
    except Exception as e:
        raise Exception(f"解析YAML时发生未知错误: {str(e)}")


