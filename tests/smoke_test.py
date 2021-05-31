from tf_plugins import optimizers

def iterate_optimizer_test():
    for name, _ in optimizers.all_optimizers.items():
        print(name)

if __name__ == "__main__":
    iterate_optimizer_test()
