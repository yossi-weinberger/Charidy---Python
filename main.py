import income
import donation
from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route("/tithe")
def index():
    return render_template("index.html")


def new_income_line():
    new_income = income.Income()
    assert new_income.amunt >= 0, "Amunt can't be negative"
    new_income.save_total_tithe()
    new_income.save_income()
    print(new_income)


def new_donation_line():
    new_donation = donation.Donation()
    new_donation.save_total_tithe()
    new_donation.save_donation()
    print(new_donation)


# new_donation_line()
new_income_line()
