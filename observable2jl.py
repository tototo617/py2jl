from py2jl import convert_observable

jl_dir = './converted'
py_dir = '.'

if __name__ == '__main__':
    convert_observable(jl_dir,py_dir)