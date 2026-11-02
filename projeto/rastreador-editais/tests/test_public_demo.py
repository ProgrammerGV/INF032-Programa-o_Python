import importlib
from src.public_demo import demo_config
from src.storage import carregar_config


def test_public_config_does_not_load_visitor_or_saved_credentials(monkeypatch):
    monkeypatch.setenv('RASTREADOR_PUBLIC_DEMO', '1')
    config = carregar_config()
    assert config == demo_config()
    assert len(config['urls']) == 2
    assert not any(config[key] for key in ['telegram_token', 'telegram_chat_id', 'ai_api_key'])


def test_public_demo_blocks_mutations_and_has_health_check(monkeypatch):
    monkeypatch.setenv('RASTREADOR_PUBLIC_DEMO', '1')
    module = importlib.import_module('app')
    monkeypatch.setitem(module.app.config, 'PUBLIC_DEMO', True)
    with module.app.test_client() as client:
        assert client.get('/healthz').json == {'status': 'ok'}
        assert client.post('/salvar', data={'ai_api_key': 'visitor-value'}).status_code == 403
        assert client.post('/sites/add', data={'url': 'http://127.0.0.1/'}).status_code == 403


def test_public_scans_are_cooled_down_without_external_notifications(monkeypatch):
    module = importlib.import_module('app')
    monkeypatch.setitem(module.app.config, 'PUBLIC_DEMO', True)
    monkeypatch.setattr(module, 'last_public_scan', 0.0)
    calls = []
    monkeypatch.setattr(module, 'executar_varredura', lambda: calls.append('scan'))
    with module.app.test_client() as client:
        assert client.get('/rastrear').status_code == 302
        assert client.get('/rastrear').status_code == 302
    assert calls == ['scan']


def test_health_identifies_deployed_commit(monkeypatch):
    monkeypatch.setenv('RENDER_GIT_COMMIT', 'a' * 40)
    module = importlib.import_module('app')
    with module.app.test_client() as client:
        response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json['commit'] == 'a' * 40
