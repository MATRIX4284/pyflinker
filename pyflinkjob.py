from org.apache.flink.streaming.api.functions.source import SourceFunction
from org.apache.flink.api.common.functions import FlatMapFunction, ReduceFunction
from org.apache.flink.api.java.functions import KeySelector
from org.apache.flink.streaming.api.windowing.time.Time import milliseconds
import sys

class Generator(SourceFunction):
    def __init__(self, num_iters):
        self._running = True
        self._num_iters = num_iters

    def run(self, ctx):
        counter = 0
        while self._running and counter < self._num_iters:
            ctx.collect('Hello World')
            counter += 1

    def cancel(self):
        self._running = False


class Tokenizer(FlatMapFunction):
    def flatMap(self, value, collector):
        for word in value.lower().split():
            collector.collect((1, word))


class Selector(KeySelector):
    def getKey(self, input):
        return input[1]


class Sum(ReduceFunction):
    def reduce(self, input1, input2):
        count1, word1 = input1
        count2, word2 = input2
        return (count1 + count2, word1)

def main(factory):
    env = factory.get_execution_environment()
    num = int(sys.argv[1])
    env.set_parallelism(num)
    env.create_python_source(Generator(num_iters=20000)) \
        .flat_map(Tokenizer()) \
        .key_by(Selector()) \
        .time_window(milliseconds(50)) \
        .reduce(Sum()) \
        
    env.execute()
