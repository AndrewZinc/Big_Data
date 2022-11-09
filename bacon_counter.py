from mrjob.job import MRJob

class Bacon_count(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == 'bacon':
                yield 'bacon', 1
            elif word.lower() == 'loin':
                yield 'loin', 1
            elif word.lower() == 'turducken':
                yield 'turducken', 1
                
    def reducer(self, key, values):
        yield key, sum(values)
    
if __name__ == '__main__':
    Bacon_count.run()
    
