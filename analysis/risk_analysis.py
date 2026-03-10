def risk_analysis(df):

    risk_students = df[
        (df['Math'] < 40) |
        (df['Science'] < 40) |
        (df['English'] < 40)
    ]

    print("Number of At Risk Students:", len(risk_students))

    return risk_students