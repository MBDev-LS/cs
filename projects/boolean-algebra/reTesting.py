from pprint import pprint
import re

lst = ["\\documentclass{article}\n\\usepackage[x11names, svgnames, rgb]{xcolor}\n\\usepackage[utf8]{inputenc}\n\\usepackage{tikz}\n\\usetikzlibrary{snakes,arrows,shapes}\n\\usepackage{amsmath}\n%\n%\n\n\\usepackage[active,tightpage]{preview}\n\\PreviewEnvironment{tikzpicture}\n\\setlength\\PreviewBorder{0pt}%\n\n%\n\n\\begin{document}\n\\pagestyle{empty}\n%\n%\n%\n\n\\enlargethispage{100cm}\n% Start of code\n\\begin{tikzpicture}[>=latex',line join=bevel,]\n%%\n\\node (or1) at (117.0bp,378.0bp) [draw,diamond] {+}", '\n  \\node (and1) at (81.0bp,306.0bp) [draw,ellipse] {.}', '\n  \\node (or2) at (175.0bp,306.0bp) [draw,diamond] {+}', '\n  \\node (d1) at (18.0bp,234.0bp) [draw,circle] {D}', '\n  \\node (and2) at (81.0bp,234.0bp) [draw,ellipse] {.}', '\n  \\node (c1) at (27.0bp,162.0bp) [draw,circle] {C}', '\n  \\node (a1) at (81.0bp,162.0bp) [draw,circle] {A}', '\n  \\node (and3) at (175.0bp,234.0bp) [draw,ellipse] {.}', '\n  \\node (or3) at (279.0bp,234.0bp) [draw,diamond] {+}', '\n  \\node (d2) at (135.0bp,162.0bp) [draw,circle] {D}', '\n  \\node (and4) at (198.0bp,162.0bp) [draw,ellipse] {.}', '\n  \\node (c2) at (144.0bp,90.0bp) [draw,circle] {C}', '\n  \\node (a2) at (198.0bp,90.0bp) [draw,circle] {A}', '\n  \\node (and5) at (279.0bp,162.0bp) [draw,ellipse] {.}', '\n  \\node (and6) at (360.0bp,162.0bp) [draw,ellipse] {.}', '\n  \\node (c3) at (252.0bp,90.0bp) [draw,circle] {C}', '\n  \\node (a3) at (306.0bp,90.0bp) [draw,circle] {A}', '\n  \\node (c4) at (360.0bp,90.0bp) [draw,circle] {C}', '\n  \\node (and7) at (423.0bp,90.0bp) [draw,ellipse] {.}', '\n  \\node (b1) at (396.0bp,18.0bp) [draw,circle] {B}', '\n  \\node (a4) at (450.0bp,18.0bp) [draw,circle] {A}', '\n  \\draw [] (or1) ..controls (104.47bp,352.64bp) and (95.742bp,335.66bp)  .. (and1)', '\n  \\draw [] (or1) ..controls (137.21bp,352.61bp) and (155.1bp,331.02bp)  .. (or2)', '\n  \\draw [] (and1) ..controls (56.37bp,277.63bp) and (40.402bp,259.89bp)  .. (d1)', '\n  \\draw [] (and1) ..controls (81.0bp,276.85bp) and (81.0bp,262.92bp)  .. (and2)', '\n  \\draw [] (and2) ..controls (59.694bp,205.38bp) and (46.871bp,188.76bp)  .. (c1)', '\n  \\draw [] (and2) ..controls (81.0bp,204.85bp) and (81.0bp,190.92bp)  .. (a1)', '\n  \\draw [] (or2) ..controls (175.0bp,276.85bp) and (175.0bp,262.92bp)  .. (and3)', '\n  \\draw [] (or2) ..controls (207.71bp,282.98bp) and (246.12bp,257.13bp)  .. (or3)', '\n  \\draw [] (and3) ..controls (159.08bp,205.13bp) and (150.19bp,189.58bp)  .. (d2)', '\n  \\draw [] (and3) ..controls (184.18bp,205.05bp) and (188.88bp,190.76bp)  .. (and4)', '\n  \\draw [] (and4) ..controls (176.69bp,133.38bp) and (163.87bp,116.76bp)  .. (c2)', '\n  \\draw [] (and4) ..controls (198.0bp,132.85bp) and (198.0bp,118.92bp)  .. (a2)', '\n  \\draw [] (or3) ..controls (279.0bp,204.85bp) and (279.0bp,190.92bp)  .. (and5)', '\n  \\draw [] (or3) ..controls (304.26bp,211.17bp) and (328.23bp,190.45bp)  .. (and6)', '\n  \\draw [] (and5) ..controls (268.23bp,133.09bp) and (262.48bp,118.18bp)  .. (c3)', '\n  \\draw [] (and5) ..controls (289.77bp,133.09bp) and (295.52bp,118.18bp)  .. (a3)', '\n  \\draw [] (and6) ..controls (360.0bp,132.85bp) and (360.0bp,118.92bp)  .. (c4)', '\n  \\draw [] (and6) ..controls (384.05bp,134.28bp) and (398.97bp,117.7bp)  .. (and7)', '\n  \\draw [] (and7) ..controls (412.23bp,61.091bp) and (406.48bp,46.178bp)  .. (b1)', '\n  \\draw [] (and7) ..controls (433.77bp,61.091bp) and (439.52bp,46.178bp)  .. (a4)', '\n%\n\\end{tikzpicture}\n% End of code\n\n%\n\\end{document}\n%\n\n\n']

for line in lst:
	# reMatch = re.match(r"\\\\node \((and\d+|or\d+|not\d+|[a-z]\d+)\) at \(\d+\.\d+bp,\d+\.\dbp\) \[draw,(diamond|ellipse|square|circle)\] \{([A-Z]|[+.~])\}", line.replace('\n', '').strip()[1:-1])
	reMatch = re.match(r"\\node \((and\d+|or\d+|not\d+|[a-z]\d+)\) at \(\d+\.\d+bp,\d+\.\dbp\) \[draw,(diamond|ellipse|square|circle)\] \{([A-Z]|[+.~])\}", line.replace('\n', '').strip())
	print(reMatch)
	pprint(line)