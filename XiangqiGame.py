# Name: John-Francis Caccamo
# Date: 3 / 12 / 20
# Description: This is the XiangqiGame.py file containing a Piece Super class with 7
# child classes holding the information about the piece moves and piece taking rules of the
# seven distinct pieces of Chinese Chess. It will also have a Xiangqi Board class
# that will display the board and carry out piece movements around the board,
# updating it with each new turn.

from abc import abstractmethod


class Piece:
    """
    The Piece super class
    """

    def __init__(self, color):
        """
        Initialization function taking in color and title as parameters, corresponding
        to the color and piece. Member variables location and piece will be initialized to
        default place holders
        """
        self.color = color
        self.location = "**"
        self.piece = "-"

    def set_location(self, loc):
        """
        Setter method taking string coordinates and assigning them to the location member variable.
        """
        self.location = loc

    def get_location(self):
        """
        getter of piece, returning the location
        """
        return self.location

    def __repr__(self):
        """
        The __repr__function will return the printable representation of a Piece object
        """
        return self.piece

    @abstractmethod
    def is_val_move(self, *args):
        """
        Abstract method will have initial check if the end coordinate is within the board. Each piece
        will have varying definitions of is_valid_move.
        """
        self.intervening_pieces = []  # will hold the intervening empty space and / or piece per move

    @abstractmethod
    def determine_obstruction(self, *args):
        """
        determine_obstruction is another abstract method that will determine if a piece's potential
        move is impeded by another piece. Each child class of Piece wil have its own definition
        of determine_obstruction
        """
        pass

    @abstractmethod
    def cannon_check_move(self, *args):
        """
        Abstract method that will determine if the end position is empty space or held by
        a friendly piece. Again, each class will have a different function implementation
        if the end_pos is held by enemy piece.
        """
        pass


class General(Piece):  # General Piece
    """
    The General class- child class of Piece. Will have an initialization function and
    move checking methods.
    """

    def __init__(self, color):  # inheriting from Piece super class with Super
        super().__init__(color)
        if color == "red":
            self.piece = u"\u2654"

        if color == "black":
            self.piece = u"\u265a"

    def is_val_move(self, xi_game, end_pos):
        """
        Generals's is_val_move - will take a XiangqiGame object and string coordinates
        as parameters.
        Will determine if  the move within the within palace boundaries and an orthogonal move of 1.
        """
        super().is_val_move()  # inheriting from Piece abstract method
        xi_board = xi_game.get_board()

        if end_pos in xi_game.get_red_palace() or end_pos in xi_game.get_black_palace():
            start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
            end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

            if (((abs(start_col - end_col) == 1) and start_row == end_row) or # if movement is 1 up, down, left, right
            ((abs(start_row - end_row) == 1) and start_col == end_col)):
                self.intervening_pieces.append(xi_board[end_row][end_col])

            if len(self.intervening_pieces) == 0:  # check if Piece hasn't moved at all
                return False
            if self.determine_obstruction(self.intervening_pieces): # call determine_obstruction
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the General move in question.
        """
        if intervening_pieces[0] != 0:
            if intervening_pieces[0].color == self.color:  # if end position is held by the same color
                return False

        return True


class Advisor(Piece):  # Advisor piece
    """
    The Advisor class - child class of Piece. Will have an intialization function and
    move checking methods.
    """
    def __init__(self, color):  # inheriting from Piece super class with Super
        super().__init__(color)
        if color == "red":
            self.piece = u"\u2655"

        if color == "black":
            self.piece = u"\u265b"

    def is_val_move(self, xi_game, end_pos):  # inheriting from Piece abstract method
        """
        Advisors's is_val_move, taking in a XiangqiGame object and end_pos as its parameters.
        It will determine whether the move is within palace boundaries and a diagonal move of 1.
        """
        super().is_val_move()  # inheriting from Piece abstract method
        xi_board = xi_game.get_board()

        if end_pos in xi_game.get_red_palace() or end_pos in xi_game.get_black_palace():
            start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
            end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

            if (abs(start_col - end_col) == 1) and (abs(start_row - end_row) == 1): # check for a diagonal move
                self.intervening_pieces.append(xi_board[end_row][end_col])

            if len(self.intervening_pieces) == 0: # if piece hasn't moved
                return False
            if self.determine_obstruction(self.intervening_pieces): # call determine_obstruction
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Advisor move in question.
        """
        if intervening_pieces[0] != 0:
            if intervening_pieces[0].color == self.color: # if board position is held by same color piece
                return False

        return True


