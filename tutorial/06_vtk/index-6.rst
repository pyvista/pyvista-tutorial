xi = np.arange(300)
x, y = np.meshgrid(xi, xi)
values = 127.5 + (1.0 + np.sin(x/25.0)*np.cos(y/25.0))