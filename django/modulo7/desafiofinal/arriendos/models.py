from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.db.models.signals import post_save

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class TipoUsuario(models.TextChoices):
        arrendatario = ("ART", "Arrendatario")
        arrendador = ("ARD", "Arrendador")

    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    correo = models.CharField(max_length=50, unique=True, null=False)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20, null=False)
    tipo_usuario = models.CharField(choices=TipoUsuario.choices)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "correo"
    EMAIL_FIELD = "correo"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.rut}- {self.nombre} {self.apellido}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



class Regiones(models.TextChoices):
    ARICA_Y_PARINACOTA = "Arica y Parinacota", "Arica y Parinacota"
    TARAPACA = "Tarapacá", "Tarapacá"
    ANTOFAGASTA = "Antofagasta", "Antofagasta"
    ATACAMA = "Atacama", "Atacama"
    COQUIMBO = "Coquimbo", "Coquimbo"
    VALPARAISO = "Valparaíso", "Valparaíso"
    REGION_DEL_LIBERTADOR_GRAL_BERNARDO_OHIGGINS = "Región del Libertador Gral. Bernardo O’Higgins", "Región del Libertador Gral. Bernardo O’Higgins"
    REGION_DEL_MAULE = "Región del Maule", "Región del Maule"
    REGION_DE_NUBLE = "Región de Ñuble", "Región de Ñuble"
    REGION_DEL_BIOBIO = "Región del Biobío", "Región del Biobío"
    REGION_DE_LA_ARAUCANIA = "Región de la Araucanía", "Región de la Araucanía"
    REGION_DE_LOS_RIOS = "Región de Los Ríos", "Región de Los Ríos"
    REGION_DE_LOS_LAGOS = "Región de Los Lagos", "Región de Los Lagos"
    REGION_AISEN_DEL_GRAL_CARLOS_IBANEZ_DEL_CAMPO = "Región Aisén del Gral. Carlos Ibáñez del Campo", "Región Aisén del Gral. Carlos Ibáñez del Campo"
    REGION_DE_MAGALLANES_Y_DE_LA_ANTARTICA_CHILENA = "Región de Magallanes y de la Antártica Chilena", "Región de Magallanes y de la Antártica Chilena"
    REGION_METROPOLITANA_DE_SANTIAGO = "Región Metropolitana de Santiago", "Región Metropolitana de Santiago"

