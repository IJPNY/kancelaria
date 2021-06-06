"""
Defines and intitates Members database
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Activity(Base):
    __tablename__ = "activity"

    aid = Column(Integer, primary_key=True)
    code = Column(String(5), nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"<Activity(aid='{self.aid}', code='{self.code}', name='{self.name}')>"


class Address(Base):
    __tablename__ = "address"

    adid = Column(Integer, primary_key=True)
    address1 = Column(String(100), nullable=False)
    address2 = Column(String(50))
    cityId = Column(Integer, ForeignKey("city.ctid"), nullable=False)
    company = Column(String(100))
    countryId = Column(Integer, ForeignKey("country.coid"), nullable=False, default=1)
    email = Column(String(100))
    fax = Column(String(25))
    isPrimary = Column(Boolean, default=True, nullable=False)
    isWork = Column(Boolean)
    memberId = Column(Integer, ForeignKey("member.mid"), nullable=False)
    phoneLand = Column(String(25))
    phoneMobile = Column(String(25))
    postalCode = Column(String(25))
    stampCreated = Column(DateTime, default=datetime.now(), nullable=False)
    stampModified = Column(DateTime, default=datetime.now(), nullable=False)
    stateId = Column(Integer, ForeignKey("state.sid"))

    def __repr__(self):
        return (
            f"<Address(adid='{self.adid}', "
            f"memberId='{self.memberId}', "
            f"address1='{self.address1}', "
            f"address2='{self.address2}', "
            f"cityId='{self.cityId}', "
            f"postalCode='{self.postalCode}', "
            f"stateId={self.stateId}, "
            f"contryId='{self.countryId}', "
            f"company='{self.company}', "
            f"email='{self.email}', "
            f"fax='{self.fax}', "
            f"phoneLand='{self.phoneLand}', "
            f"phoneMobile='{self.phoneMobile}', "
            f"isPrimary='{self.isPrimary}', "
            f"isWork='{self.isWork}', "
            f"stampCreated='{self.stampCreated}', "
            f"stampModified='{self.stampModified}')>"
        )


class BulletinCategory(Base):
    __tablename__ = "bulletin_category"

    bcid = Column(Integer, primary_key=True)
    bulletinSort = Column(Integer, nullable=False)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return (
            f"<BulletinCategory(bcid='{self.bcid}', "
            f"name='{self.name}', "
            f"bulletinSort='{self.bulletinSort}')>"
        )


class City(Base):
    __tablename__ = "city"

    ctid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<City(ctid='{self.ctid}', name='{self.name}')>"


class Country(Base):
    __tablename__ = "country"
    coid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True, unique=True)

    def __repr__(self):
        return f"<Country(coid='{self.coid}', name='{self.name}')>"


class EntityType(Base):
    __tablename__ = "entity_type"

    eid = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"<EntityType(eid='{self.eid}', name='{self.name}')>"


class Member(Base):
    __tablename__ = "member"

    mid = Column(Integer, primary_key=True)
    entityTypeId = Column(
        Integer, ForeignKey("entity_type.gid"), nullable=False, default=1
    )
    isDeceased = Column(Boolean, default=False, nullable=False)
    nameFirst = Column(String(50))
    nameLast = Column(String(50), nullable=False)
    memberCategoryId = Column(
        Integer, ForeignKey("member_category.mcid"), nullable=False
    )
    postSalutation = Column(String(25))
    salutationId = Column(
        Integer, ForeignKey("Salutation.sid"), nullable=False, default=1
    )
    stampCreated = Column(DateTime, default=datetime.now(), nullable=False)
    stampModified = Column(DateTime, default=datetime.now(), nullable=False)
    unknownAddress = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return (
            f"<Member(mid='{self.mid}', nameLast='{self.nameLast}', "
            f"nameFirst='{self.nameFirst}', stampCreated='{self.stampCreated}', "
            f"stampModified='{self.stampModified}', "
            f"entityTypeId='{self.entityTypeId}', "
            f"isDeceased='{self.isDeceased}', "
            f"memberCategoryId='{self.memberCategoryId}', "
            f"postSalutation='{self.postSalutation}', "
            f"salutationId='{self.salutationId}', "
            f"unknownAddress='{self.unknownAddress}')>"
        )


class MemberActivity(Base):
    __tablename__ = "member_activity"

    memberId = Column(Integer, ForeignKey("member.mid"), primary_key=True)
    activityId = Column(Integer, ForeignKey("activity.aid"), primary_key=True)

    def __repr__(self):
        return (
            f"<MemberActivity(memberId='{self.memberId}', "
            f"activityId='{self.activityId}')>"
        )


class MemberCategory(Base):
    __tablename__ = "member_category"

    mcid = Column(Integer, primary_key=True)
    annualDues = Column(Float, default=0.0, nullable=False)
    bulletinId = Column(Integer, ForeignKey("bulletin.bid"))
    description = Column(String(150))
    name = Column(String(25), nullable=False, unique=True)
    isMember = Column(Boolean, default=True, nullable=False)

    def __repr__(self):
        return (
            f"<MemberCategory(mcid='{self.mcid}', name='{self.name}', "
            f"description='{self.description}', annualDues='{self.annualDues}', "
            f"isMember='{self.isMember}', bulletinId='{self.bulletinId}')>"
        )


class Salutation(Base):
    __tablename__ = "salutation"

    sid = Column(Integer, primary_key=True)
    phrase = Column(String(25))

    def __repr__(self):
        return f"<Salutation(sid='{self.sid}', phrase='{self.phrase}')>"
