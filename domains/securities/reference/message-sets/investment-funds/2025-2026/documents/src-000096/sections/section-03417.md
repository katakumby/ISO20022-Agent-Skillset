---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.15 InvestmentAccount25", "66.1.24.15.4 IntermediaryInformation <IntrmyInf>"]
file_pages: [4663]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.15.4 IntermediaryInformation <IntrmyInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4663 to 4663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4663

```text
66.1.24.15.4  IntermediaryInformation <IntrmyInf>
Presence: [0..10]
Definition: Party that provides services relating to financial products to investors, eg, advice on products
and placement of orders for the investment fund.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary11" on
page 5014 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5014
   Account <Acct> [0..1] ± 5014
{Or   Role <Role> [0..1] CodeSet 5015
Or}   ExtendedRole <XtndedRole> [0..1] Text 5016
66.1.24.15.5  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see "PartyIdentification2Choice"
on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.24.16  CustomerConductClassification1Choice
Definition: Choice of formats for the specification of the customer conduct classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
66.1.24.16.1  Code <Cd>
Presence: [1..1]
Definition: Conduct type expressed as a code.
Datatype: "ConductClassification1Code" on page 5286
CodeName Name Definition
NSTA NonStandard Non standard or unusual.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4663 May 2026
```

