---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.30 AccountingStatus <AcctgSts>"]
file_pages: [4615]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.30 AccountingStatus <AcctgSts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4615 to 4615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4615

```text
AdditionalRegulatoryInformation <AddtlRgltryInf> contains the following elements (see
"RegulatoryInformation1" on page 5018 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sector <Sctr> [0..1] Text 5018
   Branch <Brnch> [0..1] Text 5019
   Group <Grp> [0..1] Text 5019
   Other <Othr> [0..1] Text 5019
66.1.24.7.30  AccountingStatus <AcctgSts>
Presence: [0..1]
Definition: Specifies if the account party is regarded as domestic or non-domestic for reporting
purposes.
AccountingStatus <AcctgSts> contains one of the following elements (see
"AccountingStatus1Choice" on page 5184 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5184
Or}   Proprietary <Prtry> [1..1] ± 5185
66.1.24.7.31  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information such as remarks or notes that must be conveyed about the party and
or limitations and restrictions.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditiononalInformation13"
on page 4867 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Limitation <Lmttn> [0..1] Text 4867
   AdditionalInformation <AddtlInf> [0..1] Text 4867
   AccountValidation <AcctVldtn> [0..1] Text 4868
   Type <Tp> [0..1] Text 4868
   Regulator <Rgltr> [0..1] ± 4868
   Status <Sts> [0..1]  4868
{Or     Code <Cd> [1..1] CodeSet 4868
Or}     Proprietary <Prtry> [1..1] ± 4869
   Period <Prd> [0..1] ± 4869
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4615 May 2026
```

