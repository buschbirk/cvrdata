# coding: utf-8
from sqlalchemy import (BigInteger, Column, DateTime,
                        Enum, Float, Index, Integer,
                        SmallInteger, String, text, Text, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from collections import namedtuple
from . import engine as proxy_engine

Base = declarative_base()
metadata = Base.metadata
default_start_date = text("'1900-01-01 00:00:00'")
default_end_date = text("'2200-01-01 00:00:00'")


class DBModel(object):
    def __init__(self):
        self.proxy_engine = proxy_engine
        metadata.reflect(bind=proxy_engine.get(), views=True)
        #metadata.reflect(bind=proxy_engine)
        Base = automap_base(metadata=metadata)
        Base.prepare()
        #self.proxy_engine = proxy_engine
        self.tables = namedtuple('tables', metadata.tables.keys())(*metadata.tables.values())
        self.tables_dict = self.tables._asdict()
        self.classes = Base.classes


class Aarsbeskaeftigelse(Base):
    __tablename__ = 'aarsbeskaeftigelse'

    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    ansatteinklusivejere = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    ansatteinklusivejereinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)


class Kvartalsbeskaeftigelse(Base):
    __tablename__ = 'kvartalsbeskaeftigelse'
    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    kvartal = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)

    
class Maanedsbeskaeftigelse(Base):
    __tablename__ = 'maanedsbeskaeftigelse'
    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    maaned = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)

class erstAarsbeskaeftigelse(Base):
    __tablename__ = 'erstaarsbeskaeftigelse'

    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    ansatteinklusivejere = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    ansatteinklusivejereinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)


class erstKvartalsbeskaeftigelse(Base):
    __tablename__ = 'erstkvartalsbeskaeftigelse'
    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    kvartal = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)

    
class erstMaanedsbeskaeftigelse(Base):
    __tablename__ = 'erstmaanedsbeskaeftigelse'
    enhedsnummer = Column(BigInteger, primary_key=True, nullable=False)
    aar = Column(Integer, primary_key=True, nullable=False)
    maaned = Column(Integer, primary_key=True, nullable=False)
    aarsvaerk = Column(Integer)
    ansatte = Column(Integer)
    aarsvaerkinterval = Column(String(40))
    ansatteinterval = Column(String(40))
    sidstopdateret = Column(DateTime, nullable=True)



class AdresseDawa(Base):
    __tablename__ = 'adressedawa'

    # adresseid = Column(Integer, primary_key=True)
    id = Column(String(40), nullable=False, primary_key=True)
    status = Column(Integer)
    oprettet = Column(DateTime)
    ændret = Column(DateTime)
    vejkode = Column(SmallInteger)
    vejnavn = Column(String(50))
    adresseringsvejnavn = Column(String(50))
    husnr = Column(String(5))
    etage = Column(String(2))
    dør = Column(String(6))
    supplerendebynavn = Column(String(50))
    postnr = Column(SmallInteger)
    postnrnavn = Column(String(50))
    stormodtagerpostnr = Column(SmallInteger)
    stormodtagerpostnrnavn = Column(String(50))
    kommunekode = Column(SmallInteger)
    kommunenavn = Column(String(50))
    ejerlavkode = Column(Integer)
    ejerlavnavn = Column(String(50))
    matrikelnr = Column(String(10))
    esrejendomsnr = Column(Integer)
    etrs89koordinat_øst = Column(Float)
    etrs89koordinat_nord = Column(Float)
    wgs84koordinat_bredde = Column(Float)
    wgs84koordinat_længde = Column(Float)
    nøjagtighed = Column(String(2))
    kilde = Column(Integer)
    tekniskstandard = Column(String(2))
    tekstretning = Column(Float)
    ddkn_m100 = Column(String(20))
    ddkn_km1 = Column(String(20))
    ddkn_km10 = Column(String(20))
    adressepunktændringsdato = Column(DateTime)
    adgangsadresseid = Column(String(40))
    adgangsadresse_status = Column(String(1))
    adgangsadresse_oprettet = Column(DateTime)
    adgangsadresse_ændret = Column(DateTime)
    regionskode = Column(SmallInteger)
    regionsnavn = Column(String(50))
    jordstykke_ejerlavnavn = Column(String(100))
    kvhx = Column(String(20))
    sognekode = Column(SmallInteger)
    sognenavn = Column(String(50))
    politikredskode = Column(SmallInteger)
    politikredsnavn = Column(String(100))
    retskredskode = Column(SmallInteger)
    retskredsnavn = Column(String(100))
    opstillingskredskode = Column(SmallInteger)
    opstillingskredsnavn = Column(String(100))
    zone = Column(String(40))
    jordstykke_ejerlavkode = Column(Integer)
    jordstykke_matrikelnr = Column(String(10))
    jordstykke_esrejendomsnr = Column(Integer)
    kvh = Column(String(20))
    højde = Column(Float)
    adgangspunktid = Column(String(40))


