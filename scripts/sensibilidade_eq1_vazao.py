# Sensibilidade da Eq. 1 (1a ordem, pistao) a vazao do piloto HSSF de Caceres.
# Geometria construida: 3,4 x 1,7 m, p = 0,60 m, eta = 0,35; K = 0,36 1/d; C0 = 135,6 g/m3.
# Vazao de projeto 0,5 m3/d; vazao media reportada no monitoramento 1,11e-4 m3/s = 9,59 m3/d (Hurtado, 2025).
import os, math, csv
_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resultados'); os.makedirs(_OUT, exist_ok=True)
L, W, p, eta, K, C0 = 3.4, 1.7, 0.60, 0.35, 0.36, 135.6
A = L * W; V = A * p * eta
rows = []
Qs = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 9.59]
for Q in Qs:
    hrt = V / Q
    rows.append(dict(Q_m3_d=round(Q, 2), HLR_m3_m2_d=round(Q / A, 3), HRT_d=round(hrt, 3), HRT_h=round(hrt * 24, 1),
                     E_BOD_eq1=round(100 * (1 - math.exp(-K * hrt)), 1), BOD_load_g_m2_d=round(Q * C0 / A, 1),
                     tank500L_residence_h=round(0.5 / Q * 24, 2), rain200mm_month_pct_of_Q=round(0.2 * A / 30 / Q * 100, 2)))
with open(os.path.join(_OUT, 'sensibilidade_eq1_vazao.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
# Balancos de ordem de grandeza (fosforo e TDS) nas duas vazoes
for Q in (0.5, 9.59):
    print(f'Q={Q}: P liberado = {0.62*Q:.2f} g/d; TDS "removido" = {49.5*Q:.0f} g/d; ~70 d: P {0.62*Q*70:.0f} g, TDS {49.5*Q*70/1000:.1f} kg')
