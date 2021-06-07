import pytest

from kancelaria.members.datastore import (
    Activity,
    Address,
    BulletinCategory,
    City,
    Contribution,
    ContributionType,
    Country,
    EntityType,
    KTable,
    Member,
    MemberActivity,
    MemberCategory,
    Profile,
    Salutation,
    State,
    Transaction,
)


def test_activity_table_repr():
    row = Activity(code="x", name="foo")
    assert str(row) == "<Activity(kid='None', code='x', name='foo')>"


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
        == "<Address(kid='None', memberId='None', address1='foo', address2='None', cityId='1', postalCode='None', stateId=1, contryId='1', company='None', email='spam', fax='None', phoneLand='None', phoneMobile='None', isPrimary='True', isWork='False', stampCreated='None', stampModified='None')>"
    )


def test_bulletin_category_table_repr():
    row = BulletinCategory(name="foo", bulletinSort=1)
    assert str(row) == "<BulletinCategory(kid='None', name='foo', bulletinSort='1')>"


def test_city_table_repr():
    row = City(name="foo")
    assert str(row) == "<City(kid='None', name='foo')>"


def test_contribution_table_repr():
    row = Contribution(amount="100.00", contributionTypeId=1, deleted=False, memberId=1)
    assert (
        str(row)
        == "<Contribution(kid='None', amount='100.00', contributionDate='None', contributionTypeId='1', deleted='False', memberId='1', stampCreated='None', stampModified='None')>"
    )


def test_contribution_type_table_repr():
    row = ContributionType(name="foo")
    assert str(row) == "<ContributionType(kid='None', name='foo')>"


def test_country_table_repr():
    row = Country(name="foo")
    assert str(row) == "<Country(kid='None', name='foo')>"


def test_entity_type_table_repr():
    row = EntityType(name="foo")
    assert str(row) == "<EntityType(kid='None', name='foo')>"


def test_ktable_table_repr():
    row = KTable(name="foo")
    assert str(row) == "<KTable(kid='None', name='foo')>"


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
        == "<Member(kid='None', nameLast='bar', nameFirst='foo', stampCreated='None', stampModified='None', entityTypeId='2', isDeceased='False', memberCategoryId='1', postSalutation='None', salutationId='1', unknownAddress='False')>"
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
        == "<MemberCategory(kid='None', name='foo', description='spam', annualDues='100.0', isMember='True', bulletinId='1')>"
    )


def test_profile_table_repr():
    row = Profile(name="foo")
    assert str(row) == "<Profile(kid='None', name='foo')>"


def test_salutation_table_repr():
    row = Salutation(phrase="foo")
    assert str(row) == "<Salutation(kid='None', phrase='foo')>"


def test_state_table_repr():
    row = State(name="foo")
    assert str(row) == "<State(kid='None', name='foo')>"


def test_transaction_table_repr():
    row = Transaction(ktableId=1, profileId=1, valueOld="foo", valueNew="bar")
    assert (
        str(row)
        == "<Transaction(kid='None', ktableId='1'), profileId='1', stampCreated='None', valueOld='foo', valueNew='bar', valueChange='None'>"
    )
