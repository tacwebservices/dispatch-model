import pypsa
n = pypsa.Network()
n.add("Bus", "gen_bus", carrier="transmission")
n.add("Bus", "load_bus")
n.add("Load", "load", bus="load_bus", p_set=500)
n.add("Line", "line", bus0="gen_bus", bus1="load_bus", x=0.1, s_nom=1000)
n.add("Generator", "coal", bus="gen_bus", p_nom=700, marginal_cost=3)