class Elephant(Piece):  # Elephant piece
    """
    The Elephant class - child of Piece class. Will have an initialization function and
    move checking methods
    """
    def __init__(self, color):  # inhereting from Piece super class with Super
        super().__init__(color)
        if color == "red":
            self.piece = u"\u2657"

        if color == "black":
            self.piece = u"\u265d"

    def is_val_move(self, xi_game, end_pos):
        """
        Will take a XiangqiGame object and an end_pos as its parameters.
        Elephants confined to their respective sides of river. Can jump 2 squares diagonally.
        """
        super().is_val_move()  # inheriting from Piece abstract method
        xi_board = xi_game.get_board()

        start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
        end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

        if self.color == "red":
            if end_row > 4:  # red elephant must stay on north side of river
                return False
            if abs(start_col - end_col) == 2 and abs(start_row - end_row) == 2:

                if start_row - end_row == 2 and start_col - end_col == 2:  # jump up, left
                    self.intervening_pieces.append(xi_board[start_row - 1][start_col - 1])

                if start_row - end_row == 2 and start_col - end_col == -2:  # jump up, right
                    self.intervening_pieces.append(xi_board[start_row - 1][start_col + 1])

                if start_row - end_row == -2 and start_col - end_col == 2:  # jump down, left
                    self.intervening_pieces.append(xi_board[start_row + 1][start_col - 1])

                if start_row - end_row == -2 and start_col - end_col == -2:  # jump down, right
                    self.intervening_pieces.append(xi_board[start_row + 1][start_col + 1])

                self.intervening_pieces.append(xi_board[end_row][end_col])

            if len(self.intervening_pieces) == 0: # check if no movement took place
                return False
            if self.determine_obstruction(self.intervening_pieces):
                return True

        if self.color == "black":
            if end_row < 5:  # black elephant must stay on south side of river
                return False
            if abs(start_col - end_col) == 2 and abs(start_row - end_row) == 2:

                if start_row - end_row == 2 and start_col - end_col == 2:  # jump up, left
                    self.intervening_pieces.append(xi_board[start_row - 1][start_col - 1])

                if start_row - end_row == 2 and start_col - end_col == -2:  # jump up, right
                    self.intervening_pieces.append(xi_board[start_row - 1][start_col + 1])

                if start_row - end_row == -2 and start_col - end_col == 2:  # jump down, left
                    self.intervening_pieces.append(xi_board[start_row + 1][start_col - 1])

                if start_row - end_row == -2 and start_col - end_col == -2:  # jump down, right
                    self.intervening_pieces.append(xi_board[start_row + 1][start_col + 1])

                self.intervening_pieces.append(xi_board[end_row][end_col])

            if len(self.intervening_pieces) == 0: # check if no movement took place
                return False
            if self.determine_obstruction(self.intervening_pieces): # call determine_obstruction
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Elephant move in question.
        """
        if intervening_pieces[0] != 0: # determine if the elephant's eye is blocked
            return False
        elif intervening_pieces[-1] != 0 and intervening_pieces[-1].color == self.color:
            return False
        else:
            return True


class Horse(Piece):
    """
    The Horse Class inheriting from Piece. Can jump one point orthogonally and one point
    diagonally as long as it is not blocked
    """

    def __init__(self, color):
        super().__init__(color)  # inhereting from Piece super class with Super
        if color == "red":
            self.piece = u"\u2658"

        if color == "black":
            self.piece = u"\u265e"

    def is_val_move(self, xi_game, end_pos):
        """
        is_val_move will take a XiangqiGame object and an end_pos as parameters.
        Horse Can jump one point orthogonally and one point diagonally as long as it is not blocked
        """
        super().is_val_move()  # inheriting from Piece abstract method
        xi_board = xi_game.get_board()

        start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
        end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

        if ((abs(start_col - end_col) == 1 and abs(start_row - end_row) == 2) or
                (abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1)):

            if start_row - end_row == 2:  # jumping up 2 rows
                self.intervening_pieces.append(xi_board[start_row - 1][start_col])  # orthogonal pos

            if start_row - end_row == -2:  # jumping down 2 rows
                self.intervening_pieces.append(xi_board[start_row + 1][start_col])  # orthogonal pos

            if start_col - end_col == 2:  # jumping left 2 columns
                self.intervening_pieces.append(xi_board[start_row][start_col - 1])  # orthogonal pos

            if start_col - end_col == -2:  # jumping right 2 columns
                self.intervening_pieces.append(xi_board[start_row][start_col + 1])  # orthogonal pos

            self.intervening_pieces.append(xi_board[end_row][end_col])

            if len(self.intervening_pieces) == 0:
                return False
            if self.determine_obstruction(self.intervening_pieces):
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Horse move in question.
        """
        if intervening_pieces[0] != 0: # if the horse is blocked
            return False
        elif intervening_pieces[-1] != 0 and intervening_pieces[-1].color == self.color: # end coord held by same color
            return False
        else:
            return True


