from time import sleep
import types
import threading
import requests  # Not an actual dependency, just used to demonstrate class usage.


class ParallelExecutioner:
    """
    Class is intended for executing code on each element of a list in separate Thread
    which it creates depending on parameters used on object creation.
    """
    def __init__(self, number_of_threads, data_list, payload_function, use_timeout=False, timeout_in_seconds=10):
        """
        Constructor uses the following parameters:
        :param number_of_threads: # Number of parallel threads to be created.
        :param data_list: # List of data on which payload function will be called in separate Thread
        :param payload_function: # Function to execute as a payload
        :param use_timeout: # Flag is used to halt execution for specified time after executing payload function
        :param timeout_in_seconds: # How many seconds to wait after executing payload function
        """
        self._lock = threading.Semaphore(number_of_threads)
        self._data_list = data_list
        self._payload_function = payload_function
        self._use_timeout = use_timeout
        self._timeout_in_seconds = timeout_in_seconds
        # creating a Thread Pool
        self.create_thread_pool()

    def run_payload(self, item):
        """
        Executes payload function passed as a parameter on object creation.
        :param item:
        :return: None
        """
        print("Starting payload...")
        # Executing payload function
        if isinstance(self._payload_function, types.FunctionType):
            self._payload_function(item)
        else:
            # Raise an exception if not a function was passed as payload.
            raise TypeError("Expecting a function but received a " + str(type(self._payload_function)))
        if self._use_timeout:
            print("Waiting: " + str(self._timeout_in_seconds) + " seconds (timeout)")
            sleep(self._timeout_in_seconds)
        self._lock.release()

    def create_thread_pool(self):
        """
        Creates a Thread Poll and uses threading.Semaphore object to control number of concurrent Threads.
        :return: None
        """
        print("Starting creating Thread Pool")
        # check if passed data is actually a list
        if not isinstance(self._data_list, list):
            raise TypeError("Expecting a list of data but received a " + str(type(self._data_list)))
        # List of threads objects
        thread_pool = []
        # passing each item of data list to the payload function and running it in separate Thread
        for item in self._data_list:
            # creating new thread that calls payload function
            thread = threading.Thread(target=self.run_payload, args=(item,))
            thread_pool.append(thread)
            thread.start()
            # adding thread to our lock, so we could wait if needed and not spawn all Threads at the same time.
            self._lock.acquire()
        for thread in thread_pool:
            # force waiting until the thread terminates
            thread.join()
        print("Thread Pool was successfully created")


def test_payload(item):
    """Just an example of payload function."""
    print("Sending HTTP Request to " + str(item))
    r = requests.get(item)
    print("Response status code: " + str(r.status_code) + " for " + str(item))


def main():
    """Simple example of how to use the class."""
    lst = ["https://google.com", "http://mail.ru", "http://ya.ru/", "https://vk.com/", "https://mail.google.com/"]
    pe = ParallelExecutioner(10, lst, test_payload)


if __name__ == "__main__":
    main()