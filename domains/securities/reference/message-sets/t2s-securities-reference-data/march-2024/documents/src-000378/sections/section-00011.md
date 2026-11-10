---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["3 reda.007.001.01 SecurityMaintenanceRequestV01", "3.2 Structure"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 3.2 Structure

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyMntncReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 24
   UpdateType <UpdTp> [1..1]  24
{Or     UpdateType <UpdTp> [1..3]  25
{Or       Add <Add> [1..1]  26
         FinancialInstrumentType <FinInstrmTp> [0..*] ± 26
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 27
         SupplementaryData <SplmtryData> [0..*] ± C14 35
Or       Delete <Del> [1..1]  36
         FinancialInstrumentType <FinInstrmTp> [0..*] ± 36
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 36
         SupplementaryData <SplmtryData> [0..*] ± C14 44
Or}       Modify <Modfy> [1..1]  45
         FinancialInstrumentType <FinInstrmTp> [0..*] ± 45
         FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 45
         SupplementaryData <SplmtryData> [0..*] ± C14 53
Or}     Replace <Rplc> [1..1]  54
       FinancialInstrumentType <FinInstrmTp> [0..*] ± 54
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..*] ± 54
       SupplementaryData <SplmtryData> [0..*] ± C14 62
   UpdateReason <UpdRsn> [0..1]  63
{Or     Code <Cd> [1..1] CodeSet 63
Or}     Proprietary <Prtry> [1..1] ± 63
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
63
   SupplementaryData <SplmtryData> [0..*] ± C14 64
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities - Securities Reference Data 22 March 2024
```

