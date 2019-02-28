import sys, os
import numpy

pictures = []

class Picture(object):
    def __init__(self, pic_id, line):
        self.id = pic_id
        tokens = line.split(' ')
        self.direction = tokens[0]
        self.num_tags = tokens[1]
        self.tags = tokens[2:]
        print self.tags

def calc_score(first_picture, other_picture):
    score = len(set(first_picture.tags).intersection(set(other_picture.tags)))
    return score

def load_data(input_filepath):
    lines = open(input_filepath, 'r').readlines()[1:]
    for i, line in enumerate(lines):
        pictures.append(Picture(i, line.strip()))

def calc_scores():
    scores = numpy.zeros((len(pictures), len(pictures)))
    for i in range(len(pictures)):
        for j in range(i, len(pictures)):
            if i == j:
                scores[i][j] = -1
                continue
            print 'calc %s %s' %(i, j)
            scores[i][j] = scores[j][i] = calc_score(pictures[i], pictures[j])
    print scores
    return scores

def calc_greedy_score(i, scores):
    photo_order = [i]
    score = 0
    row_scores = numpy.copy(scores[i])
    remaining_photos = set(range(len(pictures))) - set([i])
    print 'debug', remaining_photos
    while remaining_photos:
        next_photo_id = numpy.argmax(row_scores)
        score += row_scores[next_photo_id]
        row_scores[next_photo_id] = -1
        photo_order.append(next_photo_id)
        remaining_photos = remaining_photos - set([next_photo_id])
        print 'debug', remaining_photos

    return photo_order, score

def find_permutation(scores):
    greedy_scores = numpy.zeros(len(pictures))
    photo_order = numpy.zeros((len(pictures), len(pictures)))
    for i in range(len(pictures)):
        photo_order[i], greedy_scores[i] = calc_greedy_score(i, scores)
        print 'index %s: %s %s' %(i, photo_order[i], greedy_scores[i])
    print 'scorfes' , greedy_scores
    print 'photo_order', photo_order
    max_score_index = numpy.argmax(greedy_scores)
    return photo_order[max_score_index]

if __name__ == '__main__':
    input_path = sys.argv[1]
    load_data(input_path)
    scores = calc_scores()
    data = find_permutation(scores)
    print data
    with open('output_{}'.format(os.path.basename(input_path)), 'w') as f:
        f.write(data)