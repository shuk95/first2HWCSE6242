import http.client
import json
import csv


#############################################################################################################################
# cse6242 
# All instructions, code comments, etc. contained within this notebook are part of the assignment instructions.
# Portions of this file will auto-graded in Gradescope using different sets of parameters / data to ensure that values are not
# hard-coded.
#
# Instructions:  Implement all methods in this file that have a return
# value of 'NotImplemented'. See the documentation within each method for specific details, including
# the expected return value
#
# Helper Functions:
# You are permitted to write additional helper functions/methods or use additional instance variables within
# the `Graph` class or `TMDbAPIUtils` class so long as the originally included methods work as required.
#
# Use:
# The `Graph` class  is used to represent and store the data for the TMDb co-actor network graph.  This class must
# also provide some basic analytics, i.e., number of nodes, edges, and nodes with the highest degree.
#
# The `TMDbAPIUtils` class is used to retrieve Actor/Movie data using themoviedb.org API.  We have provided a few necessary methods
# to test your code w/ the API, e.g.: get_movie_cast(), get_movie_credits_for_person().  You may add additional
# methods and instance variables as desired (see Helper Functions).
#
# The data that you retrieve from the TMDb API is used to build your graph using the Graph class.  After you build your graph using the
# TMDb API data, use the Graph class write_edges_file & write_nodes_file methods to produce the separate nodes and edges
# .csv files for submission to Gradescope.
#
# While building the co-actor graph, you will be required to write code to expand the graph by iterating
# through a portion of the graph nodes and finding similar artists using the TMDb API. We will not grade this code directly
# but will grade the resulting graph data in your nodes and edges .csv files.
#
#############################################################################################################################


class Graph:

    # Do not modify
    def __init__(self, with_nodes_file=None, with_edges_file=None):
        """
        option 1:  init as an empty graph and add nodes
        option 2: init by specifying a path to nodes & edges files
        """
        self.nodes = []
        self.edges = []
        if with_nodes_file and with_edges_file:
            nodes_CSV = csv.reader(open(with_nodes_file))
            nodes_CSV = list(nodes_CSV)[1:]
            self.nodes = [(n[0], n[1]) for n in nodes_CSV]

            edges_CSV = csv.reader(open(with_edges_file))
            edges_CSV = list(edges_CSV)[1:]
            self.edges = [(e[0], e[1]) for e in edges_CSV]


    def add_node(self, id: str, name: str) -> None:
        """
        add a tuple (id, name) representing a node to self.nodes if it does not already exist
        The graph should not contain any duplicate nodes
        """
        return NotImplemented


    def add_edge(self, source: str, target: str) -> None:
        """
        Add an edge between two nodes if it does not already exist.
        An edge is represented by a tuple containing two strings: e.g.: ('source', 'target').
        Where 'source' is the id of the source node and 'target' is the id of the target node
        e.g., for two nodes with ids 'a' and 'b' respectively, add the tuple ('a', 'b') to self.edges
        """
        return NotImplemented


    def total_nodes(self) -> int:
        """
        Returns an integer value for the total number of nodes in the graph
        """
        return NotImplemented


    def total_edges(self) -> int:
        """
        Returns an integer value for the total number of edges in the graph
        """
        return NotImplemented


    def max_degree_nodes(self) -> dict:
        """
        Return the node(s) with the highest degree
        Return multiple nodes in the event of a tie
        Format is a dict where the key is the node_id and the value is an integer for the node degree
        e.g. {'a': 8}
        or {'a': 22, 'b': 22}
        """
        return NotImplemented


    def print_nodes(self):
        """
        No further implementation required
        May be used for de-bugging if necessary
        """
        print(self.nodes)


    def print_edges(self):
        """
        No further implementation required
        May be used for de-bugging if necessary
        """
        print(self.edges)


    # Do not modify
    def write_edges_file(self, path="edges.csv")->None:
        """
        write all edges out as .csv
        :param path: string
        :return: None
        """
        edges_path = path
        edges_file = open(edges_path, 'w', encoding='utf-8')

        edges_file.write("source" + "," + "target" + "\n")

        for e in self.edges:
            edges_file.write(e[0] + "," + e[1] + "\n")

        edges_file.close()
        print("finished writing edges to csv")


    # Do not modify
    def write_nodes_file(self, path="nodes.csv")->None:
        """
        write all nodes out as .csv
        :param path: string
        :return: None
        """
        nodes_path = path
        nodes_file = open(nodes_path, 'w', encoding='utf-8')

        nodes_file.write("id,name" + "\n")
        for n in self.nodes:
            nodes_file.write(n[0] + "," + n[1] + "\n")
        nodes_file.close()
        print("finished writing nodes to csv")



