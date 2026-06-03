# Codex 任务 04：风机压头计算

## 目标
1. 实现矩形风管水力直径计算；
2. 实现直管摩擦阻力计算；
3. 实现弯头、三通、变径、风阀、风口局部阻力数据库占位；
4. 对每台风机寻找到末端的最不利路径；
5. 输出 `output/fan_pressure_report.xlsx`；
6. 每台风机输出可追溯计算过程；
7. 增加公式测试。

## 命令行
```bash
python -m hvac_tool.cli calc-pressure path/to/input.dxf --out output
```
