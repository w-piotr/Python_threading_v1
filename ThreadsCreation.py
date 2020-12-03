from Plus import Plus
from Star import Star
from multiprocessing import Process

class ThreadsCreation:
	def run(self):
		if __name__ == '__main__':
			p = Plus().run()
			g = Star().run()
			process1 = Process(target=p)
			process1.start()
			process2 = Process(target=g)
			process2.start()
			process1.join()
			process2.join()
			print('FINISH')


ThreadsCreation().run()