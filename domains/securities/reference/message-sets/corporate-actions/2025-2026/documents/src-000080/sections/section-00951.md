---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.29 CorporateActionEventType36Code"]
file_pages: [1176, 1177, 1178, 1179, 1180, 1181]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.29 CorporateActionEventType36Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1176 to 1181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1176

```text
CodeName Name Definition
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
RCLA Reclassification Securities related event which
reclassifies the distribution in various
types of income for US tax withholding
purposes.
16.2.2.29  CorporateActionEventType36Code
Definition: Specifies the corporate action event type.
Type: CodeSet
CodeName Name Definition
ACTV ActiveTradingStatus Trading in the security has commenced
or security has been re-activated after a
suspension in trading.
ATTI Attachment Combination of different security types to
create a unit. Units are usually
comprised of warrants and bonds or
warrants and equities. Securities may be
combined at the request of the security
holder or based on market convention.
BRUP Bankruptcy Legal status of a company unable to pay
creditors. Bankruptcy usually involves a
formal court ruling. Securities may
become valueless.
DFLT BondDefault Failure by the company to perform
obligations defined as default events
under the bond agreement and that have
not been remedied.
BONU BonusIssue Bonus or capitalisation issue. Security
holders receive additional assets free of
payment from the issuer, in proportion to
their holding.
EXRI CallOnIntermediateSecurities Call or exercise on nil paid securities or
intermediate securities resulting from an
intermediate securities distribution
(RHDI). This code is used for the second
event, when an intermediate securities'
issue (rights/coupons) is composed of
two events, the first event being the
distribution of intermediate securities.
CAPD CapitalDistribution Corporate event pays shareholders an
amount in cash issued from the capital
account. There is no reduction to the
face value of a single share (or the share
has no par value). The number of
circulating shares remains unchanged.
CAPG CapitalGainsDistribution Event is the distribution of profits
resulting from the sale of securities.
Shareholders of mutual funds, unit
trusts, or SICAVs are recipients of
capital gains distributions and are often
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1176 February 2026
```

## File page 1177

```text
CodeName Name Definition
reinvested in additional shares of the
fund.
CAPI Capitalisation Increase of the current principal of a debt
instrument without increasing the
nominal value. It normally arises from
the incorporation of due but unpaid
interest into the principal. This is
commonly done by increasing the pool
factor value, for example, capitalisation,
and negative amortisation.
DRCA CashDistributionFromNonEligibleSecuritiesSale
s
Distribution to shareholders of cash
resulting from the selling of non-eligible
securities, for example, in the frame of a
depositary receipt program.
DVCA CashDividend Distribution of cash to holders, in
proportion to their equity holding.
Ordinary dividends are recurring and
regular. Holder must take cash and may
be offered a choice of currencies.
CHAN Change Information regarding a change further
described in the corporate action details.
COOP CompanyOption Company option may be granted by the
company, allowing the holder to take up
shares at some future date(s) at a pre
arranged price in the company. A
company may not grant options which
enable the holder to take up unissued
shares at a time which is five or more
years from the date of the grant. Option
holders are not members of a company.
They are contingent creditors of a
company and hence may, in some
instances, be entitled to vote on and be
bound by a scheme of arrangement
between the creditors and the company.
As many options have multiple exercise
periods a company option will either
lapse or carry on to the next expiry date.
CLSA ClassActionProposedSettlement Situation where interested parties seek
restitution for financial loss. The security
holder may be offered the opportunity to
join a class action proceeding and would
need to respond with an instruction.
CONS Consent Procedure that aims to obtain consent of
holder to a proposal by the issuer or a
third party without convening a meeting.
For example, consent to change the
terms of a bond.
CONV Conversion Conversion of securities (generally
convertible bonds or preferred shares)
into another form of securities (usually
common shares) at a pre-stated price/
ratio.
CREV CreditEvent Occurrence of credit derivative for which
the issuer of one or several underlying
securities is unable to fulfill its financial
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1177 February 2026
```