class Chariot(Piece):
    """
    The Chariot child class inheriting from Piece superclass.
    """
    def __init__(self, color):
        super().__init__(color)  # inheriting from Piece super class with Super
        if color == "red":
            self.piece = u"\u2656"

        if color == "black":
            self.piece = u"\u265c"

    def is_val_move(self, game, end_pos):  # inheriting from Piece abstract method
        """
        is_val_move will take a XiangqiGame object and a string coordinate as parameters.
        Chariot can move anywhere vertically or horizontally from its start position as long as it is not blocked.
        """
        super().is_val_move()
        xi_board = game.get_board()

        start_row, start_col = game.convert_to_int(self.location)  # obtain start location col, row
        end_row, end_col = game.convert_to_int(end_pos)  # obtain end location col, row

        if (start_row == end_row) ^ (start_col == end_col): # XOR with ^
            if start_row == end_row: # if start row and end row are the same
                col_spaces = abs(start_col - end_col)
                if start_col > end_col:  # chariot moving left
                    for i in range(1, col_spaces):
                        self.intervening_pieces.append(xi_board[end_row][start_col - i])
                else:  # chariot moving right
                    for i in range(1, col_spaces):
                        self.intervening_pieces.append(xi_board[end_row][start_col + i])

            elif start_col == end_col: # if start col and end col are the same
                row_spaces = abs(start_row - end_row)
                if start_row > end_row:  # chariot moving up:
                    for i in range(1, row_spaces):
                        self.intervening_pieces.append(xi_board[start_row - i][end_col])
                else:  # chariot moving down
                    for i in range(1, row_spaces):
                        self.intervening_pieces.append(xi_board[start_row + i][end_col])

            self.intervening_pieces.append(xi_board[end_row][end_col]) # append the end pos

            if len(self.intervening_pieces) == 0: # if the same coordinate passed
                return False
            if self.determine_obstruction(self.intervening_pieces): # call determine_obstruction
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Chariot move in question.
        """
        for i in intervening_pieces[0:-1]:
            if issubclass(type(i), Piece): # determine if there is a block along the move
                return False
        if intervening_pieces[-1] != 0 and intervening_pieces[-1].color == self.color: # if the end_piece is same color
            return False
        else:
            return True


class Cannon(Piece):
    """
    The Cannon inheriting from Class Piece. Will have an intializer and move checking methods.
    """
    def __init__(self, color):
        super().__init__(color)  # inheriting from Piece super class with Super
        if color == "red":
            self.piece = u"\uFA65"

        if color == "black":
            self.piece = u"\uFA6C"

    def is_val_move(self, xi_game, end_pos):  # inheriting from Piece abstract method
        """
        is_val_move will take a XiangqiGame object and an end_pos as paranmeters.
        Has the ability to move like the chariot but needs to perform a jump of a
        piece along the path of attack to capture.
        """
        super().is_val_move()
        xi_board = xi_game.get_board()

        start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
        end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

        if (start_row == end_row) ^ (start_col == end_col):
            if start_row == end_row:
                col_spaces = abs(start_col - end_col)
                if start_col > end_col:  # cannon moving left
                    for i in range(1, col_spaces):
                        self.intervening_pieces.append(xi_board[end_row][start_col - i])
                else:  # cannon moving right
                    for i in range(1, col_spaces):
                        self.intervening_pieces.append(xi_board[end_row][start_col + i])

            elif start_col == end_col:
                row_spaces = abs(start_row - end_row)
                if start_row > end_row:  # cannon moving up:
                    for i in range(1, row_spaces):
                        self.intervening_pieces.append(xi_board[start_row - i][end_col])
                else:  # cannon moving down
                    for i in range(1, row_spaces):
                        self.intervening_pieces.append(xi_board[start_row + i][end_col])

            self.intervening_pieces.append(xi_board[end_row][end_col]) # append the final position

            if self.determine_obstruction(self.intervening_pieces):
                return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Cannon move in question.
        """
        piece_count = 0
        can_to_targ = intervening_pieces[0:-1] # splice out from start to 1 before the finish
        for i in can_to_targ:
            if issubclass(type(i), Piece): # see if a Piece is along the path of attack
                piece_count += 1
        if piece_count > 2: # cant jump over 2 pieces
            return False
        if intervening_pieces[-1] != 0 and intervening_pieces[-1].color == self.color: # same color at final pos
            return False
        else:
            if len(self.intervening_pieces) == 0: # if Cannon has not moved
                return False
            if self.cannon_check_move(intervening_pieces, piece_count): # call cannon_check_move
                return True

        return False

    def cannon_check_move(self, intervening_pieces, piece_count):
        """
        The cannon_check_move method
        """
        if (piece_count == 0) and (intervening_pieces[-1] == 0): # if no Pieces along the way
            return True
        else: # if there was a piece jumped and the final position is held by opposing color
            if piece_count == 1 and intervening_pieces[-1] != 0 and intervening_pieces[-1].color != self.color:
                return True

        return False


