using System;

namespace SnakeAndLadder
{
    class Program
    {
        static void Main(string[] args)
        {
            var x = new Position();
            var y = new Position();
            System.Console.WriteLine(x.Equals(y));
        }
    }

    public class Board{

    }

    public class Cell{

    }

    public class Player{

        public bool Wins{get;set;} = false;
        public Position CPosition{get;set;} = new Position(0,0,0);

    }

    public class Mover{
        public MoverTypes MoverType{get;set;}
        public Position From{get;set;}
        public Position To{get;set;}

        public void MovePlayer(Player player){
            if player.CPosition
        }

    }
    public enum MoverTypes
    {
        Snack,
        Ladder
        
    }

    public struct Position{
        public int X{get;set;} 
        public int Y{get;set;} 
        public int Index{get;set;}

        public Position(int x=0,int y=1, int index = 0){
            X = x;
            Y = y;
            Index = index;
        }
    }
}
