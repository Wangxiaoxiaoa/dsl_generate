# CFG_generate

CFG_generate 是一个基于上下文无关文法(Context-Free Grammar, CFG)的自动化语言生成工具。该工具旨在帮助开发者从ANTLR语法规则出发，自动生成符合语法规则的DSL语句，并将其转换为自然语言表达。

## 主要功能

本工具采用三阶段流水线架构:

1. **语法骨架生成**: 基于ANTLR语法规则自动生成语法结构骨架
2. **DSL语句生成**: 将语法骨架填充为完整的DSL语句
3. **自然语言转换**: 将DSL语句转换为人类可读的自然语言表达

## 应用场景

- 语言设计与验证：快速验证新设计的DSL语法是否满足需求
- 测试数据生成：为语言解析器生成大量测试用例
- 文档生成：自动生成DSL语句的自然语言说明
- 语言学习：通过DSL与自然语言的对照，帮助用户理解DSL语法

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


### Stage 1: 语法骨架生成

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