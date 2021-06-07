"""
Defines and intitates Members database
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Activity(Base):
    __tablename__ = "activity"

    kid = Column(Integer, primary_key=True)
    code = Column(String(5), nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"<Activity(kid='{self.kid}', code='{self.code}', name='{self.name}')>"


class Address(Base):
    __tablename__ = "address"

    kid = Column(Integer, primary_key=True)
    address1 = Column(String(100), nullable=False)
    address2 = Column(String(50))
    cityId = Column(Integer, ForeignKey("city.kid"), nullable=False)
    company = Column(String(100))
    countryId = Column(Integer, ForeignKey("country.kid"), nullable=False, default=1)
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
    stateId = Column(Integer, ForeignKey("state.kid"))

    def __repr__(self):
        return (
            f"<Address(kid='{self.kid}', "
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

    kid = Column(Integer, primary_key=True)
    bulletinSort = Column(Integer, nullable=False)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return (
            f"<BulletinCategory(kid='{self.kid}', "
            f"name='{self.name}', "
            f"bulletinSort='{self.bulletinSort}')>"
        )


class City(Base):
    __tablename__ = "city"

    kid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<City(kid='{self.kid}', name='{self.name}')>"


class Contribution(Base):
    __tablename__ = "contribution"

    kid = Column(Integer, primary_key=True)
    amount = Column(Float, default=0.0, nullable=False)
    contributionDate = Column(DateTime, default=datetime.now(), nullable=False)
    contributionTypeId = Column(
        Integer, ForeignKey("contribution_type.kid"), nullable=False
    )
    deleted = Column(Boolean, default=False, nullable=False)
    memberId = Column(Integer, ForeignKey("member.kid"), nullable=False)
    stampCreated = Column(DateTime, default=datetime.now(), nullable=False)
    stampModified = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return (
            f"<Contribution(kid='{self.kid}', amount='{self.amount}', "
            f"contributionDate='{self.contributionDate}', "
            f"contributionTypeId='{self.contributionTypeId}', "
            f"deleted='{self.deleted}', "
            f"memberId='{self.memberId}', "
            f"stampCreated='{self.stampCreated}', "
            f"stampModified='{self.stampModified}')>"
        )


class ContributionType(Base):
    __tablename__ = "contribution_type"

    kid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<ContributionType(kid='{self.kid}', name='{self.name}')>"


class Country(Base):
    __tablename__ = "country"
    kid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True, unique=True)

    def __repr__(self):
        return f"<Country(kid='{self.kid}', name='{self.name}')>"


class EntityType(Base):
    __tablename__ = "entity_type"

    kid = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"<EntityType(kid='{self.kid}', name='{self.name}')>"


class KTable(Base):
    __tablename__ = "ktable"

    kid = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<KTable(kid='{self.kid}', name='{self.name}')>"


class Member(Base):
    __tablename__ = "member"

    kid = Column(Integer, primary_key=True)
    entityTypeId = Column(
        Integer, ForeignKey("entity_type.kid"), nullable=False, default=1
    )
    isDeceased = Column(Boolean, default=False, nullable=False)
    nameFirst = Column(String(50))
    nameLast = Column(String(50), nullable=False)
    memberCategoryId = Column(
        Integer, ForeignKey("member_category.kid"), nullable=False
    )
    postSalutation = Column(String(25))
    salutationId = Column(
        Integer, ForeignKey("salutation.kid"), nullable=False, default=1
    )
    stampCreated = Column(DateTime, default=datetime.now(), nullable=False)
    stampModified = Column(DateTime, default=datetime.now(), nullable=False)
    unknownAddress = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return (
            f"<Member(kid='{self.kid}', nameLast='{self.nameLast}', "
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

    memberId = Column(Integer, ForeignKey("member.kid"), primary_key=True)
    activityId = Column(Integer, ForeignKey("activity.kid"), primary_key=True)

    def __repr__(self):
        return (
            f"<MemberActivity(memberId='{self.memberId}', "
            f"activityId='{self.activityId}')>"
        )


class MemberCategory(Base):
    __tablename__ = "member_category"

    kid = Column(Integer, primary_key=True)
    annualDues = Column(Float, default=0.0, nullable=False)
    bulletinId = Column(Integer, ForeignKey("bulletin.kid"))
    description = Column(String(150))
    name = Column(String(25), nullable=False, unique=True)
    isMember = Column(Boolean, default=True, nullable=False)

    def __repr__(self):
        return (
            f"<MemberCategory(kid='{self.kid}', name='{self.name}', "
            f"description='{self.description}', annualDues='{self.annualDues}', "
            f"isMember='{self.isMember}', bulletinId='{self.bulletinId}')>"
        )


class Profile(Base):
    __tablename__ = "profile"

    kid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __repr__(self):
        return f"<Profile(kid='{self.kid}', name='{self.name}')>"


class Salutation(Base):
    __tablename__ = "salutation"

    kid = Column(Integer, primary_key=True)
    phrase = Column(String(25))

    def __repr__(self):
        return f"<Salutation(kid='{self.kid}', phrase='{self.phrase}')>"


class State(Base):
    __tablename__ = "state"

    kid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __repr__(self):
        return f"<State(kid='{self.kid}', name='{self.name}')>"


class Transaction(Base):
    __tablename__ = "transaction"

    kid = Column(Integer, primary_key=True)
    ktableId = Column(Integer, ForeignKey("ktable.kid"), nullable=False)
    profileId = Column(Integer, ForeignKey("profile.kid"))
    stampCreated = Column(DateTime, default=datetime.now(), nullable=False)
    valueOld = Column(String)
    valueNew = Column(String)
    valueChange = Column(String)

    def __repr__(self):
        return (
            f"<Transaction(kid='{self.kid}', ktableId='{self.ktableId}'), "
            f"profileId='{self.profileId}', "
            f"stampCreated='{self.stampCreated}', "
            f"valueOld='{self.valueOld}', "
            f"valueNew='{self.valueNew}', "
            f"valueChange='{self.valueChange}'>"
        )