class Comunas(models.TextChoices):
    ARICA = "Arica", "Arica"
    CAMARONES = "Camarones", "Camarones"
    PUTRE = "Putre", "Putre"
    GENERAL_LAGOS = "General Lagos", "General Lagos"
    IQUIQUE = "Iquique", "Iquique"
    ALTO_HOSPICIO = "Alto Hospicio", "Alto Hospicio"
    POZO_ALMONTE = "Pozo Almonte", "Pozo Almonte"
    CAMINA = "Camiña", "Camiña"
    COLCHANE = "Colchane", "Colchane"
    HUARA = "Huara", "Huara"
    PICA = "Pica", "Pica"
    ANTOFAGASTA = "Antofagasta", "Antofagasta"
    MEJILLONES = "Mejillones", "Mejillones"
    SIERRA_GORDA = "Sierra Gorda", "Sierra Gorda"
    TALTAL = "Taltal", "Taltal"
    CALAMA = "Calama", "Calama"
    OLLAGUE = "Ollagüe", "Ollagüe"
    SAN_PEDRO_DE_ATACAMA = "San Pedro de Atacama", "San Pedro de Atacama"
    TOCOPILLA = "Tocopilla", "Tocopilla"
    MARIA_ELENA = "María Elena", "María Elena"
    COPIAPO = "Copiapó", "Copiapó"
    CALDERA = "Caldera", "Caldera"
    TIERRA_AMARILLA = "Tierra Amarilla", "Tierra Amarilla"
    CHANARAL = "Chañaral", "Chañaral"
    DIEGO_DE_ALMAGRO = "Diego de Almagro", "Diego de Almagro"
    VALLENAR = "Vallenar", "Vallenar"
    ALTO_DEL_CARMEN = "Alto del Carmen", "Alto del Carmen"
    FREIRINA = "Freirina", "Freirina"
    HUASCO = "Huasco", "Huasco"
    LA_SERENA = "La Serena", "La Serena"
    COQUIMBO = "Coquimbo", "Coquimbo"
    ANDACOLLO = "Andacollo", "Andacollo"
    LA_HIGUERA = "La Higuera", "La Higuera"
    PAIGUANO = "Paiguano", "Paiguano"
    VICUNA = "Vicuña", "Vicuña"
    ILLAPEL = "Illapel", "Illapel"
    CANELA = "Canela", "Canela"
    LOS_VILOS = "Los Vilos", "Los Vilos"
    SALAMANCA = "Salamanca", "Salamanca"
    OVALLE = "Ovalle", "Ovalle"
    COMBARBALA = "Combarbalá", "Combarbalá"
    MONTE_PATRIA = "Monte Patria", "Monte Patria"
    PUNITAQUI = "Punitaqui", "Punitaqui"
    RIO_HURTADO = "Río Hurtado", "Río Hurtado"
    VALPARAISO = "Valparaíso", "Valparaíso"
    CASABLANCA = "Casablanca", "Casablanca"
    CONCON = "Concón", "Concón"
    JUAN_FERNANDEZ = "Juan Fernández", "Juan Fernández"
    PUCHUNCAVI = "Puchuncaví", "Puchuncaví"
    QUINTERO = "Quintero", "Quintero"
    VINA_DEL_MAR = "Viña del Mar", "Viña del Mar"
    ISLA_DE_PASCUA = "Isla de Pascua", "Isla de Pascua"
    LOS_ANDES = "Los Andes", "Los Andes"
    CALLE_LARGA = "Calle Larga", "Calle Larga"
    RINCONADA = "Rinconada", "Rinconada"
    SAN_ESTEBAN = "San Esteban", "San Esteban"
    LA_LIGUA = "La Ligua", "La Ligua"
    CABILDO = "Cabildo", "Cabildo"
    PAPUDO = "Papudo", "Papudo"
    PETORCA = "Petorca", "Petorca"
    ZAPALLAR = "Zapallar", "Zapallar"
    QUILLOTA = "Quillota", "Quillota"
    CALERA = "Calera", "Calera"
    HIJUELAS = "Hijuelas", "Hijuelas"
    LA_CRUZ = "La Cruz", "La Cruz"
    NOGALES = "Nogales", "Nogales"
    SAN_ANTONIO = "San Antonio", "San Antonio"
    ALGARROBO = "Algarrobo", "Algarrobo"
    CARTAGENA = "Cartagena", "Cartagena"
    EL_QUISCO = "El Quisco", "El Quisco"
    EL_TABO = "El Tabo", "El Tabo"
    SANTO_DOMINGO = "Santo Domingo", "Santo Domingo"
    SAN_FELIPE = "San Felipe", "San Felipe"
    CATEMU = "Catemu", "Catemu"
    LLAILLAY = "Llaillay", "Llaillay"
    PANQUEHUE = "Panquehue", "Panquehue"
    PUTAENDO = "Putaendo", "Putaendo"
    SANTA_MARIA = "Santa María", "Santa María"
    QUILPUE = "Quilpué", "Quilpué"
    LIMACHE = "Limache", "Limache"
    OLMUE = "Olmué", "Olmué"
    VILLA_ALEMANA = "Villa Alemana", "Villa Alemana"
    RANCAGUA = "Rancagua", "Rancagua"
    CODEGUA = "Codegua", "Codegua"
    COINCO = "Coinco", "Coinco"
    COLTAUCO = "Coltauco", "Coltauco"
    DONIHUE = "Doñihue", "Doñihue"
    GRANEROS = "Graneros", "Graneros"
    LAS_CABRAS = "Las Cabras", "Las Cabras"
    MACHALI = "Machalí", "Machalí"
    MALLOA = "Malloa", "Malloa"
    MOSTAZAL = "Mostazal", "Mostazal"
    OLIVAR = "Olivar", "Olivar"
    PEUMO = "Peumo", "Peumo"
    PICHIDEGUA = "Pichidegua", "Pichidegua"
    QUINTA_DE_TILCOCO = "Quinta de Tilcoco", "Quinta de Tilcoco"
    RENGO = "Rengo", "Rengo"
    REQUINOA = "Requínoa", "Requínoa"
    SAN_VICENTE = "San Vicente", "San Vicente"
    PICHILEMU = "Pichilemu", "Pichilemu"
    LA_ESTRELLA = "La Estrella", "La Estrella"
    LITUECHE = "Litueche", "Litueche"
    MARCHIHUE = "Marchihue", "Marchihue"
    NAVIDAD = "Navidad", "Navidad"
    PAREDONES = "Paredones", "Paredones"
    SAN_FERNANDO = "San Fernando", "San Fernando"
    CHEPICA = "Chépica", "Chépica"
    CHIMBARONGO = "Chimbarongo", "Chimbarongo"
    LOLOL = "Lolol", "Lolol"
    NANCAGUA = "Nancagua", "Nancagua"
    PALMILLA = "Palmilla", "Palmilla"
    PERALILLO = "Peralillo", "Peralillo"
    PLACILLA = "Placilla", "Placilla"
    PUMANQUE = "Pumanque", "Pumanque"
    SANTA_CRUZ = "Santa Cruz", "Santa Cruz"
    TALCA = "Talca", "Talca"
    CONSTITUCION = "Constitución", "Constitución"
    CUREPTO = "Curepto", "Curepto"
    EMPEDRADO = "Empedrado", "Empedrado"
    MAULE = "Maule", "Maule"
    PELARCO = "Pelarco", "Pelarco"
    PENCAHUE = "Pencahue", "Pencahue"
    RIO_CLARO = "Río Claro", "Río Claro"
    SAN_CLEMENTE = "San Clemente", "San Clemente"
    SAN_RAFAEL = "San Rafael", "San Rafael"
    CAUQUENES = "Cauquenes", "Cauquenes"
    CHANCO = "Chanco", "Chanco"
    PELLUHUE = "Pelluhue", "Pelluhue"
    CURICO = "Curicó", "Curicó"
    HUALANE = "Hualañé", "Hualañé"
    LICANTEN = "Licantén", "Licantén"
    MOLINA = "Molina", "Molina"
    RAUCO = "Rauco", "Rauco"
    ROMERAL = "Romeral", "Romeral"
    SAGRADA_FAMILIA = "Sagrada Familia", "Sagrada Familia"
    TENO = "Teno", "Teno"
    VICHUQUEN = "Vichuquén", "Vichuquén"
    LINARES = "Linares", "Linares"
    COLBUN = "Colbún", "Colbún"
    LONGAVI = "Longaví", "Longaví"
    PARRAL = "Parral", "Parral"
    RETIRO = "Retiro", "Retiro"
    SAN_JAVIER = "San Javier", "San Javier"
    VILLA_ALEGRE = "Villa Alegre", "Villa Alegre"
    YERBAS_BUENAS = "Yerbas Buenas", "Yerbas Buenas"
    COBQUECURA = "Cobquecura", "Cobquecura"
    COELEMU = "Coelemu", "Coelemu"
    NINHUE = "Ninhue", "Ninhue"
    PORTEZUELO = "Portezuelo", "Portezuelo"
    QUIRIHUE = "Quirihue", "Quirihue"
    RANQUIL = "Ránquil", "Ránquil"
    TREGUACO = "Treguaco", "Treguaco"
    BULNES = "Bulnes", "Bulnes"
    CHILLAN_VIEJO = "Chillán Viejo", "Chillán Viejo"
    CHILLAN = "Chillán", "Chillán"
    EL_CARMEN = "El Carmen", "El Carmen"
    PEMUCO = "Pemuco", "Pemuco"
    PINTO = "Pinto", "Pinto"
    QUILLON = "Quillón", "Quillón"
    SAN_IGNACIO = "San Ignacio", "San Ignacio"
    YUNGAY = "Yungay", "Yungay"
    COIHUECO = "Coihueco", "Coihueco"
    NIQUEN = "Ñiquén", "Ñiquén"
    SAN_CARLOS = "San Carlos", "San Carlos"
    SAN_FABIAN = "San Fabián", "San Fabián"
    SAN_NICOLAS = "San Nicolás", "San Nicolás"
    CONCEPCION = "Concepción", "Concepción"
    CORONEL = "Coronel", "Coronel"
    CHIGUAYANTE = "Chiguayante", "Chiguayante"
    FLORIDA = "Florida", "Florida"
    HUALQUI = "Hualqui", "Hualqui"
    LOTA = "Lota", "Lota"
    PENCO = "Penco", "Penco"
    SAN_PEDRO_DE_LA_PAZ = "San Pedro de la Paz", "San Pedro de la Paz"
    SANTA_JUANA = "Santa Juana", "Santa Juana"
    TALCAHUANO = "Talcahuano", "Talcahuano"
    TOME = "Tomé", "Tomé"
    HUALPEN = "Hualpén", "Hualpén"
    LEBU = "Lebu", "Lebu"
    ARAUCO = "Arauco", "Arauco"
    CANETE = "Cañete", "Cañete"
    CONTULMO = "Contulmo", "Contulmo"
    CURANILAHUE = "Curanilahue", "Curanilahue"
    LOS_ALAMOS = "Los Álamos", "Los Álamos"
    TIRUA = "Tirúa", "Tirúa"
    LOS_ANGELES = "Los Ángeles", "Los Ángeles"
    ANTUCO = "Antuco", "Antuco"
    CABRERO = "Cabrero", "Cabrero"
    LAJA = "Laja", "Laja"
    MULCHEN = "Mulchén", "Mulchén"
    NACIMIENTO = "Nacimiento", "Nacimiento"
    NEGRETE = "Negrete", "Negrete"
    QUILACO = "Quilaco", "Quilaco"
    QUILLECO = "Quilleco", "Quilleco"
    SAN_ROSENDO = "San Rosendo", "San Rosendo"
    SANTA_BARBARA = "Santa Bárbara", "Santa Bárbara"
    TUCAPEL = "Tucapel", "Tucapel"
    YUMBEL = "Yumbel", "Yumbel"
    ALTO_BIOBIO = "Alto Biobío", "Alto Biobío"
    TEMUCO = "Temuco", "Temuco"
    CARAHUE = "Carahue", "Carahue"
    CUNCO = "Cunco", "Cunco"
    CURARREHUE = "Curarrehue", "Curarrehue"
    FREIRE = "Freire", "Freire"
    GALVARINO = "Galvarino", "Galvarino"
    GORBEA = "Gorbea", "Gorbea"
    LAUTARO = "Lautaro", "Lautaro"
    LONCOCHE = "Loncoche", "Loncoche"
    MELIPEUCO = "Melipeuco", "Melipeuco"
    NUEVA_IMPERIAL = "Nueva Imperial", "Nueva Imperial"
    PADRE_LAS_CASAS = "Padre las Casas", "Padre las Casas"
    PERQUENCO = "Perquenco", "Perquenco"
    PITRUFQUEN = "Pitrufquén", "Pitrufquén"
    PUCON = "Pucón", "Pucón"
    SAAVEDRA = "Saavedra", "Saavedra"
    TEODORO_SCHMIDT = "Teodoro Schmidt", "Teodoro Schmidt"
    TOLTEN = "Toltén", "Toltén"
    VILCUN = "Vilcún", "Vilcún"
    VILLARRICA = "Villarrica", "Villarrica"
    CHOLCHOL = "Cholchol", "Cholchol"
    ANGOL = "Angol", "Angol"
    COLLIPULLI = "Collipulli", "Collipulli"
    CURACAUTIN = "Curacautín", "Curacautín"
    ERCILLA = "Ercilla", "Ercilla"
    LONQUIMAY = "Lonquimay", "Lonquimay"
    LOS_SAUCES = "Los Sauces", "Los Sauces"
    LUMACO = "Lumaco", "Lumaco"
    PUREN = "Purén", "Purén"
    RENAICO = "Renaico", "Renaico"
    TRAIGUEN = "Traiguén", "Traiguén"
    VICTORIA = "Victoria", "Victoria"
    VALDIVIA = "Valdivia", "Valdivia"
    CORRAL = "Corral", "Corral"
    LANCO = "Lanco", "Lanco"
    LOS_LAGOS = "Los Lagos", "Los Lagos"
    MAFIL = "Máfil", "Máfil"
    MARIQUINA = "Mariquina", "Mariquina"
    PAILLACO = "Paillaco", "Paillaco"
    PANGUIPULLI = "Panguipulli", "Panguipulli"
    LA_UNION = "La Unión", "La Unión"
    FUTRONO = "Futrono", "Futrono"
    LAGO_RANCO = "Lago Ranco", "Lago Ranco"
    RIO_BUENO = "Río Bueno", "Río Bueno"
    PUERTO_MONTT = "Puerto Montt", "Puerto Montt"
    CALBUCO = "Calbuco", "Calbuco"
    COCHAMO = "Cochamó", "Cochamó"
    FRESIA = "Fresia", "Fresia"
    FRUTILLAR = "Frutillar", "Frutillar"
    LOS_MUERMOS = "Los Muermos", "Los Muermos"
    LLANQUIHUE = "Llanquihue", "Llanquihue"
    MAULLIN = "Maullín", "Maullín"
    PUERTO_VARAS = "Puerto Varas", "Puerto Varas"
    CASTRO = "Castro", "Castro"
    ANCUD = "Ancud", "Ancud"
    CHONCHI = "Chonchi", "Chonchi"
    CURACO_DE_VELEZ = "Curaco de Vélez", "Curaco de Vélez"
    DALCAHUE = "Dalcahue", "Dalcahue"
    PUQUELDON = "Puqueldón", "Puqueldón"
    QUEILEN = "Queilén", "Queilén"
    QUELLON = "Quellón", "Quellón"
    QUEMCHI = "Quemchi", "Quemchi"
    QUINCHAO = "Quinchao", "Quinchao"
    OSORNO = "Osorno", "Osorno"
    PUERTO_OCTAY = "Puerto Octay", "Puerto Octay"
    PURRANQUE = "Purranque", "Purranque"
    PUYEHUE = "Puyehue", "Puyehue"
    RIO_NEGRO = "Río Negro", "Río Negro"
    SAN_JUAN_DE_LA_COSTA = "San Juan de la Costa", "San Juan de la Costa"
    SAN_PABLO = "San Pablo", "San Pablo"
    CHAITEN = "Chaitén", "Chaitén"
    FUTALEUFU = "Futaleufú", "Futaleufú"
    HUALAIHUE = "Hualaihué", "Hualaihué"
    PALENA = "Palena", "Palena"
    COIHAIQUE = "Coihaique", "Coihaique"
    LAGO_VERDE = "Lago Verde", "Lago Verde"
    AISEN = "Aisén", "Aisén"
    CISNES = "Cisnes", "Cisnes"
    GUAITECAS = "Guaitecas", "Guaitecas"
    COCHRANE = "Cochrane", "Cochrane"
    OHIGGINS = "O’Higgins", "O’Higgins"
    TORTEL = "Tortel", "Tortel"
    CHILE_CHICO = "Chile Chico", "Chile Chico"
    RIO_IBANEZ = "Río Ibáñez", "Río Ibáñez"
    PUNTA_ARENAS = "Punta Arenas", "Punta Arenas"
    LAGUNA_BLANCA = "Laguna Blanca", "Laguna Blanca"
    RIO_VERDE = "Río Verde", "Río Verde"
    SAN_GREGORIO = "San Gregorio", "San Gregorio"
    CABO_DE_HORNOS = "Cabo de Hornos", "Cabo de Hornos"
    ANTARTICA = "Antártica", "Antártica"
    PORVENIR = "Porvenir", "Porvenir"
    PRIMAVERA = "Primavera", "Primavera"
    TIMAUKEL = "Timaukel", "Timaukel"
    NATALES = "Natales", "Natales"
    TORRES_DEL_PAINE = "Torres del Paine", "Torres del Paine"
    CERRILLOS = "Cerrillos", "Cerrillos"
    CERRO_NAVIA = "Cerro Navia", "Cerro Navia"
    CONCHALI = "Conchalí", "Conchalí"
    EL_BOSQUE = "El Bosque", "El Bosque"
    ESTACION_CENTRAL = "Estación Central", "Estación Central"
    HUECHURABA = "Huechuraba", "Huechuraba"
    INDEPENDENCIA = "Independencia", "Independencia"
    LA_CISTERNA = "La Cisterna", "La Cisterna"
    LA_FLORIDA = "La Florida", "La Florida"
    LA_GRANJA = "La Granja", "La Granja"
    LA_PINTANA = "La Pintana", "La Pintana"
    LA_REINA = "La Reina", "La Reina"
    LAS_CONDES = "Las Condes", "Las Condes"
    LO_BARNECHEA = "Lo Barnechea", "Lo Barnechea"
    LO_ESPEJO = "Lo Espejo", "Lo Espejo"
    LO_PRADO = "Lo Prado", "Lo Prado"
    MACUL = "Macul", "Macul"
    MAIPU = "Maipú", "Maipú"
    NUNOA = "Ñuñoa", "Ñuñoa"
    PEDRO_AGUIRRE_CERDA = "Pedro Aguirre Cerda", "Pedro Aguirre Cerda"
    PENALOLEN = "Peñalolén", "Peñalolén"
    PROVIDENCIA = "Providencia", "Providencia"
    PUDAHUEL = "Pudahuel", "Pudahuel"
    QUILICURA = "Quilicura", "Quilicura"
    QUINTA_NORMAL = "Quinta Normal", "Quinta Normal"
    RECOLETA = "Recoleta", "Recoleta"
    RENCA = "Renca", "Renca"
    SANTIAGO = "Santiago", "Santiago"
    SAN_JOAQUIN = "San Joaquín", "San Joaquín"
    SAN_MIGUEL = "San Miguel", "San Miguel"
    SAN_RAMON = "San Ramón", "San Ramón"
    VITACURA = "Vitacura", "Vitacura"
    PUENTE_ALTO = "Puente Alto", "Puente Alto"
    PIRQUE = "Pirque", "Pirque"
    SAN_JOSE_DE_MAIPO = "San José de Maipo", "San José de Maipo"
    COLINA = "Colina", "Colina"
    LAMPA = "Lampa", "Lampa"
    TILTIL = "Tiltil", "Tiltil"
    SAN_BERNARDO = "San Bernardo", "San Bernardo"
    BUIN = "Buin", "Buin"
    CALERA_DE_TANGO = "Calera de Tango", "Calera de Tango"
    PAINE = "Paine", "Paine"
    MELIPILLA = "Melipilla", "Melipilla"
    ALHUE = "Alhué", "Alhué"
    CURACAVI = "Curacaví", "Curacaví"
    MARIA_PINTO = "María Pinto", "María Pinto"
    SAN_PEDRO = "San Pedro", "San Pedro"
    TALAGANTE = "Talagante", "Talagante"
    EL_MONTE = "El Monte", "El Monte"
    ISLA_DE_MAIPO = "Isla de Maipo", "Isla de Maipo"
    PADRE_HURTADO = "Padre Hurtado", "Padre Hurtado"
    PENAFLOR = "Peñaflor", "Peñaflor"

class Inmuebles(models.Model):
    class TipoInmueble(models.TextChoices):
        departamento = ("DPTO", "Departamento")
        casa = ("CS", "Casa")
        parcela = ("PRCL", "Parcela")

    id_usuario = models.ForeignKey(CustomUser, related_name="inmuebles", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=False)
    m2_construidos = models.CharField(max_length=10, null=False)
    m2_totales = models.CharField(max_length=10, null=False)
    cantidad_estacionamientos = models.PositiveIntegerField(null=False)
    cantidad_habitaciones = models.PositiveIntegerField(null=False)
    cantidad_baños = models.PositiveIntegerField(null=False)
    direccion = models.CharField(max_length=20, null=False)
    region = models.CharField(choices=Regiones.choices)
    comuna = models.CharField(choices=Comunas.choices)
    tipo_inmueble = models.CharField(choices=TipoInmueble.choices)
    precio_mensual = models.CharField(null=False)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.direccion}"


