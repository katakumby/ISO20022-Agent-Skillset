---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.1 StandingOrderIdentification <StgOrdrId>", "31.4.2.1.1.1 Identification <Id>"]
file_pages: [717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.1.1 Identification <Id>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 717 to 717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 717

```text
StandingOrderIdentification <StgOrdrId> contains the following StandingOrderIdentification8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 717
   Account <Acct> [1..1] ± C8, C7 717
   AccountOwner <AcctOwnr> [0..1] ± 717
31.4.2.1.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
31.4.2.1.1.2  Account <Acct>
Presence: [1..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Impacted by: C8 "IdentificationOrProxyPresenceRule", C7 "IdentificationAndProxyGuideline"
Account <Acct> contains the following elements (see "CashAccount40" on page 783 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
31.4.2.1.1.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 717 February 2025
```

