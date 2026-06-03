"""风管压损计算核心函数雏形。工程正式使用前需按公司标准校核公式和阻力系数。"""
import math
AIR_DENSITY = 1.2
AIR_VISCOSITY = 1.8e-5
ROUGHNESS_M = 0.00015

def hydraulic_diameter_rect(width_mm, height_mm):
    w, h = width_mm / 1000, height_mm / 1000
    return 2 * w * h / (w + h)

def velocity(q_m3h, width_mm, height_mm):
    area = (width_mm / 1000) * (height_mm / 1000)
    return (q_m3h / 3600) / area

def friction_factor_swamee_jain(re, d_m, eps=ROUGHNESS_M):
    if re < 2300:
        return 64 / re
    return 0.25 / (math.log10(eps/(3.7*d_m) + 5.74/(re**0.9)) ** 2)

def straight_duct_loss_pa(q_m3h, width_mm, height_mm, length_m):
    d = hydraulic_diameter_rect(width_mm, height_mm)
    v = velocity(q_m3h, width_mm, height_mm)
    re = AIR_DENSITY * v * d / AIR_VISCOSITY
    f = friction_factor_swamee_jain(re, d)
    return f * (length_m / d) * AIR_DENSITY * v * v / 2

def local_loss_pa(q_m3h, width_mm, height_mm, zeta):
    v = velocity(q_m3h, width_mm, height_mm)
    return zeta * AIR_DENSITY * v * v / 2

def total_path_loss(segments, terminal_pressure_pa=50, margin=0.10):
    total = terminal_pressure_pa
    for s in segments:
        total += straight_duct_loss_pa(s["q_m3h"], s["width_mm"], s["height_mm"], s["length_m"])
        for z in s.get("zetas", []):
            total += local_loss_pa(s["q_m3h"], s["width_mm"], s["height_mm"], z)
    return total * (1 + margin)
