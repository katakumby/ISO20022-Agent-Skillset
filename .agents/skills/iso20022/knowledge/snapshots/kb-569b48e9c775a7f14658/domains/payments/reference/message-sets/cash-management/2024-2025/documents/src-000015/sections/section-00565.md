---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["32 camt.071.001.05 DeleteStandingOrderV05"]
file_pages: [738]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.071.001.05"]
---

# 32 camt.071.001.05 DeleteStandingOrderV05

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 738 to 738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 738

```text
32 camt.071.001.05
DeleteStandingOrderV05
32.1 MessageDefinition Functionality
The DeleteStandingOrder message is sent by the system member to delete one or more standing
orders within the static data held by the system transaction administrator.
Outline
The DeleteStandingOrderV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
32.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <DelStgOrdr> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 739
   StandingOrderDetails <StgOrdrDtls> [1..1]  740
{Or     StandingOrder <StgOrdr> [1..*]  740
       Identification <Id> [0..1] Text 740
       Account <Acct> [1..1] ± C6, C5 740
       AccountOwner <AcctOwnr> [0..1] ± 741
Or}     AllStandingOrders <AllStgOrdrs> [1..*]  742
       Account <Acct> [1..1] ± C6, C5 742
       AccountOwner <AcctOwnr> [0..1] ± 743
   SupplementaryData <SplmtryData> [0..*] ± C7 744
Approved by the Payments SEG on 04 February 2025 camt.071.001.05 DeleteStandingOrderV05
Cash Management - Maintenance 2024 - 2025 738 February 2025
```

