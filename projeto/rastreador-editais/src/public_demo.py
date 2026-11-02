"""Fixed public demonstration: no visitor credentials or configurable request destinations."""


def demo_config():
    return {
        'urls': [
            'https://ifbaiano.edu.br/portal/concursos/',
            'https://www.ifbaiano.edu.br/unidades/itapetinga/concursos-e-selecoes/',
        ],
        'keywords': ['edital', 'estágio', 'seleção'],
        'paused_urls': [], 'schedule_time': '08:00', 'timeout_seconds': 10,
        'telegram_token': '', 'telegram_chat_id': '', 'ai_api_key': '',
        'filtros_cidades': [], 'filtros_areas': [],
    }
