# Codex 任务 02：风管线段提取与尺寸识别

基于任务01结果继续开发。

## 目标
1. 从疑似风管图层提取 LINE/LWPOLYLINE/POLYLINE；
2. 为每段风管生成 `duct_segment_id`；
3. 计算长度，单位按 DXF 坐标单位处理；
4. 从邻近 TEXT/MTEXT 中识别尺寸：800x400、800×400、D400、Φ400；
5. 输出 `output/duct_segments.xlsx`；
6. 无尺寸或多尺寸冲突的线段写入 `manual_review`；
7. 增加测试。

## 命令行
```bash
python -m hvac_tool.cli extract-ducts path/to/input.dxf --out output
```
