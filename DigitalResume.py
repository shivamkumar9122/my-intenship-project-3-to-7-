  <script>
    // small script: fill demo name from localStorage if available
    (function(){
      const nameEl = document.getElementById('name');
      const stored = localStorage.getItem('resume_name');
      if(stored) nameEl.textContent = stored;
    })();
  </script>
</body>
</html>

    """
    
@app.route("/about")  
def about():
    return """
    <h1>i am aboutpage</h1>
    <h2>I am running in Flask</h2>
    """
if __name__=='__main__':  
    app.run()
