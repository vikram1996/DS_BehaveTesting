Feature: The functionality of DiseaseScope : Getting Disease Genes and Tissues

  Scenario Outline: Validity of a doid
    Given a doid <doid>
    When we look the doid up with diseaseScope
    Then it yields <validity>

    Examples: Doids
    | doid          | validity  |
    | 0040003       | Valid     |
    | 2841          | Valid     |
    | 0050654       | Valid     |
    | 00000         | Invalid   |
    | 10101         | Invalid   |


  Scenario Outline: Get disease name from doid
    Given a valid doid <valid_doid>
    When we run diseaseScope to get the disease from doid
    Then  <disease> is correct

    Examples: Doids
    | valid_doid    | disease                   |
    | 0040003       | benzylpenicillin allergy  |
    | 2841          | asthma                    |
    | 2841          | long QT syndrome          |
    | 0050654       | Baller-Gerold syndrome    |


  Scenario Outline: Get set of genes associated with a disease
    Given a disease for gene association: <disease>
    When we run diseaseScope to get the associated genes of the disease
    Then <genes> are contained by the associated genes determined

    Examples: disease

    | disease           | genes               |
    | angiosarcoma      | PLCG1               |
    | pterygium         | PHGDH,IFNA2,FKBP10  |
    | pterygium         | IFNA2,FKBP10        |
    | pterygium         | PLCG1               |


  Scenario Outline: Get set of tissues associated with a disease
    Given a disease for tissue association: <disease>
    When we run diseaseScope to get the associated tissues of the disease
    Then <tissues> are contained by the associated tissues determined

    Examples: disease

    | disease           | tissues                   |
    | angiosarcoma      | renal_clear_cell          |
    | shrimp allergy    | basophil,skin,mouth       |
    | shrimp allergy    | basophil,renal_clear_cell |
    | angiosarcoma      | some_tissue               |


  Scenario: Get set of tissues associated with a disease from a file
    Given a file: disease_tissue_test.txt
    When we compare tissues in the file with those produced by diseasescope
    Then the two listings match exactly

  Scenario: Get set of diseases associated with a doid from a file
    Given a file: doid_disease_test.txt
    When we compare disease in the file with those produced by diseasescope
    Then all entries are correct

