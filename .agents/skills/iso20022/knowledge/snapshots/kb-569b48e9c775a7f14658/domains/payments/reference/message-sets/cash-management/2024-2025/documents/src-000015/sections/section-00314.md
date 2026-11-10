---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["11 camt.012.001.08 DeleteLimitV08", "11.2 Structure"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.012.001.08"]
---

# 11.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <DelLmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 452
   LimitDetails <LmtDtls> [1..1]  452
{Or     CurrentLimitIdentification <CurLmtId> [1..1]  C2, C3 453
       SystemIdentification <SysId> [0..1] ± 454
       BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 454
       Type <Tp> [1..1]  455
{Or         Code <Cd> [1..1] CodeSet 455
Or}         Proprietary <Prtry> [1..1] Text 457
       AccountOwner <AcctOwnr> [0..1] ± 457
       AccountIdentification <AcctId> [0..1] ± 458
Or}     AllCurrentLimits <AllCurLmts> [1..1]  458
       SystemIdentification <SysId> [0..1] ± 459
       Type <Tp> [1..1]  459
{Or         Code <Cd> [1..1] CodeSet 459
Or}         Proprietary <Prtry> [1..1] Text 461
       AccountOwner <AcctOwnr> [0..1] ± 461
       AccountIdentification <AcctId> [0..1] ± 462
   SupplementaryData <SplmtryData> [0..*] ± C6 462
11.3 Constraints
C1 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C2 BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
C3 BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 451 February 2025
```

