et us begin with an example:

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.

He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

Can you help him?

How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?


def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    # your code
    months = 0
    savings = 0

    while start_price_old + savings < start_price_new:
        months += 1
        if months % 2 == 0:
            percent_loss_by_month += 0.5  # increase loss every two months
        start_price_old *= (1 - percent_loss_by_month / 100)
        start_price_new *= (1 - percent_loss_by_month / 100)
        savings += saving_per_month

        print(1 - percent_loss_by_month / 100)
    return [months, round(start_price_old + savings - start_price_new)]
