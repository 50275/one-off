# should've been done with algebra solving software now that I think about it
# especially since it could've been put on a website
# i mean theres other kinematics solvers out there. I only realized that AFTER creating this program
def kinematics(d="-", vi="-", vf="-", a="-", t="-"):
    collection = [d, vi, vf, a, t]
    if collection.count("-") != 1:
        print(collection)
        return "exactly one of your variables should be \"-\" (unset)"
    if collection.count("?") != 1:
        print(collection)
        return "exactly one of your variables should be \"?\" (unknown)"
    if vf == "-":
        return kinematics1(d, vi, a, t)
    if t == "-":
        return kinematics2(vf, vi, a, d)
    if d == "-":
        return kinematics3(vf, vi, a, t)
    if a == "-":
        return kinematics4(d, vi, vf, t)
    if vi == "-":
        return kinematics5(d, vf, a, t)
    return "how?"

def kinematics1(d, vi, a, t):
    if d == "?":
        return vi*t + 0.5*a*t*t
    if vi == "?":
        return (d-0.5*a*t*t) / t
    if a == "?":
        return (d-vi*t) / 0.5 / t / t
    if t == "?":
        # 0.5*a*t*t + vi*t - d
        # b^2 +- sqrt(b - 4ac) [divide by 2a] 
        a = 0.5*a
        b = vi
        c = -d
        det = b**2 - 4*a*c
        if det < 0:
            return "error: determinant less than 0"
        # i hate having multiple outputs but what can i do
        return ((-b+det)/2/a, (-b-det)/2/a)
    return None

#vf^2 = vi^2 + 2ad
def kinematics2(vf, vi, a, d):
    if vf == "?":
        return (vi*vi+2*a*d) ** 0.5
    if vi == "?":
        return (vf*vf-2*a*d) ** 0.5
    if a == "?":
        return (vf*vf-vi*vi)/2/d
    if d == "?":
        return (vf*vf-vi*vi)/2/a
    return None

# vf = vi + a*t
def kinematics3(vf, vi, a, t):
    if vf == "?":
        return vi + a * t
    if vi == "?":
        return vf - a * t
    if a == "?":
        return (vf-vi)/t
    if t == "?":
        return (vf-vi)/a
    return None

# d = 0.5t(vi+vf)
def kinematics4(d, vi, vf, t):
    if d == "?":
        return 0.5*t*vi+0.5*t*vf
    if t == "?":
        return d / (0.5*vi+0.5*vf)
    if vi == "?":
        # d = 0.5t*vi + 0.5t*vf
        return (2*d/t-vf)
    if vf == "?":
        return (2*d/t-vi)
    return None

# laziness
def kinematics5(d, vf, a, t):
    # LOL
    vi = kinematics3(vf=vf, vi="?", a=a, t=t)
    return kinematics1(d, vi, a, t)







    