class Soldier(Piece):
    """
    The Soldier child class of Piece
    """
    def __init__(self, color):
        super().__init__(color)
        if color == "red":
            self.piece = u"\u2659"

        if color == "black":
            self.piece = u"\u265f"

    def is_val_move(self, xi_game, end_pos):
        """
        is_val_move will take a XiangqiGame object and string coordinate parameters.
        The soldier is_val_move will have a check to determine if the soldier is on the
        other color's side of the river - once crossed the soldier has the ability to move
        horizontally but can only proceed up the board.
        """
        super().is_val_move()  # inheriting from Piece abstract method
        xi_board = xi_game.get_board()

        start_row, start_col = xi_game.convert_to_int(self.location)  # obtain start location col, row
        end_row, end_col = xi_game.convert_to_int(end_pos)  # obtain end location col, row

        if self.color == "red":
            if start_row < 5:  # if red soldier is still on red's side of river
                if start_col == end_col and end_row == start_row + 1:
                    self.intervening_pieces.append(xi_board[end_row][end_col])

            elif start_row >= 5:  # if red soldier is on black's side of river
                if (((abs(start_col - end_col) == 1) and end_row == start_row) or
                ((start_col - end_col == 0) and end_row == start_row + 1)):
                    self.intervening_pieces.append(xi_board[end_row][end_col])

        elif self.color == "black":
            if start_row > 4:  # if black soldier is still on black's side of river
                if start_col == end_col and end_row == start_row - 1:
                    self.intervening_pieces.append(xi_board[end_row][end_col])

            elif start_row <= 4:  # if black soldier is on red's side of river
                if (((abs(start_col - end_col) == 1) and end_row == start_row) or
                ((start_col - end_col == 0) and end_row == start_row - 1)):
                    self.intervening_pieces.append(xi_board[end_row][end_col])

        if len(self.intervening_pieces) == 0: # if Soldier has not moved
            return False
        if self.determine_obstruction(self.intervening_pieces):
            return True

        return False

    def determine_obstruction(self, intervening_pieces):
        """
        check to determine the intervening pieces within the Soldier move in question.
        """
        if intervening_pieces[0] != 0:
            if intervening_pieces[0].color == self.color: # if end position is held by the same color
                return False

        return True


