/************************************************************************************
** Name:        John-Francis Caccamo
** Date:        6 / 6 / 19
** Description: This is the FBoard.cpp class implementation file, containing 
**              the FBoard function definitions. It contains a 1) default constructor
**              initializing the pieces of the board and empty space 2) a gameState
**              getter 3) a bool to move x and 4) a bool to move o. Included is a 
**              5th helper function that determines if o wins. 
*************************************************************************************/

#include <iostream>

#include <cmath> //include cmath for abs value function

#include "FBoard.hpp" //include FBoard.hpp file

/**********************************************************************************
**              FBoard::FBoard()
**
** Description:
** This is the FBoard default constructor, using two for loops to initialize the
** board. It also intializes x's location and assigns this coordinate as an
** initialization value to xPiece. It also initiazes 4 o pieces and gameState
** to UNFINISHED.
***********************************************************************************/

FBoard::FBoard()
{
	for (int row = 0; row < 8; row++) //nested for loops to create 2D board array
		for (int col = 0; col < 8; col++)
			boardArray[row][col] = 'T'; //initialzing board elements to empty space T

	boardArray[0][3] = 'x'; //x piece at starting position (0,3)

	xPiece[0] = 0; //xPiece data member's 1st array element stores x's x-coord, 0
	xPiece[1] = 3; //xPiece data member's 2nd array element stores x's y-coord, 3

	boardArray[7][0] = 'o'; //1st o at position (7,0)

	boardArray[7][2] = 'o'; //2nd o at position (7,2)

	boardArray[7][4] = 'o'; //3rd o at position (7,4)

	boardArray[7][6] = 'o'; //4th o at position (7,6)

	gameState = UNFINISHED; //initialize gameState to UNFINISHED
}

/******************************************************************
**               gameStatus FBoard::getGameState()
**
** Description:
** This is the getter/accessor of the enumerate value of gameState
** It will return gameState- the status of the game.
*******************************************************************/

gameStatus FBoard::getGameState()
{
	return gameState;
}

/******************************************************************
**              bool FBoard::moveX(int xMoveRow, int xMoveColumn)
**
** Description: 
** This is the moveX function, with a series of if statements 
** determining legal moves of the x piece. If the move is legal, 
** x will replace the empty character at that position and its old 
** location will be replaced with empty space. The xPiece private 
** member variable's elements will be updated accordingly to where 
** x goes.
*******************************************************************/

bool FBoard::moveX(int xMoveRow, int xMoveColumn) //two parameters representing row & column to move to
{
	if (gameState != UNFINISHED) // if game not unfinished
		return false;

	if (xMoveRow < 0 || xMoveRow > 7 || xMoveColumn < 0 || xMoveColumn > 7) //if move is not in board bounds 
		return false;

	if (boardArray[xMoveRow][xMoveColumn] != 'T') //If location to move to is not empty 
		return false;

	//abs function to check for a legal move one diagonal in any direction from current xPiece position 
	if ((std::abs(xPiece[0] - xMoveRow) == 1) && (std::abs(xPiece[1] - xMoveColumn) == 1)) 
	{
		boardArray[xPiece[0]][xPiece[1]] = 'T'; //replace orig x position
		boardArray[xMoveRow][xMoveColumn] = 'x'; //update new x position

		xPiece[0] = xMoveRow; //update the x coordinate of member variable xPiece
		xPiece[1] = xMoveColumn; //update the y coordinate of member variable xPiece

		if (xMoveRow == 7) //if x has reached row 7 of array
			gameState = X_WON; //x wins, enum gameState switched to X_WON

		return true;
	}
	else
		return false;
}

/********************************************************************************
**  bool FBoard::moveO(int oFromRow, int oFromCol, int oToRow, int oToCol)
**
** Description:
** This is the moveO function, with a series of if statements
** determining legal moves of the o pieces. If the move is legal,
** o will replace the empty character at that position and its old location will 
** be replaced with empty space.
********************************************************************************/

bool FBoard::moveO(int oFromRow, int oFromCol, int oToRow, int oToCol) //4 params-current o (x,y) to new o (x,y)
{
	if (gameState != UNFINISHED) //if game not unfinished
		return false;

	if (oFromRow < 0 || oFromRow > 7 || oFromCol < 0 || oFromCol > 7) //if current (x,y) is not in bounds
		return false;

	if (oToRow < 0 || oToRow > 7 || oToCol < 0 || oToCol > 7) //if new (x,y) is not in bounds
		return false;

	if (boardArray[oFromRow][oFromCol] != 'o') //if current (x,y) not an o piece
		return false; 

	if (boardArray[oToRow][oToCol] != 'T') //if new (x,y) doesn't hold an empty space
		return false;

	//if the o move is legal - can only go UP the board diagonally 
	if ((oToRow == oFromRow - 1) && (oToCol == oFromCol - 1 || oToCol == oFromCol + 1))
	{
		boardArray[oFromRow][oFromCol] = 'T'; //replace old o (x,y) with empty space
		boardArray[oToRow][oToCol] = 'o'; //update the new o position
		
		if (oWinner()) //helper function call to determine if x still has legal moves
			gameState = O_WON; //if true, change gameState to O_WON

		return true;
	}
	else
		return false;
}

/**********************************************************************
**              bool FBoard::oWinner()
**
** Description:
** This is the definition of the private helper function oWinner.
** The purpose of this function is to determine if the x piece 
** still has legal moves available. If x has no available legal moves 
** - IE blocked by the end of the board and o pieces - 
** this function will return true.
************************************************************************/

bool FBoard::oWinner()
{
	int xRow = xPiece[0]; //obtain x piece x-coord from xPiece array
	int xCol = xPiece[1]; //obtain x piece y-coord from xPiece array

	//if x piece can move down or right with a legal space to move to
	if (xRow + 1 >= 0 && xRow + 1 <= 7)
		if (xCol + 1 >= 0 && xCol + 1 <= 7)
			if (boardArray[xRow + 1][xCol + 1] == 'T')
				return false;

	//if x piece can move down or left with a legal space to move to
	if (xRow + 1 >= 0 && xRow + 1 <= 7)
		if (xCol - 1 >= 0 && xCol - 1 <= 7)
			if (boardArray[xRow + 1][xCol - 1] == 'T')
				return false;

	//if x piece can move up or right with a legal space to move to
	if (xRow - 1 >= 0 && xRow - 1 <= 7)
		if (xCol + 1 >= 0 && xCol + 1 <= 7)
			if (boardArray[xRow - 1][xCol + 1] == 'T')
				return false;

	//if x piece can move up or left with a legal space to move to
	if (xRow - 1 >= 0 && xRow - 1 <= 7)
		if (xCol - 1 >= 0 && xCol - 1 <= 7)
			if (boardArray[xRow - 1][xCol - 1] == 'T')
				return false;

	return true; //if x piece has no legal moves it can make
}


void FBoard::printBoard()
{
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
			std::cout << boardArray[i][j] << " ";
		std::cout << std::endl;
	}
	std::cout << std::endl;
	std::cout << std::endl;
	std::cout << std::endl;
}
