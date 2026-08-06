# Generate a 16:9 SVG thumbnail with three-layer composition:
# 1) Interference stripes (diagonal bands) with hidden text woven in
# 2) Golden logarithmic spiral overlay
# 3) Concentric ripple circles
#
# Colors: Violet-Gold duotone
# Size: 1280x720

import math
from pathlib import Path

W, H = 1280, 720

violet = "#6A4ACF"  # slightly muted violet
gold = "#FFD76A"    # soft gold
bg = "#0E0B16"      # deep dark background

phrase = "inscribing your presence in the cosmic waves of love and trust"

def make_svg():
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append(f'<defs>')
    # Background gradient
    svg.append(f'''
      <linearGradient id="duo" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{violet}" />
        <stop offset="100%" stop-color="{gold}" />
      </linearGradient>
    ''')
    # Soft glow filter for spiral
    svg.append('''
      <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    ''')
    svg.append('</defs>')
    
    # Background rectangle
    svg.append(f'<rect width="{W}" height="{H}" fill="url(#duo)"/>')
    
    # Layer 1: Interference stripes (diagonal)
    # Create semi-transparent bands by drawing lines
    stripe_spacing = 28
    angle = -30  # degrees
    rad = math.radians(angle)
    # To cover the canvas, extend lines beyond bounds
    length = int(math.hypot(W, H)) + 200
    center_x, center_y = W/2, H/2
    
    # Group with blending
    svg.append(f'<g opacity="0.28">')
    for i in range(-int(W/stripe_spacing)-20, int(W/stripe_spacing)+20):
        # line center offset across perpendicular
        offset = i * stripe_spacing
        # line endpoints in rotated coordinates
        # We'll compute a line passing through a reference point
        cx = center_x + offset * math.cos(rad + math.pi/2)
        cy = center_y + offset * math.sin(rad + math.pi/2)
        x1 = cx - (length/2) * math.cos(rad)
        y1 = cy - (length/2) * math.sin(rad)
        x2 = cx + (length/2) * math.cos(rad)
        y2 = cy + (length/2) * math.sin(rad)
        # Alternate colors for interference feel
        color = "rgba(255,255,255,0.35)" if i % 2 == 0 else "rgba(0,0,0,0.25)"
        svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="18" />')
    svg.append(f'</g>')
    
    # Hidden text woven into stripes (very light)
    svg.append(f'<g opacity="0.07" fill="#ffffff">')
    # place multiple rotated text lines parallel to stripes
    for j in range(-6, 7):
        y = center_y + j*48
        svg.append(f'<text x="{center_x - 900:.1f}" y="{y:.1f}" font-family="serif" font-size="28" transform="rotate({angle},{center_x:.1f},{y:.1f})" letter-spacing="1.2">{(phrase + "  ") * 8}</text>')
    svg.append('</g>')
    
    # Layer 2: Golden logarithmic spiral (stroke)
    # Log spiral: r = a * e^(b*theta)
    # Choose center near golden ratio point for visual balance
    cx = W * 0.618
    cy = H * 0.382
    a = 1.0
    b = 0.15  # growth rate
    # scale spiral to canvas
    max_r = max(W, H) * 0.9
    pts = []
    theta = 0.0
    while True:
        r = a * math.exp(b * theta)
        if r > max_r:
            break
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        pts.append((x, y))
        theta += 0.12
    # Build path
    if len(pts) > 1:
        d = f'M {pts[0][0]:.2f},{pts[0][1]:.2f} ' + ' '.join([f'L {x:.2f},{y:.2f}' for x,y in pts[1:]])
        svg.append(f'<path d="{d}" fill="none" stroke="{gold}" stroke-opacity="0.85" stroke-width="3.5" filter="url(#glow)"/>')
    
    # Layer 3: Concentric ripples
    svg.append('<g opacity="0.22">')
    for k in range(6):
        r = 70 + k*70
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="none" stroke="#FFFFFF" stroke-opacity="{0.22 - k*0.03:.2f}" stroke-width="2"/>')
    svg.append('</g>')
    
    # Optional: subtle vignette
    svg.append(f'''
      <radialGradient id="vign" cx="50%" cy="50%" r="70%">
        <stop offset="60%" stop-color="rgba(0,0,0,0)" />
        <stop offset="100%" stop-color="rgba(0,0,0,0.35)" />
      </radialGradient>
      <rect width="{W}" height="{H}" fill="url(#vign)"/>
    ''')
    
    # Minimal corner caption (can be hidden if not needed)
    svg.append(f'<text x="{W-28}" y="{H-20}" text-anchor="end" font-size="16" fill="#ffffff" opacity="0.5" font-family="serif">QuantumCarrollNote × RadicanTrust™</text>')
    
    svg.append('</svg>')
    return "\n".join(svg)

svg_content = make_svg()
out_path = Path("/home/workdir/artifacts/quantum_thumbnail_16x9.svg")
out_path.write_text(svg_content, encoding="utf-8")

print(out_path.as_posix())
print(f"Generated SVG size: {len(svg_content)} chars")
