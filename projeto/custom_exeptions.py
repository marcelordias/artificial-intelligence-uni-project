# Description: Custom exceptions for the project
class CityNotFound(Exception): # Exception for when a city is not found
    pass
class PathNotFound(Exception): # Exception for when a path is not found
    pass
class OriginAndDestinyAreTheSame(Exception): # Exception for when the origin and destiny are the same
    pass