---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.35 Intermediary46", "66.1.30.35.3 Account <Acct>", "66.1.30.35.3.1 Identification <Id>"]
file_pages: [5025]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.35.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5025 to 5025.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5025

```text
66.1.30.35.3.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.30.35.3.2  AccountServicer <AcctSvcr>
Presence: [1..1]
Definition: Institution servicing an account and assigning the account identifier to the account owner.
AccountServicer <AcctSvcr> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.30.35.4  WaivedTrailerCommissionIndicator <WvdTrlrComssnInd>
Presence: [0..1]
Definition: Non-enforcement of the right to all or part of a commission by the party entitled to the
commission.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.30.35.5  Role <Role>
Presence: [0..1]
Definition: Role or function performed by the intermediary.
Role <Role> contains one of the following elements (see "PartyRole2Choice" on page 5037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5038
Or}   Proprietary <Prtry> [1..1] ± 5040
66.1.30.35.6  PrimaryCommunicationAddress <PmryComAdr>
Presence: [0..*]
Definition: Communication device number or electronic address used for communication.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5025 May 2026
```

