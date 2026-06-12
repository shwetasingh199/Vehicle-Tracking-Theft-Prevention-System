def get_live_alerts(df):

    alerts = df[
        df["Alert"] != "SAFE"
    ]

    return alerts.tail(10)