## File page 1178

```text
CodeName Name Definition
obligations (as defined in terms and
conditions).
DECR DecreaseInValue Reduction of face value of a single share
or the value of fund assets. The number
of circulating shares/units remains
unchanged. This event may include a
cash payout to holders.
DETI Detachment Separation of components that comprise
a security, for example, usually units
comprised of warrants and bond or
warrants and equity. Units may be
broken up at the request of the security
holder or based on market convention.
DSCL Disclosure Requirement for holders or beneficial
owners to disclose their name, location
and holdings of any issue to the issuer.
DVOP DividendOption Distribution of a dividend to holders with
a choice of benefit to receive additional
securities or cash. To be distinguished
from DRIP as the company creates new
share capital in exchange for the
dividend rather than investing the
dividend in the market.
DRIP DividendReinvestment Dividend payment where holders can
keep cash or have the cash reinvested in
the market by the issuer into additional
shares in the issuing company. To be
distinguished from DVOP as the
company invests the dividend in the
market rather than creating new share
capital in exchange for the dividend.
DRAW Drawing Securities are redeemed in part before
the scheduled final maturity date. It is
done without any pool factor reduction.
The redemption is reflected in a debit of
the face amount (FAMT). Drawing is
distinct from partial call since drawn
bonds are chosen by lottery. Therefore,
not every holder is affected in the same
way.
DTCH DutchAuction Action by a party wishing to acquire a
security. Holders of the security are
invited to make an offer to sell, within a
specific price range. The acquiring party
will buy from the holder with lowest offer.
EXOF Exchange Exchange of holdings for other securities
and/or cash. The exchange can be either
mandatory or voluntary involving the
exchange of outstanding securities for
different securities and/or cash. For
example "exchange offer", "capital
reorganisation" or "funds separation".
REDM FinalMaturity Redemption of an entire issue
outstanding of securities, for example,
bonds, preferred equity, funds, by the
issuer or its agent, for example, asset
manager, at final maturity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1178 February 2026
```

## File page 1179

```text
CodeName Name Definition
MCAL FullCall Redemption of an entire issue
outstanding of securities, for example,
bonds, preferred equity, funds, by the
issuer or its agent, for example, asset
manager, before final maturity.
INCR IncreaseInValue Increase in the face value of a single
security. The number of circulating
securities remains unchanged.
PPMT InstalmentCall Instalment towards the purchase of
equity capital, subject to an agreement
between an issuer and a purchaser.
INTR InterestPayment Interest payment distributed to holders of
an interest bearing asset.
RHDI IntermediateSecuritiesDistribution Distribution of intermediate securities
that gives the holder the right to take part
in a future event.
LIQU LiquidationDividend Distribution of cash, assets or both. Debt
may be paid in order of priority based on
preferred claims to assets specified by
the security.
EXTM MaturityExtension As stipulated in the security's Terms and
Conditions, the issuer or the holder may
prolong the maturity date of a security.
After extension, the security details may
differ from the original issue. An issuer
initiated extension may be subject to
holder's approval.
MRGR Merger Exchange of outstanding securities,
initiated by the issuer which may include
options, as the result of two or more
companies combining assets, that is, an
external, third party company. Cash
payments may accompany share
exchange.
NOOF NonOfficialOffer Offers that are not supervised or
regulated by an official entity and being
offered by a party, for example a broker,
usually at a discount price, for example
broker offer, mini-tender, mini odd lot
offer or third party offer.
CERT NonUSTEFRADCertification Non-US beneficial owner certification
requirement for exchange of temporary
to permanent notes.
ODLT OddLotSalePurchase Sale or purchase of odd-lots to/from the
issuing company, initiated either by the
holder of the security or through an offer
made by the issuer.
OTHR OtherEvent Other event, use only when no other
event type applies, for example, a new
event type.
PARI PariPassu Occurs when securities with different
characteristics, for example, shares with
different entitlements to dividend or
voting rights, become identical in all
respects, for example, pari-passu or
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1179 February 2026
```

