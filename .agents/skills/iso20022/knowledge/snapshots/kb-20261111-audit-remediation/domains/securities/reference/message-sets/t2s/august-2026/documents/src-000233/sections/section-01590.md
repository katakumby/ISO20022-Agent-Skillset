---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["52 reda.032.001.01 SecuritiesAccountDeletionRequestV01"]
file_pages: [2216]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.032.001.01"]
---

# 52 reda.032.001.01 SecuritiesAccountDeletionRequestV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2216 to 2216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2216

```text
52 reda.032.001.01
SecuritiesAccountDeletionRequestV01
52.1 MessageDefinition Functionality
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
52.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2217
   AccountIdentification <AcctId> [1..1] ± 2217
   SupplementaryData <SplmtryData> [0..*] ± C1 2217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.032.001.01
SecuritiesAccountDeletionRequestV01
Target2-Securities 2216 August 2026
```

