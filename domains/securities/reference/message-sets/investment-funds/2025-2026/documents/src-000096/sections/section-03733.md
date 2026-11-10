---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.31 RegulatoryInformation1", "66.1.30.31.2 Branch <Brnch>"]
file_pages: [5019]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.31.2 Branch <Brnch>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5019 to 5019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5019

```text
Definition: Sector of economic activity, for example, SAE in the Italian market.
Datatype: "Max35Text" on page 5403
66.1.30.31.2  Branch <Brnch>
Presence: [0..1]
Definition: Branch of economic activity, for example, RAE in the Italian market.
Datatype: "Max35Text" on page 5403
66.1.30.31.3  Group <Grp>
Presence: [0..1]
Definition: Group of economic activity, for example, a code issued by a regulator.
Datatype: "Max35Text" on page 5403
66.1.30.31.4  Other <Othr>
Presence: [0..1]
Definition: Other regulatory information.
Datatype: "Max35Text" on page 5403
66.1.30.32  CertificationType1Choice
Definition: Choice of formats for the specification of the certificate type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5019
Or}   Proprietary <Prtry> [1..1] ± 5020
66.1.30.32.1  Code <Cd>
Presence: [1..1]
Definition: Certificate type expressed as a code.
Datatype: "CertificateType2Code" on page 5282
CodeName Name Definition
AMLC AntiMoneyLaundering Anti-money laundering certification form.
DVLC DrivingLicense Government issued form of picture
identification - driving license.
DFOR DueFormationAndOrganisation Certification of due formation and
organisation.
GOST GoodStanding Certificate of good standing.
IDEN IdentityCard Government issued form of picture
identification - identity card.
INCU Incumbency Certification of incumbency.
LREF LetterOfReference Letter of reference.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5019 May 2026
```

