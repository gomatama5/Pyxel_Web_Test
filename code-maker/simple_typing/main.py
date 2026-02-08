import pyxel
import typehandler

FPS = 60
DICT_RESULT = ["Miss", "OK", "OK", "Complete"]


class App:
    def __init__(self):
        pyxel.init(80, 35, fps=FPS, title="Typehandler Test")
        self.words = {"suika": "すいか", "itigo": "いちご", "banana": "ばなな"}
        self.process = typehandler.Process(self.words)
        self.result = ""
        pyxel.run(self.update, self.draw)

    def update(self):
        for key in pyxel.input_keys:
            key_name = chr(key)
            if not self.process.check_ignore(key_name):
                result = self.process.main(key_name)
                self.result = DICT_RESULT[result]

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, "target: {0}".format(self.process.sentence), 7)
        pyxel.text(5, 15, "input : {0}".format(self.process.input), 7)
        pyxel.text(5, 25, "result: {0}".format(self.result), 7)


App()
