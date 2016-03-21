#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            a = f.readline()
            a.strip()
            a = list(map(int, a.split(' ')))
            nodes, _nlinks = a[0], a[1]
            n = nodes
            i = 0
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            while nodes != 0:
                a = f.readline()
                nodes -= 1
                self._titles.append(a)
                a = f.readline()
                a = list(a.split(' '))
                self._sizes[n - nodes] = int(a[0])
                self._redirect[n - nodes] = int(a[1])
                a = int(a[2])
                i+=a
                while a != 0:
                    self._links[i-a] = int(f.readline())
                    a -= 1
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return(self._offset[_id+1] - self._offset[_id])

    def get_links_from(self, _id):
        return()

    def get_id(self, title):
        pass

    def get_number_of_pages(self):
        pass

    def is_redirect(self, _id):
        pass

    def get_title(self, _id):
        pass

    def get_page_size(self, _id):
        pass


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':
    wg = WikiGraph()
    wg.load_from_file('wiki_small.txt')

    # TODO: статистика и гистограммы
