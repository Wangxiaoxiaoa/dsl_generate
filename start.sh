start_time=$(date +%s)

echo "开始执行 Stage 1..."
python -m pipelines.stage1 pipelines/config_r1/stage1_config.yaml
echo "Stage 1 执行完成"

echo "开始执行 Stage 2..."
python -m pipelines.stage2 pipelines/config_r1/stage2_config.yaml
echo "Stage 2 执行完成"

echo "开始执行 Stage 3..."
python -m pipelines.stage3 pipelines/config_r1/stage3_config.yaml
echo "Stage 3 执行完成"


end_time=$(date +%s)
duration=$((end_time - start_time))
hours=$((duration / 3600))
minutes=$(( (duration % 3600) / 60 ))
seconds=$((duration % 60))

echo "总执行时间: ${hours}小时 ${minutes}分钟 ${seconds}秒"

echo "所有阶段执行完毕!"