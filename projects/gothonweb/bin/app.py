import web
from gothonweb import map

#web.config.debug = False

urls=('/hello','HelloIndex',
    '/game','GameEngine',
    '/','Index',
    )


app=web.application(urls,globals())

if web.config.get('_session') is None:
    store=web.session.DiskStore('sessions')
    session=web.session.Session(app,store,initializer={'room':None})
    web.config._session=session

else:
    session=web.config._session

render=web.template.render('templates/',base='layout')

class Index:
    def GET(self):
        session.room=map.START
        web.seeother("/game")

class GameEngine:
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()
    def POST(self):
        form=web.input(action=None)

        if session.room and form.action:
            session.room=session.room.go(form.action)

        web.seeother("/game")
    
class HelloIndex:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form=web.input(name="Nobody",greet='Hello')
        greeting="%s, %s" %(form.greet, form.name)
        return render.index(greeting=greeting)

if __name__=="__main__":
    app.run()