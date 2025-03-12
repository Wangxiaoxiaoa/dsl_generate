echo "开始执行 Stage 1..."
python -m pipelines.stage1 pipelines/config/stage1_config.yaml
echo "Stage 1 执行完成"

echo "开始执行 Stage 2..."
python -m pipelines.stage2 pipelines/config/stage2_config.yaml
echo "Stage 2 执行完成"

echo "开始执行 Stage 3..."
python -m pipelines.stage3 pipelines/config/stage3_config.yaml
echo "Stage 3 执行完成"

echo "所有阶段执行完毕!"