# 暖通风系统自动压头计算与轴测图生成工具 - 原型框架

用途：从DWG导出的DXF中提取风机、风管、文字、图层信息，逐步实现风机压头计算和轴测图自动生成。

## 建议运行环境
- Python 3.10+
- AutoCAD 2020+
- 可选：ezdxf、openpyxl、svgwrite、networkx

## MVP运行顺序
1. `python cad_reader/dxf_audit.py input.dxf output/layer_audit.csv`
2. `python recognizer/fan_detector.py input.dxf output/fans.csv`
3. 后续接入 `duct_detector.py`、`topology_builder.py`、`pressure_engine.py`。

## 注意
本框架是开发起点，不是最终成品。真实项目需根据贵司图层、块名、文字样式、构件符号继续调试规则。
