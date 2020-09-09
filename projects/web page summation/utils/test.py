import tensorflow as tf
from model import Model
from utils import build_dict, build_dataset, batch_iter, get_text_list
valid_article_path = '.'
valid_title_path = '.'
tf.reset_default_graph()
default_path = '.'


class args:
    pass


args.num_hidden = 150
args.num_layers = 2
args.beam_width = 10
args.glove = "store_true"
args.embedding_size = 300

args.learning_rate = 1e-3
args.batch_size = 64
args.num_epochs = 10
args.keep_prob = 0.8

args.toy = True

args.with_model = "store_true"


print("Loading dictionary...")
word_dict, reversed_dict, article_max_len, summary_max_len = build_dict(
    "valid", args.toy)
print("Loading validation dataset...")
valid_x = build_dataset(
    "valid", word_dict, article_max_len, summary_max_len, args.toy)
valid_x_len = [len([y for y in x if y != 0]) for x in valid_x]
print("Loading article and reference...")
article = get_text_list(valid_article_path, args.toy)
reference = get_text_list(valid_title_path, args.toy)

with tf.Session() as sess:
    print("Loading saved model...")
    model = Model(reversed_dict, article_max_len,
                  summary_max_len, args, forward_only=True)
    saver = tf.train.Saver(tf.global_variables())
    ckpt = tf.train.get_checkpoint_state(default_path + "saved_model/")
    saver.restore(sess, ckpt.model_checkpoint_path)

    batches = batch_iter(valid_x, [0] * len(valid_x), args.batch_size, 1)

    print("Writing summaries to 'result.txt'...")
    for batch_x, _ in batches:
        batch_x_len = [len([y for y in x if y != 0]) for x in batch_x]

        valid_feed_dict = {
            model.batch_size: len(batch_x),
            model.X: batch_x,
            model.X_len: batch_x_len,
        }

        prediction = sess.run(model.prediction, feed_dict=valid_feed_dict)
        prediction_output = [[reversed_dict[y]
                              for y in x] for x in prediction[:, 0, :]]
        summary_array = []
        with open(default_path + "result.txt", "a") as f:
            for line in prediction_output:
                summary = list()
                for word in line:
                    if word == "</s>":
                        break
                    if word not in summary:
                        summary.append(word)
                summary_array.append(" ".join(summary))
                # print(" ".join(summary), file=f)

    print('Summaries have been generated')
