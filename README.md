# MPP Detector (2021)
The purpose of this API is to detect via Machine Learning algorithms some key features about a user.
Disclaimer: this project is for educational purposes only within the company Mon Petit Placement and is not used in production.

## HOWTO BUILD
`docker build -t mpp-detector .`

## HOWTO RUN
`docker run -t 5000:80 mpp-detector:latest`

## HOWTO TEST

```
    POST on /is_signer

    Input : 
    {
        "kycData": {
            "mpp-long-term-risk": "mpp-long-term-risk-true",
            "mpp-high-risks-high-return": "mpp-high-risks-high-return-true",
            "mpp-has-already-invested": "mpp-has-already-invested-yes",
            "mpp-unique-investment": "mpp-unique-investment-yes",
            "mpp-summary-experience": "1",
            "mpp-reaction-loss": "mpp-reaction-loss-sell-part",
            "mpp-reaction-gain": "mpp-reaction-gain-wait",
            "mpp-preference-evolution": "mpp-preference-evolution-150-0",
            "mpp-preference-tendancy": "mpp-preference-tendancy-big",
            "mpp-summary-risk": 0,
            "monthly-amount": 100,
            "total": 100,
            "monthly-income": 100,
            "no-loans": 0,
            "mpp-summary-capacity": 1,
            "gender": "man",
            "age": 50,
            "initial-amount": 1000,
            "duration": 10,
            "no-children": 0,
            "marital-status": "family-situation-married",
            "investment-goals": [
                "mpp-investment-goals-safe-savings",
                "mpp-investment-goals-refund-guarantee",
                "mpp-investment-goals-patrimony-transmission"
            ]
        },
        "threshold": 0.3
    }

    Ouput :
        {
            "probability": 0.23,
            "label": "Peu de chance de signer"
        }, 
        200
```