## File page 1180

```text
CodeName Name Definition
assimilation. May be scheduled in
advance, for example, shares resulting
from a bonus may become fungible after
a pre-set period of time, or may result
from outside events, for example,
merger, reorganisation, issue of
supplementary tranches.
PCAL PartialRedemptionWithoutPoolFactorReduction Securities are redeemed in part before
their scheduled final maturity date. It is
done without any pool factor reduction.
The redemption is reflected in a debit of
the face amount (FAMT).
PRED PartialRedemptionWithPoolFactorReduction Securities are redeemed in part before
their scheduled final maturity date. The
redemption is reflected in a pool factor
reduction. No movement of securities
occurs.
PINK PayInKind Interest payment, in any kind except
cash, distributed to holders of an interest
bearing asset.
PLAC PlaceOfIncorporation Changes in the state of incorporation for
US companies and changes in the place
of incorporation for foreign companies.
Where shares need to be registered
following the incorporation change, the
holder(s) may have to elect the registrar.
PDEF Prefunding Also called partial defeasance. Issuer
has money set aside to redeem a portion
of an issue and the indenture states that
the securities could be called earlier than
the stated maturity.
PRIO PriorityIssue Form of open or public offer where, due
to a limited amount of securities
available, priority is given to existing
shareholders.
BPUT PutRedemption Early redemption of a security at the
election of the holder subject to the
terms and condition of the issue with no
reduction in nominal value.
REDO Redenomination Event by which the unit (currency and/or
nominal) of a security is restated, for
example, nominal/par value of security in
a national currency is restated in another
currency.
REMK RemarketingAgreement Purchase and sale of remarketed
preferred equities/bonds through the
negotiation of interest rate between the
issuers and the holders.
BIDS RepurchaseOffer Repurchase offer / issuer bid / reverse
rights. Offer to existing holders by the
issuing company to repurchase its own
securities. The objective of the offer is to
reduce the number of outstanding
securities.
SPLR ReverseStockSplit Decrease in a company's number of
outstanding equities without any change
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1180 February 2026
```

## File page 1181

```text
CodeName Name Definition
in the shareholder's equity or the
aggregate market value at the time of
the split. Equity price and nominal value
are increased accordingly.
RHTS RightsIssue Offer to holders of a security to
subscribe for additional securities via the
distribution of an intermediate security.
Both processes are included in the same
event.
DVSC ScripDividend Dividend or interest paid in the form of
scrip.
SHPR SharesPremiumDividend Corporate event pays shareholders an
amount in cash issued from the shares
premium reserve. It is similar to a
dividend but with different tax
implications.
SMAL SmallestNegotiableUnit Modification of the smallest negotiable
unit of shares in order to obtain a new
negotiable unit.
SOFF SpinOff Distribution of securities issued by
another company. The distributed
securities may either be of a newly
created or of an existing company. For
example, spin-off, demerger, unbundling,
divestment.
DVSE StockDividend Dividend paid to shareholders in the
form of equities of the issuing
corporation.
SPLF StockSplit Increase in a corporation's number of
outstanding equities without any change
in the shareholder's equity or the
aggregate market value at the time of
the split. Equity price and nominal value
are reduced accordingly.
TREC TaxReclaim Event related to tax reclaim activities.
TEND Tender Offer made to holders by a third party,
requesting them to sell (tender) or
exchange their securities.
DLST TradingStatusDelisted Security is no longer able to comply with
the listing requirements of a stock
exchange and is removed from official
board quotation.
SUSP TradingStatusSuspended Trading in the security has been
suspended.
EXWA WarrantExercise Option offered to holders to buy (call
warrant) or to sell (put warrant) a specific
amount of stock, cash, or commodity, at
a predetermined price, during a
predetermined period of time (which
usually corresponds to the life of the
issue).
WTRC WithholdingTaxReliefCertification Certification process for withholding tax
reduction or exemption based on the tax
status of the holder.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1181 February 2026
```