class Adresseupdate(Base):
    __tablename__ = 'adresseupdates'

    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer = Column(BigInteger, nullable=False)
    adressetype = Column(String(40))
    adressematch = Column(String(128), nullable=False)
    # kode = Column(BigInteger, nullable=False)
    dawaid = Column(String(40), nullable=True)
    gyldigfra = Column(DateTime, nullable=False,
                       server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False,
                       server_default=default_end_date)
    post_string = Column(String(512))
    sidstopdateret = Column(DateTime, nullable=True)


class Attributter(Base):
    __tablename__ = 'attributter'
    updateid = Column(Integer, primary_key=True)
    enhedsnummer = Column(BigInteger)
    sekvensnr = Column(Integer)
    vaerdinavn = Column(String(128))
    vaerditype = Column(String(32))
    vaerdi = Column(Text())
    gyldigfra = Column(DateTime, nullable=False, server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False, server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


# class Branche(Base):
#     __tablename__ = 'Branche'
#     branchekode = Column(Integer, primary_key=True)
#     branchetekst = Column(String(255))

class Branche(Base):
    __tablename__ = 'branche'
    __table_args__ = (
        Index('branche_index',
              'branchekode',
              'branchetekst',
              unique=True),
    )
    brancheid = Column(Integer, primary_key=True)
    branchekode = Column(Integer, nullable=False)
    branchetekst = Column(String(160))


class Enhedsrelation(Base):
    __tablename__ = 'enhedsrelation'
    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer_deltager = Column(BigInteger, nullable=False)
    enhedsnummer_virksomhed = Column(BigInteger, nullable=False)
    enhedsnummer_organisation = Column(BigInteger, nullable=False)
    sekvensnr = Column(Integer, nullable=False)
    vaerdinavn = Column(String(256), nullable=False)
    vaerdi = Column(String(2**11))
    gyldigfra = Column(DateTime, nullable=False, server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False, server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


class Kontaktinfo(Base):
    __tablename__ = 'kontaktinfo'
    oplysningid = Column(Integer, primary_key=True)
    kontaktoplysning = Column(String(768), nullable=False, unique=True)




class Lastupdated(Base):
    __tablename__ = "lastupdated"
    updatetype = Column(String(255), primary_key=True)
    lastupdated = Column(DateTime, nullable=False)


class Livsforloeb(Base):
    __tablename__ = 'livsforloeb'
    __table_args__ = (
        Index('livsforleb_enheds_index',
              'enhedsnummer',
              'gyldigfra',
              'gyldigtil',
              unique=True),
    )
    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer = Column(BigInteger, nullable=False)
    gyldigfra = Column(DateTime, nullable=False,
                       server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False,
                       server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


class Navne(Base):
    __tablename__ = 'navne'
    navnid = Column(Integer, primary_key=True)
    navn = Column(String(1024), nullable=False, unique=True)


class Organisation(Base):
    __tablename__ = 'organisation'
    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer = Column(BigInteger, nullable=False)
    hovedtype = Column(String(256), nullable=False)
    navn = Column(String(256), nullable=False)
    gyldigfra = Column(DateTime, nullable=False,
                       server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False,
                       server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


class Person(Base):
    __tablename__ = 'person'
    enhedsnummer = Column(BigInteger, primary_key=True)
    forretningsnoegle = Column(BigInteger)
    statuskode = Column(String(10))
    stilling = Column(String(255))
    dataadgang = Column(Integer)
    enhedstype = Column(String(255))
    fejlbeskrivelse = Column(String(255))
    fejlregistreret = Column(Boolean)
    fejlvedindlaesning = Column(Boolean)
    naermestefremtidigedato = Column(DateTime)
    reklamebeskyttet = Column(Boolean)
    samtid = Column(Integer)
    sidstindlaest = Column(DateTime)
    sidstopdateret = Column(DateTime)


class Produktion(Base):
    __tablename__ = 'produktion'
    enhedsnummer = Column(BigInteger, primary_key=True)
    pnummer = Column(BigInteger, index=True)
    enhedstype = Column(String(256))
    dataadgang = Column(Integer)
    brancheansvarskode = Column(Integer)
    fejlbeskrivelse = Column(String(255))
    fejlregistreret = Column(Boolean)
    fejlvedindlaesning = Column(Boolean)
    naermestefremtidigedato = Column(DateTime)
    reklamebeskyttet = Column(Boolean)
    samtid = Column(Integer)
    sidstindlaest = Column(DateTime)
    sidstopdateret = Column(DateTime)
    virkningsaktoer = Column(String(64))


class Regnummer(Base):
    __tablename__ = 'regnummer'
    regid = Column(Integer, primary_key=True)
    regnummer = Column(String(20), nullable=False, unique=True)


class SpaltningFusion(Base):
    __tablename__ = 'spaltningfusion'
    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer = Column(BigInteger, nullable=False)
    enhedsnummer_organisation = Column(BigInteger, nullable=False)
    spalt_fusion = Column(String(40))
    indud = Column(String(40), nullable=False)
    gyldigfra = Column(DateTime, nullable=False,
                       server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False,
                       server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


class Statuskode(Base):
    __tablename__ = 'statuskode'
    __table_args__ = (
        Index('status_kode_kombi_index',
              'statuskode',
              'kreditoplysningskode',
              unique=True),
    )
    statusid = Column(Integer, primary_key=True)
    statuskode = Column(Integer, nullable=False)
    statustekst = Column(Text(), nullable=True)
    kreditoplysningskode = Column(Integer, nullable=False)
    kreditoplysningtekst = Column(Text(), nullable=True)


class Update(Base):
    __tablename__ = 'updates'
    updateid = Column(BigInteger, primary_key=True)
    enhedsnummer = Column(BigInteger, nullable=False)
    felttype = Column(String(256), nullable=False)
    kode = Column(BigInteger, nullable=False)
    gyldigfra = Column(DateTime, nullable=False,
                       server_default=default_start_date)
    gyldigtil = Column(DateTime, nullable=False,
                       server_default=default_end_date)
    sidstopdateret = Column(DateTime, nullable=True)


class Virksomhed(Base):
    __tablename__ = 'virksomhed'
    enhedsnummer = Column(BigInteger, primary_key=True)
    cvrnummer = Column(Integer, nullable=False, unique=True)
    enhedstype = Column(String(256))
    dataadgang = Column(Integer)
    brancheansvarskode = Column(Integer)
    fejlbeskrivelse = Column(String(255))
    fejlregistreret = Column(Boolean)
    fejlvedindlaesning = Column(Boolean)
    naermestefremtidigedato = Column(DateTime)
    reklamebeskyttet = Column(Boolean)
    samtid = Column(Integer)
    sidstindlaest = Column(DateTime)
    sidstopdateret = Column(DateTime)
    virkningsaktoer = Column(String(64))


class Virksomhedsform(Base):
    __tablename__ = 'virksomhedsform'
    virksomhedsformkode = Column(Integer, primary_key=True)
    kortbeskrivelse = Column(String(20))
    langbeskrivelse = Column(String(255))
    ansvarligdataleverandoer = Column(String(255))


class Virksomhedsstatus(Base):
    __tablename__ = 'virksomhedsstatus'
    virksomhedsstatusid = Column(Integer, primary_key=True)
    virksomhedsstatus = Column(String(768),
                               nullable=False, unique=True)


class Registration(Base):
    __tablename__ = 'registration'
    registrationid = Column(BigInteger, primary_key=True)
    adresse = Column(String(255))
    cvrnummer = Column(Integer)
    hovednavn = Column(String(255))
    kommunekode = Column(Integer)
    offentliggoerelseid = Column(Integer, unique=True)
    offentliggoerelsetidsstempel = Column(DateTime)
    opdateret = Column(DateTime)
    oprettet =  Column(DateTime)
    postnummer = Column(Integer)
    registreringtidsstempel = Column(DateTime)
    sidstopdateret = Column(DateTime)
    tekst  = Column(Text())
    ren_tekst  = Column(Text())
    virksomhedsformkode = Column(Integer)
    virksomhedsregistreringstatusser =  Column(String(255))
    

class CreateDatabase(object):
    def __init__(self):
        self.cvr_tables = [Aarsbeskaeftigelse,
                           erstAarsbeskaeftigelse,
                           AdresseDawa,
                           Adresseupdate,
                           Attributter,
                           Branche,
                           Enhedsrelation,
                           Kontaktinfo,
                           Kvartalsbeskaeftigelse,
                           erstKvartalsbeskaeftigelse,
                           Livsforloeb,
                           Maanedsbeskaeftigelse,
                           erstMaanedsbeskaeftigelse,
                           Navne,
                           Organisation,
                           Person,
                           Produktion,
                           Registration,
                           Regnummer,
                           SpaltningFusion,
                           Statuskode,
                           Update,
                           Virksomhed,
                           Virksomhedsform,
                           Virksomhedsstatus
                           ]
    
    
    def delete_tables(self):
        pass    

    def create_tables(self):
        # base.metadata.create_all(proxy_engine, tables=[x.__table__ for x in tables])
        print('Create Tables')
        for x in self.cvr_tables:
            try:
                print('Creating Table {0}'.format(x.__tablename__))
                x.__table__.create(proxy_engine)
            except Exception as e:
                print('Create Table Exception: ', x.__tablename__)
                print('Probably already exists')
                print(e)

    def create_query_indexes(self):
        """ Create Indexes used for queries

        :return:
        """
        #attributter_type_index = Index('attributter_type_index', Attributter.vaerdinavn)
        # enheds_vaerdinavn_index = Index('enheds_vaerdinavn_index',
        # Enhedsrelation.vaerdinavn, Enhedsrelation.vaerdi)

        update_type_index = Index('updates_type_index',
                                  Update.felttype,
                                  Update.kode,
                                  Update.enhedsnummer,
                                  Update.gyldigfra,
                                  Update.gyldigtil)
        #spalt_org = Index('spalt_virk_index', SpaltningFusion.enhedsnummer_organisation)
        #org_navn = Index('orgnavn_navn', Organisation.navn)
        #org_hovedtype = Index('orgnavn_hovedtype', Organisation.hovedtype, Organisation.navn)
        enheds_org_index = Index('enheds_org_index',
                                 Enhedsrelation.enhedsnummer_organisation)
        branchekode_index = Index('branchekode_index',
                                 Branche.branchekode
                                 )
        branchetekst_index = Index('branchetekst_index',
                                   Branche.branchetekst
                                   )
        # attributter_type_index,
                         # attributter_value_index,
                         # enheds_vaerdi_index,
                         # enheds_vaerdinavn_index,
                         # org_navn,
                         # org_hovedtype,
                         # spalt_org,
        query_indexes = [enheds_org_index, update_type_index,
                         branchekode_index, branchetekst_index
                         ]
        for index in query_indexes:
            print('Creating index', index.name)
            try:
                index.create(proxy_engine)
            except Exception as e:
                print(e)

        # text_indexes = [(Enhedsrelation, vaerdi)]

    def create_text_indexes(self):
        #enheds_vaerdi_index = Index('enheds_vaerdi_index', Enhedsrelation.vaerdi)  # text index
        #attributter_value_index = Index('attributter_value_index', Attributter.vaerdi)
        pass


    def create_update_indexes(self):
        """ create (unique) indexes of database that are vital
        for fast update (deletion/insert)

        :return:
        """
        print('Create Update Indexes')
        adresse_unique = Index('adresse_time_index',
                               Adresseupdate.enhedsnummer,
                               Adresseupdate.dawaid,
                               Adresseupdate.gyldigfra,
                               Adresseupdate.gyldigtil, unique=True)
        attr_enheds_index = Index('attributter_enhedsummer_index',
                                  Attributter.enhedsnummer,
                                  Attributter.vaerdinavn,
                                  Attributter.sekvensnr,
                                  Attributter.gyldigfra,
                                  Attributter.gyldigtil)
        enheds_deltager = Index('enheds_deltager',
                                Enhedsrelation.enhedsnummer_deltager)
        enheds_virksomhed_index = Index('enheds_virksomhed_index',
                                        Enhedsrelation.enhedsnummer_virksomhed)
        org_unique = Index('orgnavn_unique',
                           Organisation.enhedsnummer,
                           Organisation.hovedtype,
                           Organisation.navn,
                           unique=True)
        spalt_unique = Index('spalt_unique',
                             SpaltningFusion.enhedsnummer,
                             SpaltningFusion.enhedsnummer_organisation,
                             SpaltningFusion.spalt_fusion,
                             SpaltningFusion.indud,
                             SpaltningFusion.gyldigfra,
                             SpaltningFusion.gyldigtil, unique=True)
        update_enhedsnummer_index = Index('updates_unique_index',
                                          Update.enhedsnummer,
                                          Update.felttype,
                                          Update.kode,
                                          Update.gyldigfra,
                                          Update.gyldigtil)

        # enheds_unique = Index('enheds_deltager', Enhedsrelation.enhedsnummer_deltager,
        # Enhedsrelation.enhedsnummer_virksomhed, Enhedsrelation.enhedsnummer_organisation, Enhedsrelation.sekvensnr,
        # Enhedsrelation.vaerdinavn, Enhedsrelation.vaerdi, Enhedsrelation.gyldigfra, Enhedsrelation.gyldigtil)
        # Enhedsrelation.enhedsnummer_deltager, Enhedsrelation.enhedsnummer_organisation,
        # Enhedsrelation.sekvensnr, Enhedsrelation.vaerdinavn,
        # Enhedsrelation.vaerdi, Enhedsrelation.gyldigfra, Enhedsrelation.gyldigtil)

        indexes = [adresse_unique,
                   attr_enheds_index,
                   enheds_virksomhed_index,
                   enheds_deltager,
                   org_unique,
                   spalt_unique,
                   update_enhedsnummer_index
                   ]
        for index in indexes:
            print('Creating index', index.name)
            try:
                index.create(proxy_engine)
            except Exception as e:
                print('Index construction failed', index.name)
                print('Probably already exists')
                print(e)


    def create_my_sql_text_index(self, my_class, full_text_columns):
        mysql_full_text_command = """ALTER TABLE {0.__tablename__} ADD FULLTEXT ({1})"""
        mysql_command = mysql_full_text_command.format(my_class, ", ".join(column for column in full_text_columns))
        proxy_engine.execute(mysql_command)
