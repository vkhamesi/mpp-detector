
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from exceptions import *

def verify_key(data, key):
    if key not in list(data.keys()):
        raise BadEntryError(str(key) + ' key does not exist')
    pass

def verify_values(data, key, values):
    verify_key(data, key)
    
    value = str(data[key])

    if value not in list(values):
        raise BadEntryError(str(value) + ' value does not exist')
    
    pass

def clean_exp_fin_q1(data):
    key = 'mpp-long-term-risk'
    values = {
        'mpp-long-term-risk-true':1,
        'mpp-long-term-risk-do-not-know':0,
        'mpp-long-term-risk-false':-1
    }

    verify_values(
        data, 
        key,
        values.keys()

    )

    return float(values[str(data[str(key)])])

def clean_exp_fin_q2(data):
    key = 'mpp-high-risks-high-return'
    values = {
        'mpp-high-risks-high-return-true':1,
        'mpp-high-risks-high-return-do-not-:know':0,
        'mpp-high-risks-high-return-false':-1
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_has_already_invested(data):
    key = 'mpp-has-already-invested'
    values = {
        'mpp-has-already-invested-yes':1,
        'mpp-has-already-invested-no':-1
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_unique_investment(data):
    key = 'mpp-unique-investment'
    values = {
        'mpp-unique-investment-yes':0,
        'mpp-unique-investment-no':1
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_summary_experience(data):
    key = 'mpp-summary-experience'
    values = {
        '0':0,
        '1':1,
        '2':2,
        '3':3
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_reaction_loss(data):
    key = 'mpp-reaction-loss'
    values = {
        'mpp-reaction-loss-sell-everything':-2,
        'mpp-reaction-loss-sell-part':-1,
        'mpp-reaction-loss-reinvest':2,
        'mpp-reaction-loss-wait':1,
        'mpp-reaction-loss-need-advice':0
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_reaction_gain(data):
    key = 'mpp-reaction-gain'
    values = {
        'mpp-reaction-gain-sell-everything':-2,
        'mpp-reaction-gain-sell-gain':-1,
        'mpp-reaction-gain-invest':2,
        'mpp-reaction-gain-wait':1,
        'mpp-reaction-gain-need-advice':0
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_preference_evolution(data):
    key = 'mpp-preference-evolution'
    values = {
        'mpp-preference-evolution-2500-1500':1,
        'mpp-preference-evolution-1200-500':0,
        'mpp-preference-evolution-150-0':-1
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_preference_tendancy(data):
    key = 'mpp-preference-tendancy'
    values = {
        'mpp-preference-tendancy-big':3,
        'mpp-preference-tendancy-middle':2,
        'mpp-preference-tendancy-small':1,
        'mpp-preference-tendancy-none':0
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_summary_risk(data):
    key = 'mpp-summary-risk'
    values = {
        '0':0,
        '1':1,
        '2':2,
        '3':3
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_monthly_amount(data):
    key = 'monthly-amount'
    verify_key(data, key)
    return data[key]

def clean_total(data):
    key = 'total'
    verify_key(data, key)
    return data[key]

def clean_monthly_income(data):
    key = 'monthly-income'
    verify_key(data, key)
    return data[key]

def clean_no_loans(data):
    key = 'no-loans'
    verify_key(data, key)
    return data[key]

def clean_summary_capacity(data):
    key = 'mpp-summary-capacity'
    values = {
        '0':0,
        '1':1,
        '2':2,
        '3':3
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_gender(data):
    key = 'gender'
    values = {
        'man':1,
        'woman':0
    }
    verify_values(
        data, 
        key,
        values.keys()
    )

    return float(values[str(data[str(key)])])

def clean_age(data):
    key = 'age'
    verify_key(data, key)
    return data[key]

def clean_initial_amount(data):
    key = 'initial-amount'
    verify_key(data, key)
    return data[key]

def clean_duration(data):
    key = 'duration'
    verify_key(data, key)
    return data[key]

def clean_no_children(data):
    key = 'no-children'
    verify_key(data, key)
    return data[key]

def guess_in_relationship(data):
    key = 'marital-status'
    verify_key(data, key)

    return int(data[key] in [
        'family-situation-cohabitant', 
        'family-situation-free-union', 
        'family-situation-married', 
        'family-situation-pacse'
        ])

def guess_single(data):
    key = 'marital-status'
    verify_key(data, key)
    
    return int(data[key] in [
        'family-situation-divorced', 
        'family-situation-single', 
        'family-situation-widow'
        ])

def guess_investment_goals_low_risk(data):
    key = 'investment-goals'
    verify_key(data, key)

    nb = 0

    for goal in [
        'mpp-investment-goals-safe-savings',
        'mpp-investment-goals-refund-guarantee',
        'mpp-investment-goals-patrimony-transmission',
        'mpp-investment-goals-retirement',
        'mpp-investment-goals-children-studies'
    ]:
        if goal in data[key]:
            nb += 1

    return nb

def guess_investment_goals_high_risk(data):
    key = 'investment-goals'
    verify_key(data, key)
    
    nb = 0

    for goal in [
        'mpp-investment-goals-energize-capital',
        'mpp-investment-goals-important-project',
        'mpp-investment-goals-regular-income'
    ]:
        if goal in data[key]:
            nb += 1
            
    return nb

def guess_investment_goals_thematic(data):
    key = 'investment-goals'
    verify_key(data, key)
    
    nb = 0

    for goal in [
        'mpp-investment-goals-thematic-climate',
        'mpp-investment-goals-thematic-equality',
        'mpp-investment-goals-thematic-health',
        'mpp-investment-goals-thematic-job',
        'mpp-investment-goals-thematic-relaunch',
        'mpp-investment-goals-thematic-solidarity',
        'mpp-investment-goals-thematic-tech'
    ]:
        if goal in data[key]:
            nb += 1
            
    return nb