# Codex 任务 05：自动轴测图 SVG

## 目标
1. 基于 network_edges 生成简化轴测 SVG；
2. 每台风机输出一张 SVG；
3. 标注风管尺寸、长度、风量、节点编号；
4. 输出到 `output/axon/`；
5. SVG 可嵌入 Word/Excel；
6. 增加测试。

## 命令行
```bash
python -m hvac_tool.cli draw-axon path/to/input.dxf --out output
```
