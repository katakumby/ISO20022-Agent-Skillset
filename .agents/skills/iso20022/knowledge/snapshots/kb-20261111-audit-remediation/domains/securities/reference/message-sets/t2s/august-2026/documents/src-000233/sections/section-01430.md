---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["33 reda.013.001.01 SecurityDeletionRequestV01", "33.2 Structure"]
file_pages: [2040]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.013.001.01"]
---

# 33.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2040 to 2040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2040

```text
33.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2040
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
2041
   SupplementaryData <SplmtryData> [0..*] ± C6 2042
33.3 Constraints
C1 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C2 DescriptionUsageRule
Description must be used alone as the last resort.
C3 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C4 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C5 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
33.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
33.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities 2040 August 2026
```

