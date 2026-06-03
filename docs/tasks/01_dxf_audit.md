# Codex 任务 01：DXF 图纸体检与图层统计

请实现第一阶段，不要开发 GUI，不要做完整压损计算。

## 目标
1. 读取 DXF 文件；
2. 输出所有图层清单；
3. 统计每个图层中 LINE、LWPOLYLINE、POLYLINE、TEXT、MTEXT、INSERT 的数量；
4. 按 `config/layer_rules.json` 识别疑似风管、风机、风口、风阀图层；
5. 生成 Excel 报告：`output/dxf_audit.xlsx`；
6. 生成 JSON 报告：`output/dxf_audit.json`；
7. 提供命令行入口；
8. 增加 pytest 测试。

## 命令行
```bash
python -m hvac_tool.cli audit path/to/input.dxf --out output
```

## Excel Sheet
- `layers_summary`
- `entity_counts`
- `candidate_layers`
- `manual_review`

## 验收
```bash
pytest
python -m hvac_tool.cli audit samples/sample.dxf --out output
```
