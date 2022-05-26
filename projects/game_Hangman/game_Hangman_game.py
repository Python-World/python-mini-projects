"""Hangman CLI game
Author: Jose Noriega
"""

import os
import random
import unicodedata

def clear():
    os.system('clear')


class GameManager:
    """Holds all the business layer to make de game."""

    def __init__(self):
        self.strikes = 0
        self.words = []

        self.word_indexes_used = []
        self.word = None
        self.guessed_letters = None

        self._load_words()
        self._set_game_level()
        self._render_frame()

    def _render_frame(self):
        """Renders and refresh the main scene."""

        while True:
            clear()

            self._render_level()
            self._render_gallow()
            self._render_word_indicator()

            if self.strikes >= 6:
                print('=========== GAME OVER ===========')
                print(f'WORD: {self.word}')
                input('<press enter to restart the game or ctrl + c to exit>')
                self.strikes = 0
                self.word_indexes_used = []
                self._set_game_level()
                continue
            
            if len([letter for letter in self.word if letter not in self.guessed_letters]) == 0:
                    self._set_game_level()
                    input('<press enter to continue>')
                    continue

            letter = self._ask_for_letter()
            if letter:
                is_valid = self._validate_letter(letter)
                if not is_valid:
                    self.strikes += 1

    def _render_level(self):
        """Shows the current level on the scene."""
        print('=' * 15 + f'   LEVEL {len(self.word_indexes_used)}   ' + '=' * 15)

    def _set_game_level(self):
        """Sets the word to start the game."""
        self.guessed_letters = set()
        idx = None

        while idx is None:
            random_index = random.randint(0, len(self.words) - 1)
            if random_index not in self.word_indexes_used:
                idx = random_index
        
        self.word = self.words[idx]
        self.word_indexes_used.append(idx)

    @staticmethod
    def _normalize_string(string):
        """Removes the accents from the provided string.
        
        Args:
            string: String to be normalized
        
        Returns:
            str: normalized string
        """
        assert isinstance(string, str), 'The parameter should be a string.'

        return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode()

    def _validate_letter(self, letter):
        """Checks if the provided letter is part of the current word.
        
        Args:
            letter: Letter typed by the user
        Returns:
            Bool: Validation result
        """

        assert isinstance(letter, str) and len(letter), 'letter should be a string'

        is_valid = False

        special_letters = ['Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']

        for char in self.word:
            _char = char
            _letter = letter

            if char in special_letters:
               _char = self._normalize_string(char)

            if letter in special_letters:
               _char = self._normalize_string(letter)

            if _char == _letter:
                self.guessed_letters.add(char)
                is_valid = True

        return is_valid

    def _load_words(self):
        """Loads the words from a text file."""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        
        with open(os.path.join(base_dir, './archivos/data.txt'), 'r', encoding='UTF-8') as file:
            for line in file:
                normalized_word = line.strip().upper()
                self.words.append(normalized_word)

        assert len(self.words) > 0, 'There are not words in the data file'

    def _render_word_indicator(self):
        """Renders the word fields in the scene."""
        # normalized_word = unicodedata.normalize('NFKD', normalized_word).encode('ASCII', 'ignore')

        template = ''

        for letter in self.word:
            if letter in list(self.guessed_letters):
                template += f' {letter} '
            else:
                template += f' __ '

        print('Word: ', template)

    def _render_gallow(self):
        """Renders the gallow scene based on the strikes.
        
        Strike description:
        - For 0 it will render just the gallow
        - For 1 it will render the head
        - For 2 it will render the torso
        - For 3 it will render the left arm
        - For 4 it will render the right arm
        - For 5 it will render the left leg
        - For 6 it will render the right leg
        """

        template = """
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ||===================
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ==========@          ========
        ||                         || 
        ||                         || 
        ||                         || 
        """

        head = (
            (8, 23, '|',),
            (9, 23, '|',),
            (10, 22, '_',),
            (10, 23, '_',),
            (10, 24, '_',),
            (11, 20, '|',),
            (11, 22, '.',),
            (11, 24, '.',),
            (11, 26, '|',),

            (12, 21, '\\',),
            (12, 23, '_',),
            (12, 25, '/',),
        )

        torso = (
            (13, 23, '|',),
            (13, 24, '|',),
            (14, 23, '|',),
            (14, 24, '|',),
            (15, 23, '|',),
            (15, 24, '|',),
            (16, 23, '|',),
            (16, 24, '|',),
        )

        left_arm = (
            (14, 20, '=',),
            (14, 21, '=',),
            (14, 22, '=',),
        )
        right_arm = (
            (14, 25, '=',),
            (14, 26, '=',),
            (14, 27, '=',),
        )

        left_leg = (
            (17, 22, '/',),
            (17, 23, '/',),
            (18, 21, '/',),
            (18, 22, '/',),
        )
        right_leg = (
            (17, 24, '\\',),
            (17, 25, '\\',),
            (18, 25, '\\',),
            (18, 26, '\\',),
        )
        tramp_closed = (
            (19, 19, '=',),
            (19, 20, '=',),
            (19, 21, '=',),
            (19, 22, '=',),
            (19, 23, '=',),
            (19, 24, '=',),
            (19, 25, '=',),
            (19, 26, '=',),
            (19, 27, '=',),
        )
        tramp_opened = (
            (19, 19, '\\',),
            (19, 20, '\\',),
            (20, 20, '\\',),
            (20, 21, '\\',),
            (21, 21, '\\',),
            (21, 22, '\\',),
            (22, 22, '\\',),
            (22, 23, '\\',),
        )

        scene_descriptors = []

        if self.strikes >= 1:
            scene_descriptors += head
        if self.strikes >= 2:
            scene_descriptors += torso
        if self.strikes >= 3:
            scene_descriptors += left_arm
        if self.strikes >= 4:
            scene_descriptors += right_arm
        if self.strikes >= 5:
            scene_descriptors += left_leg
        if self.strikes == 6:
            scene_descriptors += right_leg

        if self.strikes < 6:
            scene_descriptors += tramp_closed
        else:
            scene_descriptors += tramp_opened

        lines = [list(line) for line in template.splitlines()]

        for descriptor in scene_descriptors:
            lines[descriptor[0]][descriptor[1]] = descriptor[2]

        scene = '\n'.join([''.join(l) for l in lines])
        print(scene)

    def _ask_for_letter(self):
        """Shows a form to enter the letter.
        
        
        Returns:
            str: returns the letter enterd by the user if is valid, otherwise, it will return None.
        """

        print('Instructions: Type a letter and press enter.')
        input_letter = input(': ')

        if len(input_letter) != 1:
            print('Input error: Please type a letter.')
            input('<press enter to continue>')
            return None
        return input_letter.upper()

if __name__ == '__main__':
    game = GameManager()