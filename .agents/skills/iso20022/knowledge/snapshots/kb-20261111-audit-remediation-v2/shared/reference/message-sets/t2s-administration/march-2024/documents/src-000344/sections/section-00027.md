---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.2 Structure"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.2 Structure

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RctAck> [1..1]  
   MessageIdentification <MsgId> [1..1]  34
     MessageIdentification <MsgId> [1..1] Text 34
     CreationDateTime <CreDtTm> [0..1] DateTime 34
     QueryName <QryNm> [0..1] Text 34
   Report <Rpt> [1..*]  34
     RelatedReference <RltdRef> [1..1]  35
       Reference <Ref> [1..1] Text 35
       MessageName <MsgNm> [0..1] Text 35
       ReferenceIssuer <RefIssr> [0..1] ± 35
     RequestHandling <ReqHdlg> [1..1]  36
       StatusCode <StsCd> [1..1] Text 36
       StatusDateTime <StsDtTm> [0..1] DateTime 36
       Description <Desc> [0..1] Text 36
   SupplementaryData <SplmtryData> [0..*] ± C3 36
4.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities - Administration - Maintenance 2023 -
2024
33 March 2024
```

