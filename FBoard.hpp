/*******************************************************************************
** Name:         John-Francis Caccamo
** Date:         6 / 6 / 19
** Description:  This is the FBoard.hpp class specification file, containing the
**               FBoard class member variable and function declarations
**               AKA - the FBoard header or interface file
*******************************************************************************/

#ifndef FBOARD_HPP //if FBoard.hpp file not defined 
#define FBOARD_HPP //define FBoard.hpp 

enum gameStatus {X_WON, O_WON, UNFINISHED}; //enumerate gameState declaration with 3 values as enums

class FBoard
{
private: //private data types
	char boardArray[8][8]; //2-D board array declaration -8 rows by 8 cols
	gameStatus gameState; //private gameState member var of gameStatus enum type
	int xPiece[2]; //tracking x in an array with two elements - x and y coordinates
	bool oWinner(); //declare private helper function to determine if o wins
public: //public class functions
	FBoard(); //default constructor
	gameStatus getGameState(); //enum getter
	bool moveX(int, int); //movex 
	bool moveO(int, int, int, int); //movey
	void printBoard(); //prints board
};
#endif //end FBoard definition