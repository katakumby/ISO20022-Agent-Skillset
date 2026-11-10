---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.29 ThirdPartyRights <ThrdPtyRghts>"]
file_pages: [4658]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.29 ThirdPartyRights <ThrdPtyRghts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4658 to 4658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4658

```text
CodeName Name Definition
COLL Collateral Item is used as collateral.
NCOL NotCollateral Item is not used as collateral.
66.1.24.14.29  ThirdPartyRights <ThrdPtyRghts>
Presence: [0..1]
Definition: Details of third party rights.
ThirdPartyRights <ThrdPtyRghts> contains the following elements (see "ThirdPartyRights2" on
page 4596 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 4596
   DateTime <DtTm> [0..1] DateTime 4596
   Holder <Hldr> [0..1] ± 4596
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4597
   Amount <Amt> [0..1] Amount C1, C13 4597
   Description <Desc> [0..1] Text 4597
66.1.24.14.30  PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl>
Presence: [0..1]
Definition: Functionality permitted to a third party in the actions that may be taken on an account on
behalf of the investor.
PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> contains one of the following elements
(see "LevelOfControl1Choice" on page 4832 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4833
Or}   Proprietary <Prtry> [1..1] ± 4833
66.1.24.14.31  AccountingStatus <AcctgSts>
Presence: [0..1]
Definition: Specifies if the account is regarded as domestic or non-domestic for reporting purposes.
AccountingStatus <AcctgSts> contains one of the following elements (see
"AccountingStatus1Choice" on page 5184 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5184
Or}   Proprietary <Prtry> [1..1] ± 5185
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4658 May 2026
```

