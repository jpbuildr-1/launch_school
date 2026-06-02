lass Candidate:

    def __init__(self, name):
        self._name = name
        self._votes = 0

    # __add__ method not needed

    def __iadd__(self, augment):
        if not isinstance(augment, int):
            return NotImplemented

        self._votes += augment
        return self

    @property
    def name(self):
        return self._name

    @property
    def votes(self):
        return self._votes


class Election():

    def __init__(self, candidates):
        self._candidates = candidates
    
    def results(self):
        max_votes = 0
        winner = None
        total_votes = 0
        
        for candidate in self._candidates:
            print(f'{candidate.name}: {candidate.votes} votes')
            total_votes += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name
        
        print()
        
        if total_votes > 0:
            percent = max_votes / total_votes
            print(f'{winner} won: {percent:.1%} of votes')
            

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()
