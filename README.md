安装
首先安装java
sudo apt update
sudo apt install default-jdk

pip install antlr4-python3-runtime==4.13.0
pip install antlr4-tools

stage1:
python -m pipelines.stage1 pipelines/stage1_config.yaml