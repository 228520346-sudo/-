"""轴测图SVG生成雏形。
输入拓扑树后，可将主管竖向排布、支管45°展开。此处仅保留接口。"""
def render_system_svg(system_graph, outfile):
    # TODO: 将节点拓扑映射为二维树布局，再生成SVG polyline和文字标注。
    with open(outfile, "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800">')
        f.write('<text x="30" y="40" font-size="24">HVAC Axonometric Diagram - Prototype</text>')
        f.write('</svg>')
