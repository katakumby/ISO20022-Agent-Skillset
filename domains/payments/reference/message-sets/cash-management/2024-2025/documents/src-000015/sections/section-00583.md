---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.4 Message Building Blocks", "34.4.2 StandingOrderIdentification <StgOrdrId>"]
file_pages: [758]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.4.2 StandingOrderIdentification <StgOrdrId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 758 to 758.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 758

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
34.4.2 StandingOrderIdentification <StgOrdrId>
Presence: [1..1]
Definition: Identifies the standing order.
StandingOrderIdentification <StgOrdrId> contains the following StandingOrderIdentification8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 758
   Account <Acct> [1..1] ± C8, C7 758
   AccountOwner <AcctOwnr> [0..1] ± 759
34.4.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
34.4.2.2  Account <Acct>
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
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 758 February 2025
```

