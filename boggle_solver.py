class Boggle:
  def __init__(self, grid=None, dictionary=None):
    self.grid = []
    self.dictionary = []
    self.solution = []

    if grid is not None:
      self.setGrid(grid)
    if dictionary is not None:
      self.setDictionary(dictionary)


  def setGrid(self, grid):
    if self._is_valid_grid(grid):
      self.grid = grid
    else:
      self.grid = []


  def getGrid(self):
    return self.grid

  def setDictionary(self, dictionary):
    if self._is_valid_dictionary(dictionary):
      self.dictionary = dictionary
    else:
      self.dictionary = []

  def getDictionary(self):
    return self.dictionary

  def getSolution(self):
    # if the grid or dictionary are bad, just give back nothing
    if not self._is_valid_grid(self.grid) or not self._is_valid_dictionary(self.dictionary):
      self.solution = []
      return self.solution

    # reset solution in case this gets called more than once
    self.solution = []
    self._solve()
    return self.solution

  def _is_valid_grid(self, grid):
    # grid must be a non-empty list of lists, all the same length,
    # made up of non-empty strings
    if not isinstance(grid, list) or len(grid) == 0:
      return False

    row_length = len(grid[0])

    for row in grid:
      if not isinstance(row, list) or len(row) != row_length:
        return False

      for tile in row:
        if not isinstance(tile, str) or len(tile) == 0:
          return False

    return True


  def _is_valid_dictionary(self, dictionary):
    # dictionary must be a non-empty list of non-empty strings
    if not isinstance(dictionary, list) or len(dictionary) == 0:
      return False

    for word in dictionary:
      if not isinstance(word, str) or len(word) == 0:
        return False

    return True

  def _word_could_still_match(self, path):
    # check if ANY word in the dictionary starts with what we've spelled so far
    # if nothing does, there's no point continuing this path
    for word in self.dictionary:
      if word.upper().startswith(path):
        return True
    return False

  def _get_matching_word(self, path):
    # check if path is exactly equal to a dictionary word (ignoring case)
    # return the word as it was originally written, or None if no match
    for word in self.dictionary:
      if word.upper() == path:
        return word
    return None

  def _solve(self):
    # try starting a search from every tile in the grid
    num_rows = len(self.grid)
    num_cols = len(self.grid[0])

    for row in range(num_rows):
      for col in range(num_cols):
        visited = set()
        self._search(row, col, "", visited, num_rows, num_cols)

  def _search(self, row, col, path_so_far, visited, num_rows, num_cols):
    # add this tile's letters onto the path built so far
    tile_letters = self.grid[row][col].upper()
    path = path_so_far + tile_letters

    # stop here if no word could possibly match this path
    if not self._word_could_still_match(path):
      return

    # words need to be at least 3 letters long to count
    if len(path) >= 3:
      matched_word = self._get_matching_word(path)
      if matched_word is not None and matched_word not in self.solution:
        self.solution.append(matched_word)

    # mark this tile as used for this path
    visited.add((row, col))

    # check all 8 neighboring tiles
    for row_change in (-1, 0, 1):
      for col_change in (-1, 0, 1):
        if row_change == 0 and col_change == 0:
          continue

        next_row = row + row_change
        next_col = col + col_change

        if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
          if (next_row, next_col) not in visited:
            self._search(next_row, next_col, path, visited, num_rows, num_cols)

    # un-mark this tile so it can be used again in a different path
    visited.remove((row, col))

def main():
  grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "St", "Qu", "R"],["O", "N", "T", "A"]]
  dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "rat", "tar", "tarp", "ten", "went", "wet", "stont", "stqura", "arty", "egg", "not"]

  mygame = Boggle(grid, dictionary)
  print(mygame.getSolution())

if __name__ == "__main__":
  main()