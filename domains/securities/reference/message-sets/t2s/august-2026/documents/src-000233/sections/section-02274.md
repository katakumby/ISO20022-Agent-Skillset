---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.63 SettlingCapacity7Choice", "82.1.19.63.2 Proprietary <Prtry>"]
file_pages: [3049, 3050, 3051, 3052, 3053, 3054, 3055]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.63.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3049 to 3055.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3049

```text
CodeName Name Definition
RISP SettlingRisklessPrincipal Party settles trades that were
simultaneously offset.
82.1.19.63.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.64  CorporateActionEventType73Choice
Definition: Choice of format for the repair reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3049
Or}   Proprietary <Prtry> [1..1] ± 3056
Constraints
• EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event triggers a
securities movement as per the Event Interpretation Grid published by the Securities Market Practice
Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is decided
by the issuer and not by the holders.
82.1.19.64.1  Code <Cd>
Presence: [1..1]
Definition: Corporate action event type expressed as an ISO 20022 code.
Datatype: "CorporateActionEventType28Code" on page 3228
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3049 August 2026
```

## File page 3050

```text
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
DVCA CashDividend Distribution of cash to shareholders, in
proportion to their equity holding.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3050 August 2026
```

## File page 3051

```text
CodeName Name Definition
Ordinary dividends are recurring and
regular. Shareholder must take cash and
may be offered a choice of currency.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3051 August 2026
```

## File page 3052

```text
CodeName Name Definition
DVOP DividendOption Distribution of a dividend to shareholders
with a choice of benefit to receive.
Shareholders may choose to receive
shares or cash. To be distinguished from
DRIP as the company creates new share
capital in exchange for the dividend
rather than investing the dividend in the
market.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3052 August 2026
```

## File page 3053

```text
CodeName Name Definition
PRII InterestPaymentWithPrincipal Event which consists of two
components, the decrease of the
amortized value of a pool factor security
and an interest payment.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3053 August 2026
```

## File page 3054

```text
CodeName Name Definition
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
in the shareholder's equity or the
aggregate market value at the time of
the split. Equity price and nominal value
are increased accordingly.
RHTS RightsIssue Offer to holders of a security to
subscribe for additional securities via the
distribution of an intermediate security.
Both processes are included in the same
event.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3054 August 2026
```

## File page 3055

```text
CodeName Name Definition
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
WRTH Worthless Booking out of valueless securities.
ACCU Accumulation Funds related event in which the income
(for example accumulation units) that
accrues during an accounting period is
retained within the fund instead of being
paid away to investors. The retained
income is nonetheless deemed to have
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3055 August 2026
```

