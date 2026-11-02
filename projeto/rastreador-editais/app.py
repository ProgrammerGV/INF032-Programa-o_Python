import os
import threading
import time
from flask import Flask ,render_template ,request ,redirect ,url_for ,flash 
import pandas as pd 
from src .storage import carregar_config ,salvar_config ,carregar_todos_relatorios 
from src .monitor import executar_varredura 

app =Flask (__name__ )
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(32)
app.config['PUBLIC_DEMO'] = os.environ.get('RASTREADOR_PUBLIC_DEMO') == '1'
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024
scan_lock = threading.Lock()
last_public_scan = 0.0


@app.before_request
def public_demo_guard():
    if app.config['PUBLIC_DEMO'] and request.method == 'POST':
        return 'A demonstração pública usa configuração fixa. Explore as consultas e a varredura manual.', 403


@app.context_processor
def demo_context():
    return {'public_demo': app.config['PUBLIC_DEMO']}


@app.get('/healthz')
def healthz():
    return {'status': 'ok'}

@app.context_processor
def inject_notifications():
    try:
        df_relatorios = carregar_todos_relatorios()
        if df_relatorios.empty:
            return {'recent_alerts': [], 'unread_count': 0}
        novos = df_relatorios[df_relatorios['Status'] == 'Novo']
        unread_count = len(novos)
        # Pega os últimos 5
        recent_alerts = novos.head(5).to_dict('records')
        return {'recent_alerts': recent_alerts, 'unread_count': unread_count}
    except Exception as e:
        return {'recent_alerts': [], 'unread_count': 0}

@app .route ('/')
def index ():
    config =carregar_config ()
    page =request .args .get ('page',1 ,type =int )
    per_page =10 


    df_relatorios =carregar_todos_relatorios ()
    total_alertas =len (df_relatorios )
    import math 
    total_pages =math .ceil (total_alertas /per_page )if total_alertas >0 else 1 

    if df_relatorios .empty :
        relatorios =[]
    else :

        inicio =(page -1 )*per_page 
        fim =inicio +per_page 
        df_page =df_relatorios .iloc [inicio :fim ]
        relatorios =df_page .to_dict ('records')

    return render_template (
    'index.html',
    config =config ,
    total_sites =len (config .get ("urls",[])),
    total_palavras =len (config .get ("keywords",[])),
    total_alertas =total_alertas ,
    relatorios =relatorios ,
    page =page ,
    total_pages =total_pages 
    ,success_msg=request.args.get('success_msg')
    )

@app .route ('/salvar',methods =['POST'])
def salvar ():
    config =carregar_config ()


    keywords =request .form .get ('keywords','')
    telegram_token =request .form .get ('telegram_token','')
    telegram_chat_id =request .form .get ('telegram_chat_id','')
    ai_api_key =request .form .get ('ai_api_key','')
    filtros_cidades =request .form .get ('filtros_cidades','')
    filtros_areas =request .form .get ('filtros_areas','')


    config ['keywords']=[k .strip ()for k in keywords .split (',')if k .strip ()]
    config ['telegram_token']=telegram_token .strip ()
    config ['telegram_chat_id']=telegram_chat_id .strip ()
    config ['ai_api_key']=ai_api_key .strip ()
    config ['filtros_cidades']=[c .strip ()for c in filtros_cidades .split (',')if c .strip ()]
    config ['filtros_areas']=[a .strip ()for a in filtros_areas .split (',')if a .strip ()]

    salvar_config (config )

    return redirect (url_for ('index',success_msg ="Configuracoes salvas!"))

@app .route ('/rastrear')
def rastrear ():
    global last_public_scan
    if app.config['PUBLIC_DEMO']:
        if not scan_lock.acquire(blocking=False):
            return redirect(url_for('index', success_msg='Uma varredura já está em andamento.'))
        try:
            if last_public_scan and time.monotonic() - last_public_scan < 120:
                return redirect(url_for('index', success_msg='Confira o resultado recente. Nova varredura disponível em até dois minutos.'))
            executar_varredura()
            last_public_scan = time.monotonic()
        finally:
            scan_lock.release()
        return redirect(url_for('index', success_msg='Varredura das fontes de demonstração concluída.'))
    executar_varredura ()
    return redirect (url_for ('index',success_msg ="Varredura concluida com sucesso!"))

@app .route ('/historico/limpar',methods =['POST'])
def limpar_historico ():
    from src .storage import limpar_todo_historico 
    limpar_todo_historico ()
    return redirect (url_for ('index',success_msg ="Historico limpo completamente!"))

@app .route ('/historico/status/<hash_id>',methods =['POST'])
def status_historico (hash_id ):
    novo_status =request .form .get ('status','Novo')
    from src .storage import alterar_status 
    alterar_status (hash_id ,novo_status )
    return redirect (url_for ('index'))

@app .route ('/diretorio')
def diretorio ():
    regiao =request .args .get ('regiao','nacional')
    from src .diretorio_scraper import buscar_concursos_diretorio 
    concursos =buscar_concursos_diretorio (regiao )
    return render_template ('diretorio.html',concursos =concursos ,regiao_atual =regiao )

@app .route ('/sites')
def sites ():
    config =carregar_config ()
    urls =config .get ('urls',[])
    paused_urls =config .get ('paused_urls',[])
    return render_template ('sites.html',urls =urls ,paused_urls =paused_urls )

@app .route ('/sites/add',methods =['POST'])
def add_site ():
    config =carregar_config ()
    new_url =request .form .get ('url','').strip ()
    if new_url and new_url not in config .get ('urls',[])and new_url not in config .get ('paused_urls',[]):
        config .setdefault ('urls',[]).append (new_url )
        salvar_config (config )
    return redirect (url_for ('sites'))

@app .route ('/sites/remove',methods =['POST'])
def remove_site ():
    config =carregar_config ()
    url =request .form .get ('url','')
    if url in config .get ('urls',[]):
        config ['urls'].remove (url )
    elif url in config .get ('paused_urls',[]):
        config ['paused_urls'].remove (url )
    salvar_config (config )
    return redirect (url_for ('sites'))

@app .route ('/sites/toggle',methods =['POST'])
def toggle_site ():
    config =carregar_config ()
    url =request .form .get ('url','')
    if url in config .get ('urls',[]):
        config ['urls'].remove (url )
        config .setdefault ('paused_urls',[]).append (url )
    elif url in config .get ('paused_urls',[]):
        config ['paused_urls'].remove (url )
        config .setdefault ('urls',[]).append (url )
    salvar_config (config )
    return redirect (url_for ('sites'))

if __name__ =='__main__':
    app .run (host ='0.0.0.0',port =5000 ,debug =True )
