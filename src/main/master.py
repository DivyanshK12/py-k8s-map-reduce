import os

def main():
    num_mappers, num_reducers = os.getenv("MAP_POD_COUNT", 3), os.getenv("REDUCE_POD_COUNT", 2)
    print(f"Master Running with config mappers : {num_mappers} reducers : {num_reducers}")

if __name__ == "__main__":
    main()