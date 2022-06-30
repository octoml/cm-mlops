try:
    import tensorflowx as tf
    print(tf.__version__)
except ImportError as e:
    from sys import stderr
