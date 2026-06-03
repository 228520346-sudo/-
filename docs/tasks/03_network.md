# Codex 任务 03：风管拓扑网络

## 目标
1. 将风管端点按容差吸附；
2. 建立 node-edge 网络；
3. 识别端点、分支点、交叉点；
4. 从风机块附近寻找系统起点；
5. 输出 `output/network_nodes.xlsx` 和 `output/network_edges.xlsx`；
6. 生成 `output/network_preview.svg`；
7. 增加测试。

## 命令行
```bash
python -m hvac_tool.cli build-network path/to/input.dxf --out output --tolerance 100
```
