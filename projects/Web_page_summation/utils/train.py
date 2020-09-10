import os
import tensorflow as tf
import time
from model import Model
from utils import build_dict, build_dataset, batch_iter
start = time.perf_counter()
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

args.toy = False  # "store_true"

args.with_model = "store_true"


if not os.path.exists(default_path + "saved_model"):
    os.mkdir(default_path + "saved_model")
else:
    # if args.with_model:
    old_model_checkpoint_path = open(
        default_path + 'saved_model/checkpoint', 'r')
    old_model_checkpoint_path = "".join(
        [
            default_path + "saved_model/",
            old_model_checkpoint_path.read().splitlines()[0].split('"')[1]])


print("Building dictionary...")
word_dict, reversed_dict, article_max_len, summary_max_len = build_dict(
    "train", args.toy)
print("Loading training dataset...")
train_x, train_y = build_dataset(
    "train", word_dict, article_max_len, summary_max_len, args.toy)

tf.reset_default_graph()

with tf.Session() as sess:
    model = Model(reversed_dict, article_max_len, summary_max_len, args)
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver(tf.global_variables())
    if 'old_model_checkpoint_path' in globals():
        print("Continuing from previous trained model:",
              old_model_checkpoint_path, "...")
        saver.restore(sess, old_model_checkpoint_path)

    batches = batch_iter(train_x, train_y, args.batch_size, args.num_epochs)
    num_batches_per_epoch = (len(train_x) - 1) // args.batch_size + 1

    print("\nIteration starts.")
    print("Number of batches per epoch :", num_batches_per_epoch)
    for batch_x, batch_y in batches:
        batch_x_len = list(
            map(lambda x: len([y for y in x if y != 0]), batch_x))
        batch_decoder_input = list(
            map(lambda x: [word_dict["<s>"]] + list(x), batch_y))
        batch_decoder_len = list(
            map(lambda x: len([y for y in x if y != 0]), batch_decoder_input))
        batch_decoder_output = list(
            map(lambda x: list(x) + [word_dict["</s>"]], batch_y))

        batch_decoder_input = list(
            map(
                lambda d: d + (summary_max_len - len(d)) * [word_dict["<padding>"]],
                batch_decoder_input))
        batch_decoder_output = list(
            map(
                lambda d: d + (summary_max_len - len(d)) * [word_dict["<padding>"]],
                batch_decoder_output))

        train_feed_dict = {
            model.batch_size: len(batch_x),
            model.X: batch_x,
            model.X_len: batch_x_len,
            model.decoder_input: batch_decoder_input,
            model.decoder_len: batch_decoder_len,
            model.decoder_target: batch_decoder_output
        }

        _, step, loss = sess.run(
            [model.update,
             model.global_step, model.loss], feed_dict=train_feed_dict)

        if step % 1000 == 0:
            print("step {0}: loss = {1}".format(step, loss))

        if step % num_batches_per_epoch == 0:
            hours, rem = divmod(time.perf_counter() - start, 3600)
            minutes, seconds = divmod(rem, 60)
            saver.save(sess, default_path +
                       "saved_model/model.ckpt", global_step=step)
            print(" Epoch {0}: Model is saved.".format(step // num_batches_per_epoch),
                  "Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds), "\n")