class XiangqiGame:
    """
    The XiangqiGame class will have an initialization function. It will also static
    methods determining if a coord parameter is within the boundaries of the board and
    convert the string coordinate to integer coordinates which will be used as
    checks within the Piece class. It will also have a get_game_state getter
    returning the game state, a is_in_check function to determine if black or red is in check
    and a make_move method that will carry out a legal Piece move to a new coordinate.
    """

    def __init__(self):
        """
        The initialization function of the XiangqiGame, initializing the game board, the string
        coordinates of the board, the two players, the game_state and the check status.
        """
        self.xi_ob_board = [[0 for i in range(9)] for j in range(10)]  # initialzing the 10 rows x 9 cols board to 0
        self.xi_str_coords = [str(chr(i)) + str(j) for i in range(97, 106) for j in range(1, 11)]  # list of coords

        self.x_axis_range = [chr(x) for x in range(ord("a"), ord("j"))]
        self.y_axis_range = [x for x in range(1, 11)]

        self.red_palace = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"] # coords of the red palace
        self.black_palace = ["d10", "e10", "e11", "d9", "e9", "f9", "d8", "e8", "f8"] # coords of the black palace

        self.current_player = "red"
        self.waiter_player = "black"

        self.game_state = "UNFINISHED"
        self.in_check = False
        self.in_check_color = ""

        self.red_gen = General("red")
        self.xi_ob_board[0][4] = self.red_gen
        self.red_gen.set_location("e1")  # red general

        self.black_gen = General("black")
        self.xi_ob_board[9][4] = self.black_gen
        self.black_gen.set_location("e10")  # black general

        # ("d10", "f10")  # initialize board grid with red advisors

        self.red_adv1 = Advisor("red")
        self.xi_ob_board[0][3] = self.red_adv1
        self.red_adv1.set_location("d1")

        self.red_adv2 = Advisor("red")
        self.xi_ob_board[0][5] = self.red_adv2
        self.red_adv2.set_location("f1")

        # ("d10", "f10")  # initialize board grid with black advisors

        self.blk_adv1 = Advisor("black")
        self.xi_ob_board[9][3] = self.blk_adv1
        self.blk_adv1.set_location("d10")

        self.blk_adv2 = Advisor("black")
        self.xi_ob_board[9][5] = self.blk_adv2
        self.blk_adv2.set_location("f10")

        # ("c1", "g1")  # initialize board grid with red elephants

        self.red_ele1 = Elephant("red")
        self.xi_ob_board[0][2] = self.red_ele1
        self.red_ele1.set_location("c1")

        self.red_ele2 = Elephant("red")
        self.xi_ob_board[0][6] = self.red_ele2
        self.red_ele2.set_location("g1")

        # ("c10", "g10")  # initialize board grid with black elephants

        self.blk_ele1 = Elephant("black")
        self.xi_ob_board[9][2] = self.blk_ele1
        self.blk_ele1.set_location("c10")

        self.blk_ele2 = Elephant("black")
        self.xi_ob_board[9][6] = self.blk_ele2
        self.blk_ele2.set_location("g10")

        # ("b1", "h1")  # initialize board grid with black horse

        self.red_horse1 = Horse("red")
        self.xi_ob_board[0][1] = self.red_horse1
        self.red_horse1.set_location("b1")

        self.red_horse2 = Horse("red")
        self.xi_ob_board[0][7] = self.red_horse2
        self.red_horse2.set_location("h1")

        # ("b10", "h10")  # initialize board grid with black horse

        self.blk_horse1 = Horse("black")
        self.xi_ob_board[9][1] = self.blk_horse1
        self.blk_horse1.set_location("b10")

        self.blk_horse2 = Horse("black")
        self.xi_ob_board[9][7] = self.blk_horse2
        self.blk_horse2.set_location("h10")

        # ("a1", "i1")  # initialize board grid with red chariots

        self.red_char1 = Chariot("red")
        self.xi_ob_board[0][0] = self.red_char1
        self.red_char1.set_location("a1")

        self.red_char2 = Chariot("red")
        self.xi_ob_board[0][8] = self.red_char2
        self.red_char2.set_location("i1")

        # ("a10", "i10")  # initialize board grid with black chariots

        self.blk_char1 = Chariot("black")
        self.xi_ob_board[9][0] = self.blk_char1
        self.blk_char1.set_location("a10")

        self.blk_char2 = Chariot("black")
        self.xi_ob_board[9][8] = self.blk_char2
        self.blk_char2.set_location("i10")

        # ("b3", "h3")  # initialize board grid with red cannons

        self.red_can1 = Cannon("red")
        self.xi_ob_board[2][1] = self.red_can1
        self.red_can1.set_location("b3")

        self.red_can2 = Cannon("red")
        self.xi_ob_board[2][7] = self.red_can2
        self.red_can2.set_location("h3")

        # ("b8", "h8")  # initialize board grid with black cannons

        self.blk_can1 = Cannon("black")
        self.xi_ob_board[7][1] = self.blk_can1
        self.blk_can1.set_location("b8")

        self.blk_can2 = Cannon("black")
        self.xi_ob_board[7][7] = self.blk_can2
        self.blk_can2.set_location("h8")

        # ("a4", "c4", "e4", "g4", "i4")  # initialize board grid with red soldiers

        self.red_sold1 = Soldier("red")
        self.xi_ob_board[3][0] = self.red_sold1
        self.red_sold1.set_location("a4")

        self.red_sold2 = Soldier("red")
        self.xi_ob_board[3][2] = self.red_sold2
        self.red_sold2.set_location("c4")

        self.red_sold3 = Soldier("red")
        self.xi_ob_board[3][4] = self.red_sold3
        self.red_sold3.set_location("e4")

        self.red_sold4 = Soldier("red")
        self.xi_ob_board[3][6] = self.red_sold4
        self.red_sold4.set_location("g4")

        self.red_sold5 = Soldier("red")
        self.xi_ob_board[3][8] = self.red_sold5
        self.red_sold5.set_location("i4")

        # ("a7", "c7", "e7", "g7", "i7")  # initialize board grid with black soldiers

        self.blk_sold1 = Soldier("black")
        self.xi_ob_board[6][0] = self.blk_sold1
        self.blk_sold1.set_location("a7")

        self.blk_sold2 = Soldier("black")
        self.xi_ob_board[6][2] = self.blk_sold2
        self.blk_sold2.set_location("c7")

        self.blk_sold3 = Soldier("black")
        self.xi_ob_board[6][4] = self.blk_sold3
        self.blk_sold3.set_location("e7")

        self.blk_sold4 = Soldier("black")
        self.xi_ob_board[6][6] = self.blk_sold4
        self.blk_sold4.set_location("g7")

        self.blk_sold5 = Soldier("black")
        self.xi_ob_board[6][8] = self.blk_sold5
        self.blk_sold5.set_location("i7")

    def get_red_palace(self):
        """
        getter of the red palace
        """
        return self.red_palace

    def get_black_palace(self):
        """
        getter of the black palace
        """
        return self.black_palace

    def get_board(self):
        """
        getter of the game board
        """
        return self.xi_ob_board

    def in_board_coord(self, coord):
        """
        method that will be utilized in the Piece class and make
        move method. Will check if a coord_param corresponds to legal bord coordinates.
        """
        col = coord[0]
        row = int(coord[1:])

        if col in self.x_axis_range and row in self.y_axis_range:
            return True
        return False

    @staticmethod
    def convert_to_int(coord):
        """
        static method that will convert string coordinates to integer coordinates From (0,0)
        in bottom left corner to (8,9) in top right corner. Will return tuple of ints
        """
        col = coord[0]
        row = coord[1:]

        return int(row) - 1, ord(col) - 97

    @staticmethod
    def convert_to_string(row, col):
        """
        static method will be utilized to change integer inputs representing the column and row
        to string representations. Will return concatenated string.
        """
        return chr(col + 97) + str(row + 1)

    def get_game_state(self):
        """
        game_state getter
        """
        return self.game_state

    def is_in_check(self, color):  # check to determine if general is_in_check
        """
        is_in_check method will take a string color parameter and return True if that
        player's color in in check.
        """
        if color == "red" and self.in_check_color == "red":  # and self.red_in_check == True:
            return True
        elif color == "black" and self.in_check_color == "black":  # and self.black_in_check == True:
            return True
        else:
            return False

    def general_sight(self, piece_ob, end_row, end_col):
        """
        This function will serve as a check in the make_move function determining
        if the general's will see each other. If so, the function will return False
        preventing the move.
        """
        red_gen_row, red_gen_col = self.convert_to_int(self.red_gen.get_location()) # get red_general's location
        black_gen_row, black_gen_col = self.convert_to_int(self.black_gen.get_location()) # get black general's location

        if red_gen_col == black_gen_col: # if the red and black general are in the same column
            board_copy = [x[:] for x in self.xi_ob_board]  # create a copy of the game board
            piece_row, piece_col = self.convert_to_int(piece_ob.get_location())
            board_copy[end_row][end_col] = piece_ob # initialize Piece object to the board copy to potential move
            board_copy[piece_row][piece_col] = 0

            general_col = [row[red_gen_col] for row in board_copy]
            count = 0
            i = 1

            while general_col[i] != self.black_gen: # discover what lies between the generals
                if general_col[i] != 0:  # determine if Pieces lie between the generals
                    count += 1
                i += 1
            if count == 0:  # if there is no Piece between the two generals, return False
                return False

        return True

    def get_red_moves(self):
        """
        This function will determine from all red Pieces left in the game if an attack
        against the black General is possible.
        """
        for row in self.get_board():
            for coord in row:
                if coord != 0:
                    if coord.color == "red":
                        if coord.is_val_move(self, self.black_gen.get_location()): # if the black Gen is vulnerable
                            return True

        return False


    def get_black_moves(self):
        """
        This function will determine from all black Pieces left in the game if an attack
        against the red General is possible.
        """
        for row in self.get_board():
            for coord in row:
                if coord != 0:
                    if coord.color == "black":
                        if coord.is_val_move(self, self.red_gen.get_location()): # if the red Gen is vulnerable
                            return True

        return False

    def general_exposer(self, piece_ob, end_row, end_col):
        """
        This function will occur before a move has been made.
        The general exposer will make a copy of the current game_board state and determine
        the repurcussions of a Piece's move by calling get_red_moves and get_black_moves.
        If there currently is no player in check and if a move leaves the current player
        in check, the function will preclude the move and return False.
        IF there is a player in check and if the player can't escape check, this function
        will conclude the game and determine that the other player has won.
        """
        not_exposed = True # boolean will hold the value of the General exposer
        start_row, start_col = self.convert_to_int(piece_ob.get_location())

        self.xi_ob_board[end_row][end_col] = piece_ob # test a Piece's move
        piece_ob.set_location(self.convert_to_string(end_row, end_col))
        self.xi_ob_board[start_row][start_col] = 0

        if not self.in_check:  # if there is no player in check
            if piece_ob.color == "red": # if current player Piece is red
                if self.get_black_moves(): # obtain the black moves
                    not_exposed = False # change boolean

            elif piece_ob.color == "black":  # if current player Piece is black
                if self.get_red_moves(): # obtain the red moves
                    not_exposed = False # change boolean

        else:  # if there is a player in check
            if piece_ob.color == "red":
                if self.get_black_moves(): # if a potential move still leaves red in check
                    self.game_state = "BLACK_WON" # black wins

            elif piece_ob.color == "black":
                if self.get_red_moves(): # if a potential move still leaves black in check
                    self.game_state = "RED_WON" # red wins

        self.xi_ob_board[start_row][start_col] = piece_ob # reinitialize piece to original position
        piece_ob.set_location(self.convert_to_string(start_row, start_col))
        self.xi_ob_board[end_row][end_col] = 0

        return not_exposed

    def general_defence(self, piece_ob, end_row, end_col):
        """
        The general_defense method will serve as a check before a move is made for players
        in check to come to the aid and either move the General to safety or block him.
        The method will take a Piece object and end_row, end_col integer parameters.
        """
        gen_defended = True # boolean will hold the value of the General defense
        start_row, start_col = self.convert_to_int(piece_ob.get_location())

        self.xi_ob_board[end_row][end_col] = piece_ob # test a Piece's move
        piece_ob.set_location(self.convert_to_string(end_row, end_col))
        self.xi_ob_board[start_row][start_col] = 0

        if piece_ob.color == "red": # if player is red
            if self.get_black_moves(): # if the move hasn't protected their General
                gen_defended = False

        elif piece_ob.color == "black": # if player is black
            if self.get_red_moves(): # if the move hasn't protected their General
                gen_defended = False

        self.xi_ob_board[start_row][start_col] = piece_ob # reinitialize piece to original position
        piece_ob.set_location(self.convert_to_string(start_row, start_col))
        self.xi_ob_board[end_row][end_col] = 0

        return gen_defended

    def determine_check(self):
        """
        The determine_check will occur after the move has been made, subjecting the
        waiting_player to force defence of their general.
        """
        if self.current_player == "red":
            if self.get_red_moves():
                self.in_check = True
                self.in_check_color = "black"
                return "Black is in check! Move to defend your general!"
        else:
            if self.get_black_moves():
                self.in_check = True
                self.in_check_color = "red"
                return "Red is in check! Move to defend your general!"

    def make_move(self, start_pos, end_pos):
        """
        make_move method checking if game_state is still unfinished, the start_pos and
        end_pos are legal board moves and subsequent checks to see if piece belongs to
        the current_player and if a move is legal. If these checks are met, the piece
        will be moved and the current_player will update.
        """
        if self.game_state != "UNFINISHED":  # if game_state not finished
            return False
        if (not self.in_board_coord(start_pos)) or (not self.in_board_coord(end_pos)):  # see if coords are in board
            return False
        start_coord = self.convert_to_int(start_pos) # convert coord to int, return tuple of ints
        start_row = start_coord[0] # first index of tuple in start_row
        start_col = start_coord[1] # second index of tuple in start_col
        piece_at_pos = self.xi_ob_board[start_row][start_col]

        if not issubclass(type(piece_at_pos), Piece):  # see if a Piece is at the spot
            return False
        elif piece_at_pos.color != self.current_player:  # if piece doesnt; belong to current player
            return False

        if piece_at_pos.is_val_move(self, end_pos): # pass in XiangqiGame object and end_pos
            end_coord = self.convert_to_int(end_pos) # convert to tuple
            end_row = end_coord[0] # first index of tuple in end_row
            end_col = end_coord[1] # second index of tuple in end_col

            if not self.general_sight(piece_at_pos, end_row, end_col): # see if general sight
                return False
            if not self.general_exposer(piece_at_pos, end_row, end_col): # see if move exposes general to check
                return False

            if self.current_player == self.in_check_color: # if player is in check and doesn't perform move
                if not self.general_defence(piece_at_pos, end_row, end_col): # to defend their General
                    return False

            self.xi_ob_board[end_row][end_col] = piece_at_pos  # update the board
            piece_at_pos.set_location(end_pos) # update the location
            self.xi_ob_board[start_row][start_col] = 0 # fill in the original location with 0 - empty space

            if self.current_player == self.in_check_color:  # take the current_player out of check
                self.in_check = False
                self.in_check_color = ""

            self.determine_check()  # determine if waiter_player is in check

            self.current_player, self.waiter_player = self.waiter_player, self.current_player  # swap players

            return True
        return False


