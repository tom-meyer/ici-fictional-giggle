from creatures import (
    accalathura,
    addax,
    aega,
    amakusanthura,
    antarcturus,
    apanthura,
    arcturus,
    austroniscus,
)

def rollcall():
    print "Aye aye, captain"
    print "----------------"
    print "-", accalathura.Accalathura()
    print "-", addax.Addax()
    print "-", aega.Aega()
    print "-", amakusanthura.Amakusanthura()
    print "-", antarcturus.Antarcturus()
    print "-", apanthura.Apanthura()
    print "-", arcturus.Arcturus()
    print "-", austroniscus.Austroniscus()

if __name__ == '__main__':
    rollcall()
