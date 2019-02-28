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
            scores[i][j] = scores[j][i] = calc_score(pictures[i], pictures[j])
    return scores

# def _calc_greedy_score(i, photo_order, scores, score):
#     if numpy.max(scores[i]) < 0 :
#         return photo_order, scores
#         photo_order.append[]
#         return photo_order, scores
#
# def find_largest_combo(remaining_photos, scores):
#     if len(remaining_photos) == 1 :
#         return remaining_photos[0]
#             next_photo_id = numpy.argmax(temp_scores[i])


def calc_greedy_score(i, scores):
    photo_order = [i]
    score = 0
    temp_scores = numpy.copy(scores)
    length = len(temp_scores[i])-1
    remaining_photos = set(range(len(pictures))) - set([i])

    for j in range(length):
        next_photo_id = numpy.argmax(temp_scores[i])
        score += temp_scores[i][next_photo_id]
        temp_scores[i][next_photo_id] = temp_scores[next_photo_id][i] = -1
        photo_order.append(next_photo_id)
        remaining_photos = remaining_photos - set([next_photo_id])
        i=next_photo_id
        # photo_order, score = _calc_greedy_score(next_photo_id, photo_order,temp_scores, score)

    #
    #
    # while remaining_photos:
    #     next_photo_id = numpy.argmax(temp_scores[i])
    #     score += temp_scores[next_photo_id]
    #     print next_photo_id, temp_scores[next_photo_id]
    #     temp_scores[i][next_photo_id] = temp_scores[next_photo_id][i] = -1
    #     photo_order.append(next_photo_id)
    #     remaining_photos = remaining_photos - set([next_photo_id])
    #     photo_order, score = _calc_greedy_score(next_photo_id, photo_order,temp_scores, score)
    #     print 'debug', remaining_photos
    #     print photo_order, score
    return photo_order, score

def find_permutation(scores):
    greedy_scores = numpy.zeros(len(pictures))
    photo_order = numpy.zeros((len(pictures), len(pictures)))
    for i in range(len(pictures)):
        photo_order[i], greedy_scores[i] = calc_greedy_score(i, scores)
    max_score_index = numpy.argmax(greedy_scores)
    return photo_order[max_score_index]

if __name__ == '__main__':
    input_path = sys.argv[1]
    load_data(input_path)
    scores = calc_scores()
    data = find_permutation(scores)
    output_data = str(len(data)) + '\n' + '\n'.join(str(int(i)) for i in data)
    with open('output_{}'.format(os.path.basename(input_path)), 'w') as f:
        f.write(output_data)