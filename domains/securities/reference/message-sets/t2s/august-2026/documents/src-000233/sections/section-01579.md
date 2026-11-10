---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "49.2 Structure"]
file_pages: [2204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.029.001.01"]
---

# 49.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2204 to 2204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2204

```text
49.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyMntncStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2205
     MessageIdentification <MsgId> [1..1] Text 2205
     CreationDateTime <CreDtTm> [0..1] DateTime 2205
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2205
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C2, C3,
C4, C5,
C6
2205
   ProcessingStatus <PrcgSts> [1..1] ± 2206
   SupplementaryData <SplmtryData> [0..*] ± C7 2207
49.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C3 DescriptionUsageRule
Description must be used alone as the last resort.
C4 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C5 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C6 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
49.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
Target2-Securities 2204 August 2026
```

