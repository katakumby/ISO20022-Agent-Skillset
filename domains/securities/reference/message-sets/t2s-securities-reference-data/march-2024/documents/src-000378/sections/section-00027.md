---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["4 reda.008.001.01 SecurityCreationStatusAdviceV01", "4.2 Structure"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.008.001.01"]
---

# 4.2 Structure

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCreStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  68
     MessageIdentification <MsgId> [1..1] Text 68
     CreationDateTime <CreDtTm> [0..1] DateTime 68
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 68
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C2, C3,
C4, C5,
C6
68
   ProcessingStatus <PrcgSts> [1..1] ± 69
   SupplementaryData <SplmtryData> [0..*] ± C7 70
4.3 Constraints
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
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities - Securities Reference Data 67 March 2024
```