class  TMDBAPIUtils:

    # Do not modify
    def __init__(self, api_key:str):
        self.api_key=api_key


    def get_movie_cast(self, movie_id:str, limit:int=None, exclude_ids:list=None) -> list:
        """
        Get the movie cast for a given movie id, with optional parameters to exclude an cast member
        from being returned and/or to limit the number of returned cast members
        documentation url: https://developers.themoviedb.org/3/movies/get-movie-credits

        :param string movie_id: a movie_id
        :param list exclude_ids: a list of ints containing ids (not cast_ids) of cast members  that should be excluded from the returned result
            e.g., if exclude_ids are [353, 455] then exclude these from any result.
        :param integer limit: maximum number of returned cast members by their 'order' attribute
            e.g., limit=5 will attempt to return the 5 cast members having 'order' attribute values between 0-4
            If after excluding, there are fewer cast members than the specified limit, then return the remaining members (excluding the ones whose order values are outside the limit range). 
            If cast members with 'order' attribute in the specified limit range have been excluded, do not include more cast members to reach the limit.
            If after excluding, the limit is not specified, then return all remaining cast members."
            e.g., if limit=5 and the actor whose id corresponds to cast member with order=1 is to be excluded,
            return cast members with order values [0, 2, 3, 4], not [0, 2, 3, 4, 5]
        :rtype: list
            return a list of dicts, one dict per cast member with the following structure:
                [{'id': '97909' # the id of the cast member
                'character': 'John Doe' # the name of the character played
                'credit_id': '52fe4249c3a36847f8012927' # id of the credit, ...}, ... ]
                Note that this is an example of the structure of the list and some of the fields returned by the API.
                The result of the API call will include many more fields for each cast member.
        """
        return NotImplemented


    def get_movie_credits_for_person(self, person_id:str, vote_avg_threshold:float=None)->list:
        """
        Using the TMDb API, get the movie credits for a person serving in a cast role
        documentation url: https://developers.themoviedb.org/3/people/get-person-movie-credits

        :param string person_id: the id of a person
        :param vote_avg_threshold: optional parameter to return the movie credit if it is >=
            the specified threshold.
            e.g., if the vote_avg_threshold is 5.0, then only return credits with a vote_avg >= 5.0
        :rtype: list
            return a list of dicts, with each dict having 'id', 'title', and 'vote_avg' keys, 
            one dict per movie credit with the following structure:
                [{'id': '97909' # the id of the movie
                'title': 'Long, Stock and Two Smoking Barrels' # the title (not original title) of the credit
                'vote_avg': 5.0 # the float value of the vote average value for the credit}, ... ]
        """
        return NotImplemented


#############################################################################################################################
#
# BUILDING YOUR GRAPH
#
# Working with the API:  See use of http.request: https://docs.python.org/3/library/http.client.html#examples
#
# Using TMDb's API, build a co-actor network for the actor's/actress' highest rated movies
# In this graph, each node represents an actor
# An edge between any two nodes indicates that the two actors/actresses acted in a movie together
# i.e., they share a movie credit.
# e.g., An edge between Samuel L. Jackson and Robert Downey Jr. indicates that they have acted in one
# or more movies together.
#
class Graph:
    def __init__(self, with_nodes_file=None, with_edges_file=None):
        self.nodes = []  # List of (id, name) tuples
        self.edges = []  # List of (source, target) tuples

        if with_nodes_file and with_edges_file:
            with open(with_nodes_file, 'r', encoding='utf-8') as nodes_file:
                reader = csv.reader(nodes_file)
                next(reader)  # Skip header
                self.nodes = [(row[0], row[1]) for row in reader]

            with open(with_edges_file, 'r', encoding='utf-8') as edges_file:
                reader = csv.reader(edges_file)
                next(reader)  # Skip header
                self.edges = [(row[0], row[1]) for row in reader]

    def add_node(self, id: str, name: str) -> None:
        """Add node if it doesn't exist"""
        clean_name = name.replace(",", "")  # Remove commas to avoid CSV issues
        if not any(node[0] == str(id) for node in self.nodes):
            self.nodes.append((str(id), clean_name))

    def add_edge(self, source: str, target: str) -> None:
        """Add undirected edge if it doesn't exist"""
        if source > target:
            source, target = target, source
        if not any(edge == (source, target) for edge in self.edges):
            self.edges.append((source, target))

    def total_nodes(self) -> int:
        return len(self.nodes)

    def total_edges(self) -> int:
        return len(self.edges)

    def max_degree_nodes(self) -> dict:
        """Find nodes with highest degree"""
        degrees = {node_id: 0 for node_id, _ in self.nodes}
        for source, target in self.edges:
            degrees[source] += 1
            degrees[target] += 1

        max_degree = max(degrees.values(), default=0)
        return {node_id: deg for node_id, deg in degrees.items() if deg == max_degree}

    def write_edges_file(self, path="edges.csv") -> None:
        """Write edges to CSV file"""
        with open(path, 'w', encoding='utf-8', newline='') as edges_file:
            writer = csv.writer(edges_file)
            writer.writerow(["source", "target"])
            writer.writerows(self.edges)

    def write_nodes_file(self, path="nodes.csv") -> None:
        """Write nodes to CSV file"""
        with open(path, 'w', encoding='utf-8', newline='') as nodes_file:
            writer = csv.writer(nodes_file)
            writer.writerow(["id", "name"])
            writer.writerows(self.nodes)


