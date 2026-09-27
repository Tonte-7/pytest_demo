import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  def _run_line_word_case(self, size, word):

    #puts `word` in the top row of an NxN grid, fills the rest with "X"
    
    grid = [list(word.upper())]
    for _ in range(size - 1):
      grid.append(["X"] * size)
    dictionary = [word.lower(), "zzz", "qqq"]
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    expected = [word.upper()]
    self.assertEqual(sorted(expected), sorted(solution))

  def test_Normal_case_4x4(self):
    self._run_line_word_case(4, "abcd")

  def test_Normal_case_5x5(self):
    self._run_line_word_case(5, "abcde")

  def test_Normal_case_6x6(self):
    self._run_line_word_case(6, "abcdef")

  def test_Normal_case_7x7(self):
    self._run_line_word_case(7, "abcdefg")

  def test_Normal_case_8x8(self):
    self._run_line_word_case(8, "abcdefgh")

  def test_Normal_case_9x9 (self):
    self._run_line_word_case(9, "abcdefghi")

  def test_Normal_case_10x10(self):
    self._run_line_word_case(10, "abcdefghij")
 
  def test_Normal_case_11x11(self):
    self._run_line_word_case(11, "abcdefghijk")

  def test_Normal_case_12x12(self):
    self._run_line_word_case(12, "abcdefghijkl")
    
  def test_Normal_case_13x13(self):
    self._run_line_word_case(13, "abcdefghijklm")

  def test_Larger_grid_15x15_with_larger_dictionary(self):
    size = 15
    word = "abcdefghijklmno"
    grid = [list(word.upper())]
    for _ in range(size - 1):
      grid.append(["X"] * size)

  # bigger dictionary of words not in the grid, to test with more to check
    
    decoys = [f"decoy{i}" for i in range(30)]
    dictionary = [word] + decoys
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    self.assertEqual([word.upper()], solution)


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

  def test_SquareGrid_case_1x1(self):
    grid = [["A"]]
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_EmptyGrid_case_0x0(self):

    # a grid with no columns is technically valid, but has no tiles to search
    
    grid = [[]]
    dictionary = ["hello", "there", "general", "kenobi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  def test_SingleRow_grid(self):
    grid = [["C", "A", "T", "S"]]
    dictionary = ["cat", "cats"]
    mygame = Boggle(grid, dictionary)
    solution = sorted(w.upper() for w in mygame.getSolution())
    expected = sorted(["CAT", "CATS"])
    self.assertEqual(expected, solution)

  def test_SingleColumn_grid(self):
    grid = [["C"], ["A"], ["T"]]
    dictionary = ["cat"]
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    self.assertEqual(["CAT"], solution)

  def test_AllSameLetter_grid(self):
    grid = [["A", "A"], ["A", "A"]]
    dictionary = ["aaa", "aaaa"]
    mygame = Boggle(grid, dictionary)
    solution = sorted(w.upper() for w in mygame.getSolution())
    expected = sorted(["AAA", "AAAA"])
    self.assertEqual(expected, solution)

  def test_NoMatchingWords_atAll(self):
    grid = [["C", "A", "T"]]
    dictionary = ["dog", "fish"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    self.assertEqual([], solution)

  def test_WordShorterThanThreeLetters_isIgnored(self):

    # words must be at least 3 letters to count

    grid = [["A", "T"]]
    dictionary = ["at"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    self.assertEqual([], solution)

class TestSuite_Complete_Coverage(unittest.TestCase):

  def test_diagonal_adjacency_word(self):

    # diagonal tiles count as adjacent, not just up/down/left/right
    
    grid = [["C", "A"], ["T", "X"]]
    dictionary = ["cat"]  
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    self.assertEqual(["CAT"], solution)

  def test_word_found_via_two_paths_is_not_duplicated(self):

    # same word is spellable two different ways here, should still appear once
    
    grid = [["A", "B"], ["A", "B"]]
    dictionary = ["aab"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    self.assertEqual(solution.count("aab"), 1)

  def test_tile_cannot_be_reused_in_same_path(self):

    # "ABA" needs tile (0,0) twice, which isn't allowed

    grid = [["A", "B"]]
    dictionary = ["aba"]
    mygame = Boggle(grid, dictionary)
    self.assertEqual([], mygame.getSolution())

  def test_non_square_rectangular_grid(self):
    grid = [["C", "A", "T"], ["X", "X", "X"]]
    dictionary = ["cat"]
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    self.assertEqual(["CAT"], solution)

  def test_multiple_words_all_returned(self):
    grid = [["C", "A", "T", "S"]]
    dictionary = ["cat", "cats", "at"]
    mygame = Boggle(grid, dictionary)
    solution = sorted(w.upper() for w in mygame.getSolution())
    expected = sorted(["CAT", "CATS"])
    self.assertEqual(expected, solution)
  
class TestSuite_Qu_and_St(unittest.TestCase):

  def test_Qu_tile_forms_word_with_adjacent_tile(self):

    # "Qu" tile counts as the two letters Q and U together
    
    grid = [["Qu", "A"], ["X", "X"]]
    dictionary = ["qua"]
    mygame = Boggle(grid, dictionary)
    solution = [w.upper() for w in mygame.getSolution()]
    self.assertEqual(["QUA"], solution)
  
  def test_Qu_tile_does_not_match_word_starting_with_single_Q(self):

    # tile always contributes "QU", so it can't spell a word starting with just "Q"
    
    grid = [["Qu", "A"], ["X", "X"]]
    dictionary = ["qat"]
    mygame = Boggle(grid, dictionary)
    self.assertEqual([], mygame.getSolution())

  def test_St_and_Qu_tiles_together_in_one_grid(self):
    grid = [["St", "Qu"], ["A", "R"]]
    dictionary = ["star", "stqua", "qua", "art"]
    mygame = Boggle(grid, dictionary)
    solution = sorted(w.upper() for w in mygame.getSolution())
    # "art" can't be spelled: there's no separate T tile
    expected = sorted(["STAR", "STQUA", "QUA"])
    self.assertEqual(expected, solution)

if __name__ == '__main__':
  unittest.main()




  
