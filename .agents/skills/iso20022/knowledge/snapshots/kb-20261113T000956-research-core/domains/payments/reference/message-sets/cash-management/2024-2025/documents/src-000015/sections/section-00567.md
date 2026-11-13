---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["32 camt.071.001.05 DeleteStandingOrderV05", "32.4 Message Building Blocks", "32.4.2 StandingOrderDetails <StgOrdrDtls>"]
file_pages: [740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.071.001.05"]
---

# 32.4.2 StandingOrderDetails <StgOrdrDtls>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 740 to 740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 740

```text
32.4.2 StandingOrderDetails <StgOrdrDtls>
Presence: [1..1]
Definition: Identifies one particular limit set by the member and managed by the transaction
administrator.
StandingOrderDetails <StgOrdrDtls> contains one of the following StandingOrderOrAll4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StandingOrder <StgOrdr> [1..*]  740
     Identification <Id> [0..1] Text 740
     Account <Acct> [1..1] ± C6, C5 740
     AccountOwner <AcctOwnr> [0..1] ± 741
Or}   AllStandingOrders <AllStgOrdrs> [1..*]  742
     Account <Acct> [1..1] ± C6, C5 742
     AccountOwner <AcctOwnr> [0..1] ± 743
32.4.2.1  StandingOrder <StgOrdr>
Presence: [1..*]
Definition: Identification of single standing orders defined with specific characteristics.
StandingOrder <StgOrdr> contains the following StandingOrderIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 740
   Account <Acct> [1..1] ± C6, C5 740
   AccountOwner <AcctOwnr> [0..1] ± 741
32.4.2.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
32.4.2.1.2  Account <Acct>
Presence: [1..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Impacted by: C6 "IdentificationOrProxyPresenceRule", C5 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 04 February 2025 camt.071.001.05 DeleteStandingOrderV05
Cash Management - Maintenance 2024 - 2025 740 February 2025
```

