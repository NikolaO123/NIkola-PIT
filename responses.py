def get_bot_response(message):
        message= message.lower()
        if "zdravo" in message or "cao" in message:
                return"Zdravo! Kako mogu da ti pomognem u vezi satova."
        elif "noviteti" in message:
                return"Novitete mozete naći na početnoj stranici kao i na posebnoj gde se nalaze svi noviteti."
        elif"cena" in message:
                return"Trenutno ne prodajemo satove."
        elif "youtube" in message:
                return"Link ka youtube stranici mozete pronaci na početnij stranici"
        else:
                return"Nisam siguran kako da odgovorim . Ponovi pitanje"