class TMDBAPIUtils:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_movie_cast(self, movie_id: str, limit: int = None, exclude_ids: list = None) -> list:
        """Get the movie cast with filtering and limiting"""
        try:
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            conn.request(
                "GET",
                f"/3/movie/{movie_id}/credits?api_key={self.api_key}&language=en-US"
            )

            response = conn.getresponse()
            data = json.loads(response.read().decode())

            if 'cast' not in data:
                return []

            exclude_set = set(str(id) for id in (exclude_ids or []))
            sorted_cast = sorted(data['cast'], key=lambda x: x.get('order', float('inf')))
            
            filtered_cast = []
            for cast_member in sorted_cast:
                member_id = str(cast_member.get('id', ''))
                if not member_id or member_id in exclude_set:
                    continue  # Skip excluded actors

                filtered_cast.append({
                    'id': member_id,
                    'character': cast_member.get('character', ''),
                    'credit_id': cast_member.get('credit_id', ''),
                    'name': cast_member.get('name', '')
                })

                if limit is not None and len(filtered_cast) >= limit:
                    break  # Stop if limit reached

            return filtered_cast

        except Exception as e:
            print(f"Error getting cast for movie {movie_id}: {e}")
            return []
        finally:
            if 'conn' in locals():
                conn.close()

    def get_movie_credits_for_person(self, person_id: str, vote_avg_threshold: float = None) -> list:
        """Get movie credits for a person with filtering"""
        try:
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            conn.request(
                "GET",
                f"/3/person/{person_id}/movie_credits?api_key={self.api_key}&language=en-US"
            )

            response = conn.getresponse()
            data = json.loads(response.read().decode())

            if 'cast' not in data:
                return []

            credits = []
            for movie in data['cast']:
                if not movie.get('id'):
                    continue

                vote_avg = float(movie.get('vote_average', 0))
                if vote_avg_threshold is None or vote_avg >= vote_avg_threshold:
                    credits.append({'id': str(movie['id']), 'title': movie.get('title', ''), 'vote_avg': vote_avg})

            return credits

        except Exception as e:
            print(f"Error getting credits for person {person_id}: {e}")
            return []
        finally:
            if 'conn' in locals():
                conn.close()


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(id='2975', name='Laurence Fishburne')

    tmdb_api_utils = TMDBAPIUtils(api_key='<your API key>')

    base_movies = tmdb_api_utils.get_movie_credits_for_person('2975', vote_avg_threshold=8.0)
    processed_nodes = {'2975'}
    current_level_nodes = set()

    for movie in base_movies:
        cast = tmdb_api_utils.get_movie_cast(movie['id'], limit=3)
        for actor in cast:
            if actor['id'] != '2975':
                graph.add_node(actor['id'], actor['name'])
                graph.add_edge('2975', actor['id'])
                current_level_nodes.add(actor['id'])
                processed_nodes.add(actor['id'])

    for _ in range(2):
        next_level_nodes = set()
        for actor_id in current_level_nodes:
            movies = tmdb_api_utils.get_movie_credits_for_person(actor_id, vote_avg_threshold=8.0)
            for movie in movies:
                exclude_ids = list(processed_nodes)
                cast = tmdb_api_utils.get_movie_cast(movie['id'], limit=3, exclude_ids=exclude_ids)

                for co_actor in cast:
                    if co_actor['id'] not in processed_nodes:
                        graph.add_node(co_actor['id'], co_actor['name'])
                        graph.add_edge(actor_id, co_actor['id'])
                        next_level_nodes.add(co_actor['id'])
                        processed_nodes.add(co_actor['id'])

        current_level_nodes = next_level_nodes


# ----------------------------------------------------------------------------------------------------------------------

# Exception handling and best practices
# - You should use the param 'language=en-US' in all API calls to avoid encoding issues when writing data to file.
# - If the actor name has a comma char ',' it should be removed to prevent extra columns from being inserted into the .csv file
# - Some movie_credits do not return cast data. Handle this situation by skipping these instances.
# - While The TMDb API does not have a rate-limiting scheme in place, consider that making hundreds / thousands of calls
#   can occasionally result in timeout errors. If you continue to experience 'ConnectionRefusedError : [Errno 61] Connection refused',
#   - wait a while and then try again.  It may be necessary to insert periodic sleeps when you are building your graph.


def return_name()->str:
    """
    Return a string containing your GT Username
    e.g., gburdell3
    Do not return your 9 digit GTId
    """
    return NotImplemented


# You should modify __main__ as you see fit to build/test your graph using  the TMDBAPIUtils & Graph classes.
# Some boilerplate/sample code is provided for demonstration. We will not call __main__ during grading.

if __name__ == "__main__":

    graph = Graph()
    graph.add_node(id='2975', name='Laurence Fishburne')
    tmdb_api_utils = TMDBAPIUtils(api_key='<your API key>')

    # call functions or place code here to build graph (graph building code not graded)
    # Suggestion: code should contain steps outlined above in BUILD CO-ACTOR NETWORK

    graph.write_edges_file()
    graph.write_nodes_file()

    # If you have already built & written out your graph, you could read in your nodes & edges files
    # to perform testing on your graph.
    # graph = Graph(with_edges_file="edges.csv", with_nodes_file="nodes.csv")