def main():
    xi = XiangqiGame()

    xi.make_move("a1", "a2")
    xi.make_move("e7", "e6")
    xi.make_move("a2", "e2")
    xi.make_move("e6", "e5")
    xi.make_move("a4", "a5")
    xi.make_move("e5", "e4")
    xi.make_move("i4", "i5")
    xi.make_move("e4", "d4") # cant move soldier - exposes general
    xi.make_move("a7", "a6")
    xi.make_move("b3", "e3")
    xi.make_move("d10", "e9")
    xi.make_move("e3", "e9")
    xi.make_move("i7", "i6")
    xi.make_move("e2", "e4")
    xi.make_move("c7", "c6")
    xi.make_move("i1", "i2")
    xi.make_move("g7", "g6")
    xi.make_move("i2", "d2")
    xi.make_move("c6", "c5")
    xi.make_move("g4", "g5")
    xi.make_move("h8", "i8")
    xi.make_move("g5", "g6")
    xi.make_move("i8", "h8")
    xi.make_move("g6", "f6")
    xi.make_move("b8", "a8")
    xi.make_move("h3", "e3")
    xi.make_move("a8", "b8")
    xi.make_move("e9", "a9")
    #xi.make_move("b8", "a8")
    #xi.make_move("f10", "e9")
    #xi.make_move("e1", "e2") # attempt general jump

    print(xi.is_in_check("black"))
    print(xi.get_game_state())
    print(xi.current_player)

    """#check general sight, check and checkmate
    xi.make_move("e4", "e5")
    xi.make_move("e7", "e6")
    xi.make_move("e5", "e6")
    xi.make_move("a7", "a6")
    xi.make_move("h3", "e3")
    #xi.make_move("a6", "a5")
    print(xi.is_in_check("black"))
    print(xi.current_player)"""

    # soldier testing = good!!!!!!!!!
    """xi.make_move("a4", "a5")
    xi.make_move("i7", "i6")
    xi.make_move("a5", "a6")
    xi.make_move("i6", "i5")
    xi.make_move("a6", "b6")
    xi.make_move("i5", "h5")
    xi.make_move("c4", "c5")
    xi.make_move("c7", "c6")
    xi.make_move("c5", "c6")
    xi.make_move("h5", "g5")
    xi.make_move("c6", "b6")
    print(xi.current_player)"""

    """#cannon testing- good
    xi.make_move("b3", "g3")
    xi.make_move("h8", "c8")
    xi.make_move("h3", "h10")
    xi.make_move("g3", "g7")
    xi.make_move("c8", "c4")
    xi.make_move("g7", "d7")
    xi.make_move("g7", "g1")
    xi.make_move("g7", "b7")
    xi.make_move("g7", "c7")
    xi.make_move("c4", "f4")
    xi.make_move("c4", "g4")
    print(xi.current_player)"""

    """#chariot looking good
    xi.make_move("a1", "a2")
    xi.make_move("i10", "i9")
    xi.make_move("a2", "d2")
    xi.make_move("i9", "f9")
    xi.make_move("d2", "d10")
    xi.make_move("f9", "f1")
    print(xi.current_player)"""

    """"#horse - looking goood 
    xi.make_move("b1", "c3")
    xi.make_move("h10", "g8")
    xi.make_move("c3", "e2")
    xi.make_move("g8", "e9")
    xi.make_move("e2", "d4")
    xi.make_move("e9", "d7")
    xi.make_move("d4", "c6")
    xi.make_move("d7", "c5")
    xi.make_move("c6", "a7")
    xi.make_move("c5", "a4")
    print(xi.current_player)"""

    """#elephant -- good!
    xi.make_move("c1", "a3")
    xi.make_move("c10", "a8")
    #xi.make_move("a3", "c5")
    #xi.make_move("a8", "c6")
    #xi.make_move("a4", "a5")
    #xi.make_move("c6", "a4")
    xi.make_move("c4", "c5")
    xi.make_move("i7", "i6")
    xi.make_move("c5", "c6")
    xi.make_move("i6", "i5")
    xi.make_move("a8", "c6")
    xi.make_move("e4", "e5")
    xi.make_move("a8", "c6")
    xi.make_move("g1", "e3")
    xi.make_move("g7", "g6")
    xi.make_move("e5", "e6")
    xi.make_move("g6", "g5")
    xi.make_move("e3", "g5")
    print(xi.current_player)"""

    """# gen / advisor testing

    xi.make_move("d1", "e2")
    xi.make_move("d10", "e9")
    xi.make_move("e1", "d1")
    xi.make_move("e10", "d10")
    xi.make_move("e2", "d3")
    xi.make_move("e9", "d8")
    xi.make_move("d1", "d2")
    xi.make_move("d10", "d9")
    xi.make_move("d3", "c4")"""

    # print(xi.current_player)
    # print(xi.black_gen_get())

    for i in xi.get_board():
        print(i)


if __name__ == "__main__":
    main()