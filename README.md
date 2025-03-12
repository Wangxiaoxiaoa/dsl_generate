- 输入：ANTLR语法文件
- 输出：批量生成的语法骨架语句
- 功能：根据ANTLR语法规则，生成符合语法结构的基本骨架

### Stage 2: DSL语句填充
- 输入：Stage 1生成的语法骨架
- 输出：完整的DSL语句
- 功能：将骨架语句中的占位符填充为具体的值，生成完整且符合ANTLR语法的DSL语句

### Stage 3: 自然语言转换
- 输入：Stage 2生成的DSL语句
- 输出：对应的自然语言描述
- 功能：将DSL语句转换为人类可读的自然语言表达

## 环境要求

### 系统依赖
- Java Runtime Environment (JRE)
- Python 3.x

### 安装步骤

1. 安装Java环境
bash
sudo apt update
sudo apt install default-jdk

2. 安装Python依赖
bash
pip install antlr4-python3-runtime==4.13.0
pip install antlr4-tools


## 使用方法

### Stage 1: 生成语法骨架
python -m pipelines.stage1 pipelines/stage1_config.yaml
### Stage 2: DSL语句生成
python -m pipelines.stage2 pipelines/stage2_config.yaml
### Stage 3: 自然语言转换
python -m pipelines.stage3 pipelines/stage3_config.yaml
