from django.db import models


class FamiliaBeneficiaria(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    codigo_familia = models.CharField(max_length=100)
    data_inquerito = models.DateField()
    nome_inquiridor = models.CharField(max_length=255)
    numero_questionario = models.IntegerField()
    local_entrevista = models.CharField(max_length=100)
    gps_local_lat_long = models.CharField(max_length=255)
    gps_local_accuracy = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_beneficiario = models.CharField(max_length=100)
    tipo_familia = models.CharField(max_length=100)
    nome_agg_familiar = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    photo_doc_url = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=100)
    outro_genero = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    parte_bd = models.CharField(max_length=20)
    criterios_elegib_agg_familiar = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    posto_administrativo = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    comunidade = models.CharField(max_length=100)
    ficha = models.CharField(max_length=100)


class AlocacaoTerra(models.Model):
    familia_beneficiaria = models.OneToOneField(
        FamiliaBeneficiaria, on_delete=models.CASCADE, primary_key=True)
    familia_tem_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    machamba_familia = models.CharField(max_length=100, null=True, blank=True)
    tipo_posse = models.CharField(max_length=100, null=True, blank=True)
    outro_tipo_posse = models.CharField(max_length=100, null=True, blank=True)
    forma_aquisicao = models.CharField(max_length=100, null=True, blank=True)
    outra_forma_aquisicao = models.CharField(
        max_length=100, null=True, blank=True)
    quando_conseguiu_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    outra_data = models.CharField(max_length=100, null=True, blank=True)
    tamanho_machamba = models.CharField(max_length=100, null=True, blank=True)
    local_machamba = models.CharField(max_length=100, null=True, blank=True)
    outro_local_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    caracteristica_solos = models.CharField(
        max_length=100, null=True, blank=True)
    outra_caracteristica_solos = models.CharField(
        max_length=100, null=True, blank=True)
    cor_solo = models.CharField(max_length=100, null=True, blank=True)
    historico_uso_solo = models.CharField(
        max_length=100, null=True, blank=True)
    outro_historico_uso_solo = models.CharField(
        max_length=100, null=True, blank=True)
    tempo_gasto_casa_machamba = models.CharField(
        max_length=100, null=True, blank=True)
    outro_tempo_gasto = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.familia_beneficiaria.nome_agg_familiar} {id}"


class Sementeira(models.Model):
    familia_beneficiaria = models.OneToOneField(
        FamiliaBeneficiaria, on_delete=models.CASCADE, primary_key=True)
    recebeu_semente = models.CharField(max_length=100, null=True, blank=True)
    quando_recebeu = models.CharField(max_length=100, null=True, blank=True)
    outra_data_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    identificacao_lote = models.CharField(
        max_length=100, null=True, blank=True)
    tipo_kit = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_a = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_a = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_b = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_b = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_c = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_c = models.CharField(max_length=100, null=True, blank=True)
    composicao_kit_d = models.CharField(max_length=100, null=True, blank=True)
    comentario_kit_d = models.CharField(max_length=100, null=True, blank=True)
    conservacao_semente = models.CharField(
        max_length=100, null=True, blank=True)
    foto_semente_url = models.CharField(max_length=255, null=True, blank=True)
    de_quem_recebeu_semente = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_semente = models.CharField(
        max_length=100, null=True, blank=True)
    quem_escolheu_kit = models.CharField(max_length=100, null=True, blank=True)
    outro_quem_escolheu_kit = models.CharField(
        max_length=100, null=True, blank=True)
    quando_realizou_sementeira = models.CharField(
        max_length=100, null=True, blank=True)
    familia_necess_nao_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    nome_familia = models.CharField(max_length=100, null=True, blank=True)
    sementes_germinou = models.CharField(max_length=100, null=True, blank=True)
    foto_sementes_germinou_url = models.CharField(
        max_length=255, null=True, blank=True)
    semente_nao_germinou = models.CharField(
        max_length=100, null=True, blank=True)
    usou_fertilizante = models.CharField(max_length=100, null=True, blank=True)
    tipo_fertilizante = models.CharField(max_length=100, null=True, blank=True)
    outro_tipo_fertilizante = models.CharField(
        max_length=100, null=True, blank=True)
    momento_usou_adubo = models.CharField(
        max_length=100, null=True, blank=True)
    outro_momento_usou_adubo = models.CharField(
        max_length=100, null=True, blank=True)
    adubo_usado = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.familia_beneficiaria.nome_agg_familiar


class TipoSementeGerminou(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    nome_semente = models.CharField(max_length=100, null=True, blank=True)
    familia_beneficiaria = models.ForeignKey(
        FamiliaBeneficiaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_semente


class TipoAreaGerminacao(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    nome_semente = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    familia_beneficiaria = models.ForeignKey(
        FamiliaBeneficiaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_semente


class Treinamento(models.Model):
    recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    lugar_treinamento = models.CharField(max_length=100, null=True, blank=True)
    outro_lugar_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    de_quem_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    quando_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    outro_quando_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    tipo_treinamento = models.CharField(max_length=100, null=True, blank=True)
    recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    de_quem_recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    outro_de_quem_recebeu_visita_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    momento_recebeu_visita = models.CharField(
        max_length=100, null=True, blank=True)
    familia_nao_recebeu_treinamento = models.CharField(
        max_length=100, null=True, blank=True)
    nome_familia_nao_recebeu = models.CharField(
        max_length=100, null=True, blank=True)
    familia_beneficiaria = models.ForeignKey(
        FamiliaBeneficiaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.familia_beneficiaria.nome_agg_familiar


class Reclamacao(models.Model):
    canais_apresentar_reclamacao = models.CharField(
        max_length=100, null=True, blank=True)
    apresentou_reclamacao = models.CharField(
        max_length=100, null=True, blank=True)
    canal_que_usou = models.CharField(max_length=100, null=True, blank=True)
    outro_canal = models.CharField(max_length=100, null=True, blank=True)
    tempo_gasto_resolver = models.CharField(
        max_length=100, null=True, blank=True)
    ficou_satisfeito = models.CharField(max_length=100, null=True, blank=True)
    familia_beneficiaria = models.ForeignKey(
        FamiliaBeneficiaria, on_delete=models.CASCADE)


class VBG(models.Model):
    ouviu_falar_vbg = models.CharField(max_length=100, null=True, blank=True)
    ja_foi_vitima_vbg = models.CharField(max_length=100, null=True, blank=True)
    canais_denunciar_vbg = models.CharField(
        max_length=100, null=True, blank=True)
    outro_canal_denuncia = models.CharField(
        max_length=100, null=True, blank=True)
    teve_toda_assistencia = models.CharField(
        max_length=100, null=True, blank=True)
    e_comum_vbg_comunidade = models.CharField(
        max_length=100, null=True, blank=True)
    casos_vbg_ouviu_falar = models.CharField(
        max_length=100, null=True, blank=True)
    outro_caso_vbg_ouviu_falar = models.CharField(
        max_length=100, null=True, blank=True)
    foto_caso_vbg_url = models.CharField(max_length=255, null=True, blank=True)
    familia_beneficiaria = models.ForeignKey(
        FamiliaBeneficiaria, on_delete=models.CASCADE)
