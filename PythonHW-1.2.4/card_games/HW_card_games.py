class Card():
    """ A Card object maintains a `rank` and a `suit`. """

    _rank_to_str = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    _suit_to_str = {'C': 'Clubs', 'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}

    def __init__(self, rank: int, suit: str):
        """ Initialize a Card object.
        
        Parameters
        ----------
        rank : int in [2, 14]
            The rank of this card, with order 2, 3, 4, ..., 10, J, Q, K, A.
            
        suit : str in ('C', 'H', 'S', 'D')
            The suit of this card.
        """
        assert 2 <= rank <= 14, 'Valid ranks are [2, 14] for the ranks: [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]'
        assert suit.upper() in {'C', 'H', 'S', 'D'}, 'Valid suits are [C, H, S, D]'

        # student code goes here
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """ Return the string representation of this card.
        
        The card should be printed as "<rank> of <suit>s" where <rank> is the
        rank of this card and <suit> is the suit of this card. For example, the
        desired behavior is:
        
        >>> my_card = Card(4, 'D')
        >>> my_card
        4 of Diamonds
        
        >>> Card(13, 'H')
        King of Hearts
        
        >>> print(Card(11, 'C'))
        Jack of Clubs
        """
        # student code goes here
        _rank_to_str = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        _suit_to_str = {'C': 'Clubs', 'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}
        print(_rank_to_str)
        if self.rank < 11:
            return f'{self.rank} of {_suit_to_str[self.suit]}'
        return f'{_rank_to_str[self.rank]} of {_suit_to_str[self.suit]}'

    def __lt__(self, other):
        """ Determine whether the rank of this card is less than the rank of the other. """
        # student code goes here
        if self.rank < other.rank:
            return True
        return False

    def __gt__(self, other):
        """ Determine whether the rank of this card is greater than the rank of the other. """
        # student code goes here
        if self.rank > other.rank:
            return True
        return False

    def __le__(self, other):
        """ Determine whether the rank of this card is less than or equal to the rank of the other. """
        # student code goes here
        if self.rank <= other.rank:
            return True
        return False

    def __ge__(self, other):
        """ Determine whether the rank of this card is greater than or equal to the rank of the other. """
        # student code goes here
        if self.rank >= other.rank:
            return True
        return False

    def __eq__(self, other):
        """ Determine whether the rank of this card is equal to the rank of the other. """
        # student code goes here
        if self.rank == other.rank:
            return True
        return False

import random
class Deck():

    def __init__(self, shuffled=False):
        self.deckList = list()
        for suit in ["C", "H", "S", "D"]:
            for rank in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                self.deckList.append(Card(rank, suit))
        if shuffled:
            random.shuffle(self.deckList)
        self.dealtCards = 0
        self.shuffled = shuffled

    def shuffle(self):
        random.shuffle(self.deckList)
        self.shuffled = True

    def deal_card(self):
        if len(self.deckList) == 0: return None
        self.dealtCards += 1
        return(self.deckList.pop(0))

    def __repr__(self):
        return(f"Deck(dealt {self.dealtCards}, shuffled={self.shuffled})")

    def reset(self):
        self.shuffled = False
        self.dealtCards = 0
        self.deckList = []
        for suit in ["C", "H", "S", "D"]:
            for rank in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
                self.deckList.append(Card(rank, suit))