Feature: The functionality of DiseaseScope : Get Network and Expand

  Scenario Outline: Build PCNet network from doid
    Given a doid <doid>
    When we pull a PCNet
    Then we get a valid <network_type>  with <nodes> and <edges>

    Examples: Doids

    | doid          | network_type                                        |     nodes     |   edges        |
    | 2841          |   Parsimonious Composite Network (PCNet)            |     19781     |    2724724     |


  Scenario: expand geneset
    Given a doid 2841 and its generated PCNetwork
    When we expand gene set with alpha=0.56 , n=250 and add subnetwork = True
    Then The expnansion is valid

  Scenario: infer hierarchical model
    Given a doid 2841 and its generated PCNetwork
    When we infer hierarchical model with method=clixo-api , edge_attr=weight and method args
    |argument | value|
    |alpha  | 0.01 |
    |beta   | 0.5  |
    Then the generated hierarchical model is valid
