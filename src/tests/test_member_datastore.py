import pytest

from kancelaria.members.datastore import (
    Activity,
    Address,
    BulletinCategory,
    City,
    Country,
    EntityType,
    Member,
    MemberActivity,
    MemberCategory,
    Salutation,
)


def test_activity_table_repr():
    row = Activity(code="x", name="foo")
    assert str(row) == "<Activity(aid='None', code='x', name='foo')>"


def test_address_table_repr():
    row = Address(
        address1="foo",
        cityId=1,
        countryId=1,
        email="spam",
        isPrimary=True,
        isWork=False,
        stateId=1,
    )
    assert (
        str(row)
        == "<Address(adid='None', memberId='None', address1='foo', address2='None', cityId='1', postalCode='None', stateId=1, contryId='1', company='None', email='spam', fax='None', phoneLand='None', phoneMobile='None', isPrimary='True', isWork='False', stampCreated='None', stampModified='None')>"
    )


def test_bulletin_category_table_repr():
    row = BulletinCategory(name="foo", bulletinSort=1)
    assert str(row) == "<BulletinCategory(bcid='None', name='foo', bulletinSort='1')>"


def test_city_table_repr():
    row = City(name="foo")
    assert str(row) == "<City(ctid='None', name='foo')>"


def test_country_table_repr():
    row = Country(name="foo")
    assert str(row) == "<Country(coid='None', name='foo')>"


def test_entity_type_table_repr():
    row = EntityType(name="foo")
    assert str(row) == "<EntityType(eid='None', name='foo')>"


def test_member_table_repr():
    row = Member(
        entityTypeId=2,
        isDeceased=False,
        nameFirst="foo",
        nameLast="bar",
        memberCategoryId=1,
        salutationId=1,
        unknownAddress=False,
    )
    assert (
        str(row)
        == "<Member(mid='None', nameLast='bar', nameFirst='foo', stampCreated='None', stampModified='None', entityTypeId='2', isDeceased='False', memberCategoryId='1', postSalutation='None', salutationId='1', unknownAddress='False')>"
    )


def test_member_activity_repr():
    row = MemberActivity(memberId=1, activityId=2)
    assert str(row) == "<MemberActivity(memberId='1', activityId='2')>"


def test_member_category_table_repr():
    row = MemberCategory(
        bulletinId=1,
        name="foo",
        description="spam",
        annualDues=100.00,
        isMember=True,
    )
    assert (
        str(row)
        == "<MemberCategory(mcid='None', name='foo', description='spam', annualDues='100.0', isMember='True', bulletinId='1')>"
    )


def test_salutation_table_repr():
    row = Salutation(phrase="foo")
    assert str(row) == "<Salutation(sid='None', phrase='foo')>"
