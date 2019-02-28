import sys, os
import numpy

pictures = []
picture_mapping = {}
all_scores = numpy.zeros((len(pictures), len(pictures)))

class Picture(object):
    def __init__(self, pic_id, line):
        self.id = pic_id
        tokens = line.split(' ')
        self.direction = tokens[0]
        self.num_tags = tokens[1]
        self.tags = tokens[2:]
        print self.tags


def load_data(input_filepath):
    lines = open(input_filepath, 'r').readlines()[1:]
    for i, line in enumerate(lines):
        pictures.append(Picture(i, line.strip()))

def calc_score(first_picture, other_picture):
    score = len(set(first_picture.tags).intersection(set(other_picture.tags)))
    return score

def calc_scores():
    #scores = numpy.zeros((len(pictures), len(pictures)))
    for i in range(len(pictures)):
        for j in range(i, len(pictures)):
            if i == j:
                all_scores[i][j] = -1
                continue
            print 'calc %s %s' %(i, j)
            all_scores[j][i] = calc_score(pictures[i], pictures[j])
    print all_scores
    return all_scores

def algogeva():
    while all_scores.argmax() >= 0:
        algogeva_step()


def algogeva_step():
    (i,j) = numpy.unravel_index(all_scores.argmax(), all_scores.shape)
    geva_join(i,j)

def geva_join(i, j):
    #need to flip list
    if (picture_mapping[i][0] == i and picture_mapping[j][0] == j) or (picture_mapping[i][-1] == i and picture_mapping[j][-1]):
        picture_mapping[i].reverse()

    if picture_mapping[i][0] == i:
        new_list = picture_mapping[j] + picture_mapping[i]
    else:
        new_list = picture_mapping[i] + picture_mapping[j]

    all_scores[i,j] = all_scores[j,i] = -1
    all_scores[new_list[0], new_list[-1]] = all_scores[new_list[-1], new_list[0]] = -1
    #deleting rows and columns from the scores matrix if i or j are ending up in the middle of a list
    for edge in [i,j]
    if new_list[0] != edge and new_list[-1] != edge:
        all_scores[:,i] = -1
        all_scores[i,:] = -1

    picture_mapping[j] = picture_mapping[i] = new_list

def create_picture_mapping():
    for picture in pictures:
        picture_mapping[picture.index] = [picture.index]

def run_algorithm():
    input_path = sys.argv[1]
    print(1)
    load_data(input_path)
    all_scores = calc_scores()
    create_picture_mapping()
    algogeva()
    data = picture_mapping[1]
    with open('output','w') as f:
        f.write(data)

if __name__ == '__main__':
    run_algorithm()











