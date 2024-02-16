class Prompter(object):

    def __init__(self):
        pass

    def text(self, feeling, whats_next):
        resp = "It is 8:14am, and I am feeling {feeling} but {whats_next} for the new day."
        resp += " "
        resp += "Give me a fortune that will inspire me for the next hour. "

        return resp.format(
            feeling=feeling,
            whats_next=whats_next,
        )
