module Types.Page exposing (Page(..), PageState(..))

import Types.GameState exposing (GameState)


type Page
    = Home
    | Recipes
    | Photos
    | Debug


type PageState
    = Loading
    | Failure String
    | Success GameState String
