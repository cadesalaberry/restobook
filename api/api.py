from flask import redirect
from eve import Eve
app = Eve()

@app.route('/search')
def function():
  
  # If set, then we are booking
  print 'Should return all restaurants for now'
  return redirect('/restaurants')

if __name__ == '__main__':
    app.run(debug=True)
