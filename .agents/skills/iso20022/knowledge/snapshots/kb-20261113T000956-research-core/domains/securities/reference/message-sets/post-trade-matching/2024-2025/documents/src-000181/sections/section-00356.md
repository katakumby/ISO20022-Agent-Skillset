---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.10 ConfirmationPartyDetails13", "7.1.20.10.4 AdditionalInformation <AddtlInf>"]
file_pages: [420, 421]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.10.4 AdditionalInformation <AddtlInf>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 420 to 421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 420

```text
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 669
7.1.20.10.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C1 "AdditonalDetailsGuideline"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation5" on
page 441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 442
   PartyContactDetails <PtyCtctDtls> [0..1] Text 442
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
7.1.20.10.5  InvestorProtectionAssociationMembership <InvstrPrtcnAssoctnMmbsh>
Presence: [0..1]
Definition: Indicates whether the confirmation party is a member of the investor protection association
required, eg, as per regulation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.20.11  TradingPartyCapacity4Choice
Definition: Choice of format for the trading capacity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 420
Or}   Proprietary <Prtry> [1..1] ± 422
7.1.20.11.1  Code <Cd>
Presence: [1..1]
Definition: Trading capacity expressed as an ISO 20022 code.
Datatype: "TradingCapacity4Code" on page 654
CodeName Name Definition
PRIN Principal Trading as Principal.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 420 February 2025
```

## File page 421

```text
CodeName Name Definition
CPRN CrossingPrincipal Crossing as a principal.
RISP RisklessPrincipal Trading as a riskless principal, ie, the
order to buy(sell) has been
simultaneously offset by an order to sell
(buy) with another party.
PROP Proprietary Trading for its firm. The transaction
affects the firm's own account, not that of
its customers.
AGEN Agent Trading as Agent on behalf of a
customer.
CAGN CrossingAgent Crossing as an agent.
OAGN OtherAgent Acting as an agent for a party other than
a customer.
PRAG PrincipalAgent Acting as an agent for some executions
and principal for others in the same
transaction.
BAGN ActingAgent Party acting as an agent for both
customer and another person.
INFI InvestmentFirm Any legal person whose regular
occupation or business is the provision
of one or more investment services to
third parties and/or the performance of
one or more investment activities on a
professional basis.
MKTM MarketMaker Dealer or specialist that is trading for
their own account in the OTC market.
Market makers are expected to maintain
an orderly market by being available to
buy or sell.
MLTF MultilateralTradingFacility Multilateral Trading Facility (MTF) is a
multilateral system which brings together
multiple third-party buying and selling
interests in financial instruments in a way
that results in a contract.
RMKT RegulatedMarket Regulated market on which financial
instruments can be traded according to
rules defined by the stock exchange.
SINT SystematicInternaliser Firms which, on an organised, frequent
and systematic basis, deal on their own
account by executing client orders
outside a regulated market or an MTF.
SIs have the obligation to provide, and
make public, a definite bid and offer
quote for liquid securities.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 421 February 2025
```

