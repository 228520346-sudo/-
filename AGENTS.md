# Codex 开发指令

本仓库目标：开发“DWG/DXF 暖通风系统自动压头计算与轴测图生成工具”。

## 重要原则
- 先支持 DXF；DWG 通过 AutoCAD/ODA 转 DXF 后处理。
- 不要一次性实现全部功能，每次只完成当前任务文件指定的阶段。
- 不要静默丢弃无法识别的数据，必须输出到 `output/manual_review.xlsx`。
- 所有输出文件统一写入 `output/`。
- 所有核心算法必须有 pytest 测试。
- 不做 GUI，先做命令行工具。
- 计算结果必须可追溯：每段风管、每个局部构件、每条最不利路径都要有 ID。

## 技术栈
- Python 3.11+
- ezdxf：读取 DXF
- pandas/openpyxl：输出 Excel
- networkx：风管拓扑网络
- svgwrite 或原生 XML：输出轴测 SVG
- pytest：测试

## 风管识别基本规则
优先读取 `config/layer_rules.json`。
常见图层关键词：DUCT、风管、0M-D-AC-SA、0M-D-FA、0M-D-VEN、0M-D-FIRE、DM-DUCT。
常见风机图层关键词：FAN、风机、0M-E-FAN、EQ-风机。
常见风口图层关键词：DIFF、风口、DM-DIFF。
常见风阀图层关键词：VALV、阀、DM-VALV。

## 验收方式
每一阶段完成后必须能运行：

```bash
pytest
python -m hvac_tool.cli --help
```

阶段1至少能运行：

```bash
python -m hvac_tool.cli audit samples/sample.dxf --out output
```
