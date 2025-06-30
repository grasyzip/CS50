@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validações
        if not username:
            return apology("must provide username", 400)
        if not password or not confirmation:
            return apology("must provide password", 400)
        if password != confirmation:
            return apology("passwords don't match", 400)

        # Hash da senha
        hash = generate_password_hash(password)

        # Inserir usuário no banco
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except ValueError:
            return apology("username already exists", 400)

        # Login automático
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Validações
        if not symbol:
            return apology("must provide symbol", 400)
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide positive integer", 400)

        shares = int(shares)
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        # Verificar saldo
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]
        total_cost = stock["price"] * shares

        if cash < total_cost:
            return apology("can't afford", 400)

        # Atualizar banco de dados
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                  session["user_id"], symbol, shares, stock["price"])

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Obter informações do usuário
    user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]

    # Obter ações do usuário
    stocks = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    # Calcular valores totais
    total = user["cash"]
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["total"] = stock["price"] * stock["total_shares"]
        total += stock["total"]

    return render_template("index.html", stocks=stocks, cash=user["cash"], total=total)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validações
        if not symbol:
            return apology("must select symbol", 400)
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide positive integer", 400)

        shares = int(shares)
        stock = lookup(symbol)

        # Verificar se tem ações suficientes
        rows = db.execute("""
            SELECT SUM(shares) as total_shares
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, session["user_id"], symbol)

        if len(rows) != 1 or rows[0]["total_shares"] < shares:
            return apology("not enough shares", 400)

        # Atualizar banco de dados
        total_sale = stock["price"] * shares
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                  session["user_id"], symbol, -shares, stock["price"])

        return redirect("/")
    else:
        # Obter ações que o usuário possui
        stocks = db.execute("""
            SELECT symbol
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, session["user_id"])

        return render_template("sell.html", stocks=stocks)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("""
        SELECT symbol, shares, price, transacted
        FROM transactions
        WHERE user_id = ?
        ORDER BY transacted DESC
    """, session["user_id"])

    return render_template("history.html", transactions=transactions)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to account"""
    if request.method == "POST":
        amount = request.form.get("amount")

        # Validação
        if not amount or not amount.replace('.', '').isdigit() or float(amount) <= 0:
            return apology("must provide positive amount", 400)

        amount = float(amount)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, session["user_id"])

        return redirect("/")
    else:
        return render_template("add_cash.html")
