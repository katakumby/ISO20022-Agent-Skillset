---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["7 reda.032.001.01 SecuritiesAccountDeletionRequestV01"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.032.001.01"]
---

# 7 reda.032.001.01 SecuritiesAccountDeletionRequestV01

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
7 reda.032.001.01
SecuritiesAccountDeletionRequestV01
7.1 MessageDefinition Functionality
The SecuritiesAccountDeletionRequest message is sent by an instructing party to the executing party to
request for the deletion of a securities account from the securities account reference data defined in the
system of the executing party.
Usage:
It aims at instructing the deletion of an existing securities account providing securities account
identification.
The result of the deletion is provided through a SecuritiesAccountStatusAdvice message.
Outline
The SecuritiesAccountDeletionRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountIdentification
Identification of the securities account to be deleted from the executing party system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 57
   AccountIdentification <AcctId> [1..1] ± 57
   SupplementaryData <SplmtryData> [0..*] ± C1 57
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.032.001.01
SecuritiesAccountDeletionRequestV01
Target2-Securities - Securities Account Reference Data 56 December 2019
```

