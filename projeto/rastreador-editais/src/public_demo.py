"""Fixed public demonstration: no visitor credentials or configurable request destinations."""


def demo_config():
    return {
        'urls': [
            'https://portal.ifba.edu.br/dgcom/editais',
            'https://portal.ifba.edu.br/simoes-filho/institucional/processos-seletivos/estagio-externo/estagio-externo-2026',
        ],
        'keywords': ['edital', 'estágio', 'seleção'],
        'paused_urls': [], 'schedule_time': '08:00', 'timeout_seconds': 10,
        'telegram_token': '', 'telegram_chat_id': '', 'ai_api_key': '',
        'filtros_cidades': [], 'filtros_areas': [],
    }
