# EXERCISE 1

rented_movies = [{
    'movie' : 'The Little Mermaid',
    'days' : 3
},
{
    'movie' : 'Brother Bear',
    'days' : 5   
},
{
    'movie' : 'Hercules',
    'days' : 1
}]
def how_much_to_pay(movie_name):
    price_per_day = 3
    for n in rented_movies:
        if n['movie'] == movie_name:
            total_price = n['days'] * price_per_day
    return print('For', movie_name, 'the total price was', total_price)

# example 1
how_much_to_pay('The Little Mermaid')
how_much_to_pay('Brother Bear')
how_much_to_pay('Hercules')

# EXERCISE 2


def payment_for_this_week(g, a, f):
    google = 400 * g
    amazon = 380 * a
    facebook = 350 * f
    total_pay = google + amazon + facebook
    return total_pay
# example
payment_for_this_week(6, 4, 10)

# EXERCISE 3

student_enrolled == True if class_full == False and schedule_conflict == False

# EXERCISE 4

if shopper == premium_member or (items >= 2 and date > current_date):
    purchase = purchase - (purchase * product_offer)

