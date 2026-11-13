---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["29 reda.008.001.01 SecurityCreationStatusAdviceV01", "29.2 Structure"]
file_pages: [1754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.008.001.01"]
---

# 29.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1754 to 1754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1754

```text
29.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCreStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  1755
     MessageIdentification <MsgId> [1..1] Text 1755
     CreationDateTime <CreDtTm> [0..1] DateTime 1755
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 1755
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C2, C3,
C4, C5,
C6
1755
   ProcessingStatus <PrcgSts> [1..1] ± 1756
   SupplementaryData <SplmtryData> [0..*] ± C7 1757
29.3 Constraints
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
29.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities 1754 August 2026
```

