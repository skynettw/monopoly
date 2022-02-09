import uuid
from django.shortcuts import render, redirect
from mysite.models import Game, GameUser

def index(request):
    games = Game.objects.all()
    return render(request, "index.html", locals())

def newgame(request):
    if request.method=="POST":
        players = [""] * 4
        name = request.POST.get("name")
        players[0] = request.POST.get("player1")
        players[1] = request.POST.get("player2")
        players[2] = request.POST.get("player3")
        players[3] = request.POST.get("player4")
        money = request.POST.get("money")
        game = Game()
        game.name = name
        game.gid = str(uuid.uuid4())[:4]
        game.save()
        for player in players:
            if player != "":
                p = GameUser()
                p.name = player 
                p.game = game 
                p.money = int(money)
                p.save()
        return redirect("/list/")
    else:
        games = Game.objects.all()  
    return render(request, "newgame.html", locals())

def listgame(request):
    games = Game.objects.all()
    return render(request, "listgame.html", locals())

def info(request, id=1):
    game = Game.objects.get(id=id)
    players = GameUser.objects.filter(game=game).filter(status=0)
    return render(request, "info.html", locals())

def join(request, gid=1, pid=1):
    game = Game.objects.get(id=gid)
    players = GameUser.objects.filter(game=game)
    player = GameUser.objects.get(id=pid)
    return render(request, "gamepage.html", locals())

def access(request, gid, pid):
    if request.method=="POST":
        etype = request.POST.get("etype")
        target = request.POST.get("target")
        amount = request.POST.get("amount")
        if target=='0':
            target_player = GameUser.objects.get(id=pid)
            if etype=="0":
                target_player.money = target_player.money + int(amount)
            else:
                target_player.money = target_player.money - int(amount)
            target_player.save()
            print(target_player.money)
            print(target_player.name)
        else:
            target_player = GameUser.objects.get(id=target)
            my_account = GameUser.objects.get(id=pid)
            if etype=="0":
                my_account.money = my_account.money + int(amount)
                target_player.money = target_player.money - int(amount)
            else:
                my_account.money = my_account.money - int(amount)
                target_player.money = target_player.money + int(amount)
            my_account.save()
            target_player.save()
    return redirect("/join/{}/{}/".format(gid, pid))

def delete(request, id):
    target = Game.objects.get(id=id)
    target.delete()
    return redirect("/list/")