import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print("Wash disk {}".format(dish))
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print("Drye dish {}".format(dish))
        input.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dishes = ['salad', 'bread', 'entree', 'dessert']
    proc_dryer = mp.Process(target=dryer, args=(dish_queue,))
    proc_dryer.daemon = True
    proc_dryer.start()
    washer(dishes, dish_queue)
    dish_queue.join()
