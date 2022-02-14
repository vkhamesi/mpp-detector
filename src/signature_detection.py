import pickle
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from utils import *
from src.mapper import *
import numpy as np

def build_kyc_data(data: dict) -> dict:
    """
    -> Input: 
    ---
    -> Output: 
    • kyc data with good format
    """
    kyc_data = {
        "exp_fin_q1": clean_exp_fin_q1(data),
        "exp_fin_q2": clean_exp_fin_q2(data),
        "has_already_invested": clean_has_already_invested(data),
        "unique_investment": clean_unique_investment(data),
        "summary_experience": clean_summary_experience(data),
        "reaction_loss": clean_reaction_loss(data),
        "reaction_gain": clean_reaction_gain(data),
        "preference_evolution": clean_preference_evolution(data),
        "preference_tendancy": clean_preference_tendancy(data),
        "summary_risk": clean_summary_risk(data),
        "monthly_amount": clean_monthly_amount(data),
        "total": clean_total(data),
        "monthly_income": clean_monthly_income(data),
        "no_loans": clean_no_loans(data),
        "summary_capacity": clean_summary_capacity(data),
        "gender": clean_gender(data),
        "age": clean_age(data),
        "initial_amount": clean_initial_amount(data),
        "duration": clean_duration(data),
        "no_children": clean_no_children(data),
        "in_relationship": guess_in_relationship(data),
        "single": guess_single(data),
        "investment_goals_low_risk": guess_investment_goals_low_risk(data),
        "investment_goals_high_risk": guess_investment_goals_high_risk(data),
        "investment_goals_thematic": guess_investment_goals_thematic(data)
    }

    return kyc_data

def get_probability(kyc_data: dict) -> float:
    """
    -> Input: kyc data following format
    • kyc_data = {
        "exp_fin_q1": [-1, 0, 1],
        "exp_fin_q2": [-1, 0, 1],
        "has_already_invested": [-1, 1],
        "unique_investment": [0, 1],
        "summary_experience": [0, 1, 2, 3],
        "reaction_loss": [-2, -1, 0, 1, 2],
        "reaction_gain": [-2, -1, 0, 1, 2],
        "preference_evolution": [-1, 0, 1],
        "preference_tendancy": [0, 1, 2, 3],
        "summary_risk": [0, 1, 2, 3],
        "monthly_amount": [0:+],
        "total": [0:+],
        "monthly_income": [0:+],
        "no_loans": [0:+],
        "summary_capacity": [0, 1, 2, 3],
        "gender": [0, 1],
        "age": [0:+],
        "initial_amount": [0:+],
        "duration": [0:+],
        "no_children": [0:+],
        "in_relationship": [0, 1],
        "single": [0, 1],
        "investment_goals_low_risk": [0:+],
        "investment_goals_high_risk": [0:+],
        "investment_goals_thematic": [0:+]
    }
    ---
    -> Output: 
    • probability of signature
    """

    filename = MODELS_DIRPATH + "signature_detection_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))

    array = np.array(list(kyc_data.values()))
    probability = float(loaded_model.predict(array.reshape(1, -1)))

    return probability

def get_threshold(data: dict) -> float:
    threshold = 0.3

    if 'threshold' in data.keys():
        threshold = data['threshold']
    
    return threshold

def get_prediction(probability: float, threshold=0.3) -> str:
    """
    -> Input:
    • probability of signature
    • threshold : high -> a lot of predictions but low accuracy 
                  low -> few predictions but high accuracy
    ---
    -> Output:
    • label
    """

    if np.abs(probability) < threshold:
        return 0
    elif np.abs(1 - probability) < threshold:
        return 1
    else:
        return None

def guess_label(decision: int) -> str:
    """
    -> Input:
    • decision
    ---
    -> Output:
    • label
    """

    if 0 == decision:
        content = "Peu de chance de signer"
    elif 1 == decision:
        content = "Grandes chances de signer"
    elif None == decision:
        content = "Ne peut pas prédire"
    else:
        raise ValueError('Wrong value for decision')
    return content

def guess_result(data: dict) -> dict:
    """
    -> Input:
    • data dictionary
    ---
    -> Output:
    • decision dictionary with probability and label
    """

    probability = get_probability(build_kyc_data(data['kycData']))
    decision = get_prediction(probability, get_threshold(data))    
    
    return {
        "probability": probability,
        "label": guess_label(decision)
    }